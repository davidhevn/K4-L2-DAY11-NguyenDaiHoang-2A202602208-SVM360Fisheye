# Đối chiếu chất lượng cục bộ — rectangle

Teaching reference, không phải gold set đã phê duyệt; không có điểm đạt tự động.
Nguồn: export r1_craft đã khóa SHA256 `ef721fb5efc1dce105a888f844c5c18dcf110e304f9411b5f4c7084c0c17e2ab`; slice `B3-dense`.
Ghép hình học greedy một-một theo IoU ≥ 0.50, rồi so class; H ≥ 40 px.
Box trái nằm chủ yếu trong ignore_region reference không tính. Polygon, polyline, track không được chấm.
Đây là phép tính offline của lab, không phải báo cáo hay kết quả tương đương CVAT Premium.

Frame được tính: adasind_145860.jpg, adasind_167700.jpg, adasind_199770.jpg. Frame thiếu trong export: không.
TP=16; FP=3; FN=4; số lần đối chiếu=22; mean IoU của TP=0.721.

| Chỉ số | Micro | Macro | Nhãn thấp nhất |
|---|---:|---:|---:|
| accuracy | 0.727 | 0.936 | 0.864 |
| precision | 0.842 | 0.880 | 0.600 |
| recall | 0.800 | 0.767 | 0.500 |
| jaccard | 0.696 | 0.677 | 0.500 |
| dice | 0.821 | 0.798 | 0.667 |

| Nhãn | TP | FP | FN | Accuracy | Precision | Recall | Jaccard | Dice |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bike | 5 | 0 | 1 | 0.955 | 1.000 | 0.833 | 0.833 | 0.909 |
| Car | 1 | 0 | 1 | 0.955 | 1.000 | 0.500 | 0.500 | 0.667 |
| Pedestrian | 3 | 0 | 1 | 0.955 | 1.000 | 0.750 | 0.750 | 0.857 |
| ThreeWheeler | 3 | 2 | 1 | 0.864 | 0.600 | 0.750 | 0.500 | 0.667 |
| Truck | 4 | 1 | 0 | 0.955 | 0.800 | 1.000 | 0.800 | 0.889 |

| Frame | TP | FP | FN | Accuracy | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| adasind_145860.jpg | 2 | 0 | 0 | 1.000 | 1.000 | 1.000 |
| adasind_167700.jpg | 8 | 2 | 1 | 0.800 | 0.800 | 0.889 |
| adasind_199770.jpg | 6 | 1 | 3 | 0.600 | 0.857 | 0.667 |

Confusion matrix: hàng = teaching reference; cột = export đã khóa.
`<missing>` là thiếu box; `<extra>` là box thừa. Xem `local_quality_confusion.csv`.

| Reference \ Export | Bike | Car | Pedestrian | ThreeWheeler | Truck | <missing> |
|---|---:|---:|---:|---:|---:|---:|
| Bike | 5 | 0 | 0 | 0 | 0 | 1 |
| Car | 0 | 1 | 0 | 0 | 1 | 0 |
| Pedestrian | 0 | 0 | 3 | 0 | 0 | 1 |
| ThreeWheeler | 0 | 0 | 0 | 3 | 0 | 1 |
| Truck | 0 | 0 | 0 | 0 | 4 | 0 |
| <extra> | 0 | 0 | 0 | 2 | 0 | 0 |

Chi tiết xung đột trong `local_quality_conflicts.csv`; dữ liệu máy đọc trong `local_quality.json`.
Mismatching label đóng góp một FP cho class vẽ và một FN cho class reference; attribute khác được báo riêng.
Micro accuracy đếm mỗi cặp ghép sai class là một lần đối chiếu; Jaccard đếm cả FP và FN.
Macro/worst bỏ nhãn không xuất hiện ở cả hai phía; chỉ số không có mẫu là N/A.
