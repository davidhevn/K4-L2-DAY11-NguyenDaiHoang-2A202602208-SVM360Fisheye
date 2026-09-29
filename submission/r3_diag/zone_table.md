# Zone table (slice của bạn)

Lệnh `python3 lab11.py model` tự ghi bảng số (cùng cách đếm với `r1_craft/compare.md` và `model_compare.md`); chạy lại lệnh sẽ cập nhật bảng và giữ nguyên phần nhận xét. Bạn chỉ viết mục Nhận xét.

| Zone | n_ref | L missing | L spurious | M missing (`LR_noM` + `R_only`) | M thừa (`LM_noR` + `M_only`) | Lỗi L chính (`what`) |
|---|---:|---:|---:|---:|---:|---|
| center | 9 | 1 | 2 | 2 | 3 | WRONG_CLASS (1) |
| mid | 7 | 2 | 1 | 3 | 4 | MISSING (2) |
| edge | 4 | 1 | 0 | 4 | 3 | MISSING (1) |

## Nhận xét

- Zone nào người (L) và model (M) gãy nhiều nhất, dẫn số ở bảng trên:
  - Đối với Model (M): Gãy nặng nề nhất ở **zone edge** và **zone mid**. Ở zone edge, Model bỏ sót toàn bộ 4/4 vật thể (tỷ lệ missing 100%) và sinh thêm 3 box thừa (M thừa = 3); ở zone mid, Model tiếp tục bỏ sót 3/7 vật thể và tạo 4 box thừa. Ngay cả ở center, Model cũng bỏ sót 2 và thừa 3 box.
  - Đối với Người (L): Duy trì độ chính xác cao hơn rõ rệt (khớp 16/20 vật thể), nhưng gặp lỗi nhiều nhất ở **zone mid** (2 missing, 1 spurious) và **zone center** (1 lỗi chính WRONG_CLASS do nhầm lẫn giữa Truck và ThreeWheeler, cùng 2 box spurious do vẽ thừa).
- Giả thuyết vì sao (méo fisheye, box lỏng, thiếu `ego_body`, ...) và giới hạn của slice ba frame:
  - Model gãy do lệch miền dữ liệu (Domain Shift): Model YOLO được huấn luyện trên ảnh phẳng thông thường, không thích ứng được với độ méo cong cực đại ở rìa kính fisheye (zone mid và edge); đồng thời taxonomy của model không có nhãn ThreeWheeler dẫn đến phân loại sai.
  - Người gán nhãn gặp khó khăn do mật độ phương tiện đông đúc dẫn đến che khuất phức tạp (occluded), một số box bọc chưa thật sát biên thực tế làm suy giảm chỉ số IoU, và ban đầu thiếu polygon `ego_body` ở góc dưới trái.
  - Giới hạn của slice 3 frame: Tập mẫu 3 frame quá nhỏ để phản ánh toàn bộ phân phối dữ liệu thế giới thực; chỉ thể hiện lát cắt giao thông ban ngày mật độ cao, chưa thể kiểm chứng tính ổn định khi chuyển góc quay hoặc kết hợp dữ liệu từ 4 camera quanh xe.

