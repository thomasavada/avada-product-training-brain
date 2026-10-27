#!/usr/bin/env python3
"""Query the bundled brain graph without requiring Graphify."""
from __future__ import annotations
import argparse,json
from collections import Counter,deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GRAPH=ROOT/'knowledge'/'graph'/'graph.json'

def load(): return json.loads(GRAPH.read_text(encoding='utf-8'))

def resolve(nodes,query):
 q=query.casefold().strip()
 exact=[n for n in nodes if n['label'].casefold()==q or n['source_file'].casefold()==q]
 if len(exact)==1:return exact[0]
 partial=[n for n in nodes if q in n['label'].casefold() or q in n['source_file'].casefold()]
 if len(partial)==1:return partial[0]
 raise SystemExit(json.dumps({'ok':False,'query':query,'matches':[n['label'] for n in partial[:20]]},ensure_ascii=False))

def adjacency(graph):
 adj={n['id']:[] for n in graph['nodes']}
 for e in graph['links']:
  adj[e['source']].append((e['target'],e));adj[e['target']].append((e['source'],e))
 return adj

def path(graph,a,b):
 nodes=graph['nodes'];by={n['id']:n for n in nodes};start=resolve(nodes,a);goal=resolve(nodes,b);adj=adjacency(graph)
 q=deque([start['id']]);prev={start['id']:None};via={}
 while q:
  cur=q.popleft()
  if cur==goal['id']:break
  for nxt,e in adj[cur]:
   if nxt not in prev:prev[nxt]=cur;via[nxt]=e;q.append(nxt)
 if goal['id'] not in prev:return {'ok':False,'from':start['label'],'to':goal['label'],'path':[]}
 ids=[];cur=goal['id']
 while cur is not None:ids.append(cur);cur=prev[cur]
 ids.reverse();steps=[]
 for i,nid in enumerate(ids):
  item={'node':by[nid]['label'],'source_file':by[nid]['source_file']}
  if i: item['edge']={'relation':via[nid]['relation'],'confidence':via[nid]['confidence']}
  steps.append(item)
 return {'ok':True,'hops':len(ids)-1,'path':steps}

def god(graph,top):
 degree=Counter()
 for e in graph['links']:degree[e['source']]+=1;degree[e['target']]+=1
 by={n['id']:n for n in graph['nodes']}
 return {'ok':True,'nodes':[{'label':by[i]['label'],'degree':d,'source_file':by[i]['source_file']} for i,d in degree.most_common(top)]}

def neighbors(graph,q):
 node=resolve(graph['nodes'],q);by={n['id']:n for n in graph['nodes']};adj=adjacency(graph)
 return {'ok':True,'node':node['label'],'source_file':node['source_file'],'neighbors':[{'label':by[n]['label'],'source_file':by[n]['source_file'],'relation':e['relation'],'confidence':e['confidence']} for n,e in adj[node['id']]]}

def main():
 p=argparse.ArgumentParser();sub=p.add_subparsers(dest='cmd',required=True)
 q=sub.add_parser('path');q.add_argument('a');q.add_argument('b')
 q=sub.add_parser('neighbors');q.add_argument('query')
 q=sub.add_parser('god-nodes');q.add_argument('--top',type=int,default=10)
 a=p.parse_args();g=load()
 result=path(g,a.a,a.b) if a.cmd=='path' else neighbors(g,a.query) if a.cmd=='neighbors' else god(g,a.top)
 print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
