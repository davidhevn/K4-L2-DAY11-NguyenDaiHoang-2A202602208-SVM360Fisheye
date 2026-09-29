# Quan sát vạch ô đỗ

- Hai vạch `parking_line` đã vẽ (mô tả vị trí trong ảnh): Đã vẽ các vạch sơn chéo màu vàng có chức năng phân chia giữa các ô đỗ xe riêng biệt, nằm ở khu vực tiền cảnh.
- Một vạch/dấu sơn hoặc biên **không** vẽ, và vì sao: Không vẽ vạch kẻ thẳng dài ở ngoài cùng vì đó là vạch giới hạn đường chạy, không phải vạch phân ô đỗ xe.
- Polygon `free_space` dừng ở đâu; có phần bị che nào không: Dừng ở mép bánh xe của các xe đang đỗ và viền vỉa hè; không vẽ đè lên bóng râm hay xe cộ.
