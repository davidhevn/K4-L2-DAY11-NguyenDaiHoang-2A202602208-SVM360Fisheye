# Zone table (slice của bạn)

Lệnh `python3 lab11.py model` tự ghi bảng số (cùng cách đếm với `r1_craft/compare.md` và `model_compare.md`); chạy lại lệnh sẽ cập nhật bảng và giữ nguyên phần nhận xét. Bạn chỉ viết mục Nhận xét.

| Zone | n_ref | L missing | L spurious | M missing (`LR_noM` + `R_only`) | M thừa (`LM_noR` + `M_only`) | Lỗi L chính (`what`) |
|---|---:|---:|---:|---:|---:|---|
| center | 6 | 0 | 0 | 4 | 5 | — |
| mid | 7 | 2 | 1 | 3 | 10 | BOX_GEOMETRY (1) |
| edge | 7 | 1 | 0 | 1 | 1 | MISSING (1) |

## Nhận xét

- Zone nào người (L) và model (M) gãy nhiều nhất, dẫn số ở bảng trên: Zone `mid` gãy nhiều nhất. Theo bảng trên, Người (L) mắc lỗi cao nhất ở mid với 2 missing và 1 spurious. Model (M) cũng thảm họa nhất ở mid với 3 missing và 10 thừa (spurious). Kế tiếp là zone `center` model cũng có 4 missing và 5 thừa.
- Giả thuyết vì sao (méo fisheye, box lỏng, thiếu `ego_body`, ...) và giới hạn của slice ba frame: Do hiệu ứng méo cực đại của thấu kính fisheye khi tỏa ra từ tâm (center) ra rìa (mid/edge), cộng với các box lỏng (box_geometry) khiến cả người và model bị bối rối về kích thước thật. Mặt khác, model gặp nhiều False Positive (M thừa) do có khả năng bị nhiễu bởi các chi tiết thân xe nếu thiếu che chắn bằng `ego_body` ignore_region. Dù vậy, slice 3 frame quá nhỏ bé nên các số liệu này chưa mang tính đại diện thống kê tuyệt đối.
