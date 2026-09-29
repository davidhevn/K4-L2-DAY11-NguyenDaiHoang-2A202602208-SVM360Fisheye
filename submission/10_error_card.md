# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B4 | MISSING | 4 |
| center | B4 | SPURIOUS | 5 |
| center | C0 | MISSING | 1 |
| center | C0 | SPURIOUS | 1 |
| edge | B4 | MISSING | 3 |
| edge | B4 | SPURIOUS | 2 |
| mid | B4 | BOX_GEOMETRY | 1 |
| mid | B4 | MISSING | 4 |
| mid | B4 | SPURIOUS | 10 |
| mid | C0 | SPURIOUS | 1 |
| unknown | B4 | MISSING | 1 |

## Top defects
- SPURIOUS: 19 (ví dụ frame adasind_019560.jpg)
- MISSING: 13 (ví dụ frame adasind_019560.jpg)
- BOX_GEOMETRY: 1 (ví dụ frame adasind_258420.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy: Lỗi SPURIOUS (19 lỗi) chiếm áp đảo. Nguyên nhân chính là do hệ thống model dự đoán quá "nhạy" ở khu vực rìa ảnh (mid và edge), nơi hình ảnh bị biến dạng và lẫn nhiều chi tiết thân xe. Việc thiếu polygon `ignore_region` (`ego_body`) càng khiến model dễ nhận nhầm các chi tiết này thành vật thể.
- Cách sửa và ai nhận việc (`owner`): Data Ops cần thắt chặt quy trình yêu cầu vẽ `lens_border` và `ego_body` để lọc nhiễu ngay từ đầu vào. AI Team cần nghiên cứu chỉnh ngưỡng tự tin (confidence threshold) hoặc train thêm data có masking viền.
- Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule): Frame `adasind_019560.jpg` ghi nhận hàng loạt lỗi SPURIOUS. Dựa trên luật R06 (Ignore Region).
