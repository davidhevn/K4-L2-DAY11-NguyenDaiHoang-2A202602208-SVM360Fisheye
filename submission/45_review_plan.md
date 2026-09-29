# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| `B3-dense / adasind_167700.jpg` | 4 ca: 1 WRONG_CLASS (ThreeWheeler vs Truck), 1 SPURIOUS box lỏng, 1 MISSING ở rìa của model, và lỗi thiếu `ego_body` | Cảnh giao thông đô thị có mật độ đông đúc nhất, tập trung nhiều xe ba bánh và người đi bộ đan xen; lỗi phân loại và thiếu ignore_region ở đây gây hậu quả lớn nhất (P0/P1) | Ảnh chụp [submission/screenshots/evidence_1.png](file:///d:/Study/VinUni/Day11/src/K4-L2-DAY11-PhamVanNhatTruong-2A202602304/submission/screenshots/evidence_1.png), dòng finding L6+R4 và tọa độ polygon `ego_body` |
| `B3-dense / adasind_199770.jpg` | 4 ca: 3 ca MISSING ở vùng mid và edge; 1 ca SPURIOUS do model bắt ảo tại rìa kính | Khu vực rìa ống kính fisheye (zone edge) bị méo nén quang sai cực lớn; cần kiểm tra ranh giới cắt và khả năng bắt vật thể sát vành đen lens_border | Dòng finding R6 MISSING, M6 SPURIOUS và bảng so sánh zone trong `r1_craft/compare.md` |

Giới hạn của kết luận từ ba frame ADASIND: Cụm 3 frame chỉ là một mẫu vi mô (micro-sample) trong điều kiện ánh sáng ban ngày nắng gắt, không thể đại diện cho toàn bộ phân phối giao thông thực tế (thiếu cảnh ban đêm, mưa gió, chói lóa ngược sáng) và chỉ ghi nhận từ một góc camera đơn, không đại diện được sự phối hợp 4 camera của hệ thống SVM 360.

## Chuyển sang kế hoạch bốn camera giả lập

Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv` (kể cả tránh đếm nhiều frame liền nhau trong cùng cảnh như nhiều ca độc lập), và vì sao kế hoạch đó chỉ giúp tìm ca cần soi, chưa đo được tỷ lệ lỗi:
- Để kiểm soát độ phủ 200 frame, áp dụng phương pháp lấy mẫu phân tầng (Stratified Sampling) đồng đều cho cả 4 camera (`front`, `rear`, `left`, `right`) chia theo nhóm `normal` và `hard`. Để tránh trùng lặp cảnh, bắt buộc áp dụng khoảng cách trích xuất thời gian (temporal stride tối thiểu cách nhau 3–5 giây hoặc 60–100 frame liên tiếp) và kích hoạt lấy mẫu theo biến cố động lực học xe (rẽ góc cua gấp, lùi đỗ, phanh đột ngột).
- Kế hoạch này được thiết kế theo hướng tìm kiếm ca lỗi biên (targeted edge-case sampling) nhằm tối ưu hóa việc phát hiện khiếm khuyết trong guideline và mô hình, chứ không phải lấy mẫu ngẫu nhiên độc lập (IID random sampling). Do đó, tỷ lệ lỗi trên tập 200 frame này sẽ bị thổi phồng có chủ đích và không thể dùng làm thước đo tỷ lệ lỗi tổng thể trên toàn bộ 50.000 frame vận hành thực tế.

