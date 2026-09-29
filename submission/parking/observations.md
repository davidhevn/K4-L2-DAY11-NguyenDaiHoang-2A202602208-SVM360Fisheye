# Quan sát vạch ô đỗ

- Hai vạch `parking_line` đã vẽ (mô tả vị trí trong ảnh): Vạch 1 ở tiền cảnh khu vực giữa (chạy chéo từ khoảng x=405, y=655 xuống x=513, y=715) phân chia hai ô đỗ xe phía trước; Vạch 2 ở tiền cảnh bên phải (chạy chéo từ x=725, y=630 sang x=958, y=685) phân chia ô đỗ liền kề bên phải.
- Một vạch/dấu sơn hoặc biên **không** vẽ, và vì sao: Dải mép lề đường (curb/ranh giới bãi đỗ) và các vạch mờ chỉ dẫn hướng đi ở phía hậu cảnh xa: không vẽ vì chúng đóng vai trò biên giới hạn lối lưu thông bãi đỗ chứ không phải đoạn sơn tạo ranh giới chia một ô đỗ xe riêng biệt.
- Polygon `free_space` dừng ở đâu; có phần bị che nào không: Polygon bao phủ dải mặt đường asphalt thông thoáng của lối xe chạy nằm giữa hàng ô đỗ tiền cảnh (y ≈ 630–650) và hàng ô đỗ phía sau (y ≈ 565); polygon dừng lại trước mép các vạch đỗ, không chạm vào thân chiếc xe đỏ đỗ ở xa và không có vật cản nào che khuất trong vùng này.
- Ca chưa chắc cần hỏi người soát (nếu không có, ghi “không có”): Các đoạn vạch sơn mờ ở hàng ô đỗ xa (gần vị trí xe đỏ): độ tương phản thấp do khoảng cách chụp xa và sơn bị mòn, cần thống nhất quy tắc có gán nhãn các vạch quá xa/mờ hay chỉ giới hạn ở khu vực nhìn rõ ràng.

