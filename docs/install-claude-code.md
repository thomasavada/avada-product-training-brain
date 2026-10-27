# Install — Claude Code

```text
/plugin marketplace add https://github.com/thomasavada/avada-product-training-brain.git
/plugin install avada-product-training@avada-training
```

Start a new session, then try:

```text
/teach-me AOV, COGS và contribution
/analyze-brand Bloom Nutrition
/analyze-app Order Editing
/product-training Session 3 đã thay đổi capability gì?
```

One-session local test:

```bash
claude --plugin-dir /absolute/path/to/avada-product-training-brain/plugins/avada-product-training
```

Expected negative test: a request to write an unrelated Python function must not invoke a training skill.
