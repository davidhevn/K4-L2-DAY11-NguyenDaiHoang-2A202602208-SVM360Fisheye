# Bảng Zone và Phân tích Model

- Zone nào người (L) và model (M) gãy nhiều nhất, dẫn số ở bảng trên: Zone M_only (khu vực giữa) gãy nhiều nhất do model nhầm lẫn người và xe.
- Giả thuyết vì sao (méo fisheye, box lỏng, thiếu `ego_body`, ...) và giới hạn của slice ba frame: Do méo fisheye khiến hình ảnh xe cộ ở rìa bị biến dạng quá mức, model chưa được train đủ trên dữ liệu méo này.
