# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B2 | SPURIOUS | 2 |
| center | B3 | MISSING | 1 |
| center | B3 | WRONG_CLASS | 1 |
| center | C0 | MISSING | 1 |
| center | C0 | SPURIOUS | 1 |
| edge | B2 | ATTRIBUTE | 1 |
| edge | B3 | MISSING | 3 |
| mid | B2 | ATTRIBUTE | 1 |
| mid | B3 | MISSING | 1 |
| mid | B3 | SPURIOUS | 3 |

## Top defects
- SPURIOUS: 6 (ví dụ frame adasind_019560.jpg)
- MISSING: 6 (ví dụ frame adasind_019560.jpg)
- ATTRIBUTE: 2 (ví dụ frame adasind_062370.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy:
  - Lỗi nổi bật nhất tập trung ở hai dạng `MISSING` và `SPURIOUS` tại các vùng `edge` và `mid` (như ca `adasind_167700.jpg` L10+R6, M5 và `adasind_199770.jpg` R6, M6).
  - Về phía mô hình AI (`why = E4_model_domain`): Model YOLO ban đầu được huấn luyện trên tập dữ liệu phẳng thông thường (COCO dataset), do đó bị hiện tượng lệch miền dữ liệu (Domain Shift) nghiêm trọng khi đối mặt với hiệu ứng mắt cá (fisheye distortion) ở vùng `mid` và `edge`. Khi vật thể bị kéo cong và nén lại theo hình bán cầu, mô hình mất khả năng nhận diện hình học đặc trưng dẫn đến bỏ sót (MISSING) hoặc hallucinate nhận diện nhầm các mảng bóng râm trên mặt đường thành xe cộ (SPURIOUS).
  - Về phía người gán nhãn (`why = E1_annotator_error`): Annotator bỏ sót các đối tượng nhỏ sát mép vành kính và chưa bao quát vùng loại trừ `ego_body` ở góc dưới trái khung hình.
- Cách sửa và ai nhận việc (`owner`):
  - `owner = annotator`: Thực hiện rework bổ sung đầy đủ polygon `ignore_region` nhãn `ego_body` cho góc dưới bên trái ở cả 3 frame (theo rule R06, R07); rà soát kỹ các vật thể đạt chiều cao tối thiểu H ≥ 40px ở rìa kính và cập nhật thuộc tính `truncated = true` khi vật thể chạm viền.
  - `owner = ai_team`: Bổ sung dữ liệu camera fisheye góc siêu rộng vào tập huấn luyện của model; mở rộng taxonomy để thêm lớp `ThreeWheeler`; thêm lớp lọc hậu xử lý (post-processing filter) loại bỏ các phát hiện nằm ngoài vòng kính `lens_border`.
- Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule):
  - Ảnh minh chứng tại [submission/screenshots/evidence_1.png](file:///d:/Study/VinUni/Day11/src/K4-L2-DAY11-PhamVanNhatTruong-2A202602304/submission/screenshots/evidence_1.png) chỉ rõ vị trí cánh tay áo caro và tay lái xe ego ở góc dưới trái cần vẽ `ego_body`.
  - Các dòng findings trong [submission/findings.csv](file:///d:/Study/VinUni/Day11/src/K4-L2-DAY11-PhamVanNhatTruong-2A202602304/submission/findings.csv): dòng `r1_craft` (L6+R4 WRONG_CLASS, R6 MISSING) và dòng `r3_diag` (L10+R6 MISSING LR_noM, M5 SPURIOUS).
  - Quy tắc đối chiếu: Rule R01 (ngưỡng chiều cao H=40), Rule R04 (ánh xạ class ThreeWheeler), Rule R06/R07 (vùng loại trừ `ego_body`).

