# Đề xuất gold set theo camera — tình huống giả lập

**Đầu bài:** 50.000 frame từ bốn camera SVM, ngân sách chọn 200 frame để review/gold. Đây là tình huống trên slide,
**không phải** 50.000 frame có trong repo. Phân bổ đúng 200 ở `45_sampling_plan.csv` cho bốn camera, mỗi camera có
normal và hard slice. “Gold set” ở đây là **kế hoạch tạo** reference sau kiểm chứng, không phải teaching reference
ADASIND hoặc nhãn bạn vừa vẽ. Nếu cần, dùng `notebooks/day11-svm360-colab.ipynb` để thử tổng phân bổ; notebook
không làm thay phần lý do.

| camera_id | Hard case cần chọn | Vì sao dễ sai | Annotation space / calibration cần giữ | Cách review trước khi gọi là gold |
|---|---|---|---|---|
| front | Ngược nắng chói lóa, xe phanh gấp sát đầu | Độ tương phản gắt làm mất chi tiết viền vật thể, méo ở rìa do xe ở quá gần. | Giữ nguyên gốc tọa độ và distortion parameters. | Chấm chéo bởi Senior Annotator, đối chiếu chéo (cross-check) với Lidar nếu có. |
| rear | Đèn pha chiếu thẳng góc ban đêm | Cảm biến camera bị lóa sáng (lens flare), nhầm lẫn ánh sáng với kích thước xe thật. | Lens border mask đặc biệt quan trọng để tránh nhiễu do bụi mờ kính. | So sánh chuỗi frame trước/sau (temporal context) để đoán nội suy. |
| left | Xe máy cắt ngang góc hẹp, người đi bộ chen ngang | Vật thể đi vào vùng seam giữa camera trái và trước/sau, gây biến dạng mạnh. | Cross-camera overlap (Vùng chồng mép). | Review theo luồng BEV (Bird Eye View) để nối track chính xác. |
| right | Chướng ngại vật tĩnh sát lề, xe đạp lấn tuyến | Tương tự left nhưng thường bị khuất tầm nhìn do kích thước xe ego (ego_body). | Góc ego_body che khuất lớn. | Kiểm tra kỹ ignore_region của thân xe tránh đánh dấu nhầm. |

- Khi nào cần refresh gold set (đổi camera, calibration hoặc rule): Khi có bản cập nhật mới về Rules (ví dụ nâng hạ ngưỡng H), thay đổi góc lắp đặt (rigging) của camera, hoặc khi model mới train ra báo cáo lỗi hệ thống quá sai khác so với lỗi người làm.
- Một ca seam/cross-camera cần policy và evidence trước khi ghép hai box: Cần chính sách đồng nhất Track_ID trên không gian 3D/BEV; bằng chứng (evidence) là vector chuyển động (motion) của vật thể khớp nhau ở cả hai camera trước khi sang vùng khuất.
- Vì sao peer agreement hoặc quality report trên ảnh một camera chưa chứng minh gold set đúng cho cả bốn camera: Vì ảnh đơn 2D không phản ánh đúng hình học không gian (Calibration) khi chiếu xuống mặt đường (BEV); 2 người có thể đồng thuận sai trên ảnh 2D ở vùng seam do méo fisheye, dẫn đến ghép 4 hình lại thì vỡ trận.
