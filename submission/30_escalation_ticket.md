# Escalation ticket

## Ticket 1

- **Frame:** adasind_167700.jpg
- **Ảnh chụp:** submission/screenshots/evidence_1.png
- **Expected impact:** Phần cánh tay áo kẻ caro và tay lái xe ego lọt vào khung hình góc rộng ở cự ly siêu gần. Nếu không được bọc polygon loại trừ thống nhất, mô hình AI nhận diện nhầm thành Pedestrian (người đi bộ áp sát phương tiện), gây ra cảnh báo va chạm ảo và phanh khẩn cấp không mong muốn (Phantom Braking) khi vận hành xe tự hành; đồng thời làm sai lệch toàn bộ chỉ số đánh giá chất lượng dữ liệu.
- **Owner:** guideline
- **Recommendation:** Cập nhật tài liệu hướng dẫn gán nhãn quy định bắt buộc: Mọi frame nhìn thấy bất kỳ bộ phận nào của xe ego hoặc người lái (tay, chân, áo, gương) đều phải vẽ polygon `ignore_region` với `reason: ego_body`; tích hợp bộ lọc tự động kiểm tra sự tồn tại của polygon ego_body trước khi cho phép xuất dữ liệu huấn luyện.

