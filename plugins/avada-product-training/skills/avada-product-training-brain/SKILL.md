---
name: avada-product-training-brain
description: Tra cứu và áp dụng brain Avada Product Training — business/ecommerce economics, merchant stage, customer journey, KPI, interactive case clinic, product mechanism, value/ROI/pricing, learner progress và feedback. Dùng khi hỏi về curriculum BA/Product Training, Session 1–4, Blume/Promix/Bloom, Alia, Order Editing, bài app deep dive, thiết kế workshop/Kahoot, hoặc cách biến observation thành product argument. Dùng cả khi đang làm việc ngoài repo này.
---

# Avada Product Training Brain

Tri thức nằm ở `${CLAUDE_PLUGIN_ROOT}/knowledge/`. Đọc file liên quan trước khi trả lời; không trả lời từ trí nhớ hoặc biến learner claim thành fact.

## Bản đồ nhanh

| Nhu cầu | Đọc trước |
|---|---|
| Hiểu toàn bộ chương trình và Session 1–4 | `knowledge/course-map.md` |
| Phân tích merchant/business/app | `knowledge/product-operator-method.md` |
| Thiết kế case clinic, interaction, Kahoot | `knowledge/interactive-training.md` |
| Viết product argument, ROI, pricing ceiling | `knowledge/templates/product-argument.md` |
| Tổng hợp progress qua ba buổi | `knowledge/progress/2026-10-27-three-session-progress.md` |
| Đọc learner feedback và facilitator reflection | `knowledge/progress/2026-10-27-learner-feedback-reflection.md` |
| Recap Session 3 cho learner | `knowledge/sessions/2026-10-27-session-3-recap.md` |
| Team Bloom learner deck và evidence boundary | `knowledge/cases/2026-10-27-team-bloom.md` |
| Tìm nguồn Notion/Slack/Slides/Git | `knowledge/sources/source-map.md` |
| Chọn video/source học kèm active prompt | `knowledge/sources/learning-resources.md` |
| Không biết đọc gì | `knowledge/00-index.md` |

## Quy trình trả lời

1. Xác định câu hỏi thuộc curriculum, business analysis, product argument, facilitation, progress/feedback hay source verification.
2. Đọc `knowledge/00-index.md`, sau đó đọc file chuyên đề gần nhất trong bảng trên.
3. Nếu câu hỏi liên quan một session/case cụ thể, đọc cả source map và case/session note trước khi kết luận.
4. Tách rõ trong output:
   - observed fact;
   - learner interpretation;
   - training assumption;
   - vendor claim;
   - modeled value;
   - experiment-verified incrementality;
   - unknown/data needed.
5. Nếu thiết kế bài tập, yêu cầu learner tạo artifact hoặc decision; attendance, vocabulary và slide completion không phải learning proof.
6. Nếu đánh giá learner/presenter, mô tả evidence, capability progress và improvement gap; không dùng giọng thầy chấm/khen học viên.
7. Nếu brain thiếu dữ liệu, nói rõ đã đọc file nào và còn thiếu source nào; không suy đoán để lấp chỗ trống.

## Product doctrine

```text
Research real business
→ identify stage + ICP + KPI leak
→ explain mechanism
→ model contribution / ROI
→ set evidence boundary
→ define pricing ceiling
→ pilot / holdout / stop rule
```

Không bắt đầu bằng competitor feature hoặc UI mockup.

Một metric bề mặt chưa phải business outcome:

```text
usage / response / opt-in
→ behavior changed
→ business KPI changed
→ contribution or cost changed
→ merchant ROI
```

## Training doctrine

```text
Exposure ≠ understanding
Attendance ≠ learning
Correct vocabulary ≠ usable judgment
```

Loop cần tạo:

```text
observe
→ hypothesize
→ calculate
→ test against evidence
→ receive challenge
→ correct model/artifact
→ prove capability/outcome
→ encode learning
```

AI được dùng để tìm, tính, đối chiếu và validate; không được làm thay observation hoặc judgment mà bài tập đang xây.

## Bất biến nguồn

- **Blume skincare** và **Bloom Nutrition** là hai brand/case khác nhau.
- Notion `Training BA 20/10` có hai transcription block; chỉ block Bloom ngày 27/10 là Session 3.
- Hai feedback ngày 21/10 và 24/10 được gửi trước Session 3; không dùng chúng làm post-Session-3 proof.
- Team Bloom deck là learner artifact; các con số trong deck cần primary-source verification trước khi trở thành instructor facts.
- Alia/Graza `4.5% → 13.8%` là vendor case claim, không phải universal causal benchmark.
- Order Editing là external follow-on case, không phải nội dung được claim đã trình bày trong transcript Session 3.
- Không đưa transcript raw, credential, private customer data hoặc binary slide vào plugin. Source artifacts đầy đủ nằm ở repo training được trỏ trong `knowledge/sources/source-map.md`.

## Khi thiết kế buổi tiếp theo

Dùng progressive scaffold:

```text
foundation diagnostic
→ short refresh
→ instructor worked case
→ contrasting learner case
→ peer challenge
→ live revision
→ spaced repetition
```

Kahoot dùng để chẩn đoán terminology, denominator, grain và arithmetic; không thay thế case judgment.

## Verification

Trước khi trả lời:

- đã đọc đúng file nguồn;
- đã giữ đúng ranh giới Session 2/3 và Blume/Bloom;
- không biến `n=2` feedback thành cohort statistic;
- arithmetic được tính bằng tool khi có số;
- fact/assumption/vendor claim/model được label;
- output nêu artifact, decision hoặc next test rõ ràng.
