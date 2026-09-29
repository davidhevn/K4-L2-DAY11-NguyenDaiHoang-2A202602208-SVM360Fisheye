# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| adasind_258420.jpg | 3 ca SPURIOUS | Xảy ra lỗi H<40px hàng loạt, cho thấy Annotator chưa ước lượng được kích thước ở vùng bị biến dạng. | Kích thước box (width/height) và tọa độ. |
| adasind_270517.jpg | 2 ca thiếu lens_border | Đây là lỗi hệ thống bỏ sót bước vẽ polygon, ảnh hưởng tới bước post-processing che viền đen camera. | Thiếu thuộc tính reason = lens_border. |

Giới hạn của kết luận từ ba frame ADASIND: Số lượng frame quá ít không đại diện cho độ phong phú của dữ liệu thực tế (thời tiết, mật độ giao thông, loại phương tiện).

## Chuyển sang kế hoạch bốn camera giả lập

Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv` (kể cả tránh đếm nhiều frame liền nhau trong cùng cảnh
như nhiều ca độc lập), và vì sao kế hoạch đó chỉ giúp tìm ca cần soi, chưa đo được tỷ lệ lỗi: Kế hoạch này dùng khoảng cách thời gian hoặc thuật toán keyframe extraction để bốc mẫu phân tán ngẫu nhiên, giúp phát hiện lỗi có tính hệ thống (systematic error) thay vì đo đạc chính xác tỉ lệ lỗi toàn cục. Tỉ lệ lỗi thực tế chỉ đo được khi random sampling thuần túy trên toàn bộ tập dữ liệu chứ không chỉ nhặt cảnh nghi ngờ.
