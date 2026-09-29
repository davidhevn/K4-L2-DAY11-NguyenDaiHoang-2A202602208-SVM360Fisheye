# Sensor context

- Rig: Camera fisheye đơn gắn phía trước phương tiện (xe hai bánh / xe máy của tập dữ liệu ADASIND) di chuyển trong điều kiện giao thông hỗn hợp tại Ấn Độ; camera hướng về phía trước ghi nhận bối cảnh phía trước xe ego, không có thông số calibration rig chi tiết hay hệ thống 4 camera quanh xe.
- `ego_body`: Xuất hiện ở góc dưới bên trái của khung hình (thường thấy tay, chân, áo của người lái xe ego hoặc phần gương/tay lái). Ngoại lệ có 2 frame không nhìn thấy thân xe ego là `adasind_006840.jpg` và `adasind_271039.jpg`.
- Vòng kính (lens circle): Nằm ở khu vực trung tâm khung hình dọc (kích thước 1080×1920 px, tâm cx ≈ 450–610 px, cy ≈ 890–970 px, bán kính r ≈ 770–830 px), bao phủ toàn bộ chiều ngang khung hình và chiếm khoảng 70–75% tổng diện tích ảnh; hai phần ngoài vòng kính ở phía trên đỉnh và dưới đáy bị che bởi vành đen quang học (`lens_border`).

