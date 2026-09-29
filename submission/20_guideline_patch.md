# Guideline patch

- **Rule mới đề xuất:** Khi vẽ polygon `ignore_region` cho `lens_border`, phải vẽ sát mép viền đen thực tế của ảnh fisheye, không vẽ dư vào vùng ảnh hữu ích.
- **Áp dụng cho:** `ignore_region` (attribute: `lens_border`)
- **Vì sao luật hiện tại (`docs/02-rules-vi.md`) không đủ:** Luật hiện tại chỉ yêu cầu "vẽ polygon che phần viền đen" nhưng chưa quy định độ lệch tối đa cho phép, dẫn đến việc nhiều Annotator vẽ lẹm vào phần xe cộ ở sát mép ảnh.
- **`rules_version` mới:** v1.1.0
- **Hiệu lực từ:** Round R3 (hoặc các dự án tương lai)
