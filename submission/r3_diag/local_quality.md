# Đối chiếu chất lượng cục bộ — rectangle

Teaching reference, không phải gold set đã phê duyệt; không có điểm đạt tự động.
Nguồn: export r1_craft đã khóa SHA256 `de1e69f1080ab31479194cb82b0655bb91ee5022d804f64259da8c13e28384d0`; slice `B4-dense`.
Ghép hình học greedy một-một theo IoU ≥ 0.50, rồi so class; H ≥ 40 px.
Box trái nằm chủ yếu trong ignore_region reference không tính. Polygon, polyline, track không được chấm.
Đây là phép tính offline của lab, không phải báo cáo hay kết quả tương đương CVAT Premium.

Frame được tính: adasind_258420.jpg, adasind_270517.jpg, adasind_310008.jpg. Frame thiếu trong export: không.
TP=17; FP=1; FN=3; số lần đối chiếu=21; mean IoU của TP=0.816.

| Chỉ số | Micro | Macro | Nhãn thấp nhất |
|---|---:|---:|---:|
| accuracy | 0.810 | 0.952 | 0.905 |
| precision | 0.944 | 0.917 | 0.667 |
| recall | 0.850 | 0.792 | 0.500 |
| jaccard | 0.810 | 0.750 | 0.500 |
| dice | 0.895 | 0.833 | 0.667 |

| Nhãn | TP | FP | FN | Accuracy | Precision | Recall | Jaccard | Dice |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bike | 2 | 0 | 2 | 0.905 | 1.000 | 0.500 | 0.500 | 0.667 |
| Car | 2 | 1 | 1 | 0.905 | 0.667 | 0.667 | 0.500 | 0.667 |
| Pedestrian | 7 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| ThreeWheeler | 6 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

| Frame | TP | FP | FN | Accuracy | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| adasind_258420.jpg | 6 | 1 | 2 | 0.667 | 0.857 | 0.750 |
| adasind_270517.jpg | 6 | 0 | 1 | 0.857 | 1.000 | 0.857 |
| adasind_310008.jpg | 5 | 0 | 0 | 1.000 | 1.000 | 1.000 |

Confusion matrix: hàng = teaching reference; cột = export đã khóa.
`<missing>` là thiếu box; `<extra>` là box thừa. Xem `local_quality_confusion.csv`.

| Reference \ Export | Bike | Car | Pedestrian | ThreeWheeler | <missing> |
|---|---:|---:|---:|---:|---:|
| Bike | 2 | 0 | 0 | 0 | 2 |
| Car | 0 | 2 | 0 | 0 | 1 |
| Pedestrian | 0 | 0 | 7 | 0 | 0 |
| ThreeWheeler | 0 | 0 | 0 | 6 | 0 |
| <extra> | 0 | 1 | 0 | 0 | 0 |

Chi tiết xung đột trong `local_quality_conflicts.csv`; dữ liệu máy đọc trong `local_quality.json`.
Mismatching label đóng góp một FP cho class vẽ và một FN cho class reference; attribute khác được báo riêng.
Micro accuracy đếm mỗi cặp ghép sai class là một lần đối chiếu; Jaccard đếm cả FP và FN.
Macro/worst bỏ nhãn không xuất hiện ở cả hai phía; chỉ số không có mẫu là N/A.
