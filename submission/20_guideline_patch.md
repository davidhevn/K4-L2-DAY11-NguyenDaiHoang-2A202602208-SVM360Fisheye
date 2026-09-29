# Guideline patch

- **Rule mới đề xuất:** R12 — Quy định xử lý đối tượng vùng chồng lấn (Seam Area) và đối chiếu Cross-camera: Ở các góc giao thoa giữa hai camera liền kề trong hệ SVM 360, một vật thể có thể xuất hiện đồng thời trên hai ảnh với hai góc mép khác nhau. Ở tầng gán nhãn 2D, mỗi camera phải giữ độc lập bounding box ôm sát phần nhìn thấy được (không được tự ý xóa hoặc coi là lỗi DUPLICATE); bổ sung thuộc tính `seam_object = true` khi tâm vật thể nằm trong góc chồng lấn (seam zone). Việc hợp nhất dữ liệu thành một vật thể duy nhất chỉ được thực hiện ở tầng Bird's-Eye View (BEV) hoặc 3D Fusion.
- **Áp dụng cho:** Toàn bộ 6 class đối tượng giao thông (`Car`, `Bus`, `Truck`, `ThreeWheeler`, `Bike`, `Pedestrian`), thuộc tính mới `seam_object` và các box nằm trong zone `edge` tại góc nhìn tiếp giáp giữa các camera.
- **Vì sao luật hiện tại (`docs/02-rules-vi.md`) không đủ:** Luật hiện hành `v1.0.0` được biên soạn cho bài toán camera đơn (ADASIND), chưa có quy định cho hệ thống camera vòm 360 độ (SVM). Khi thiếu quy ước này, annotator và QA dễ nhầm lẫn một vật xuất hiện ở 2 camera là lỗi trùng lặp (`DUPLICATE`) và tùy tiện xóa đi, làm suy giảm nghiêm trọng khả năng phát hiện vật thể ở điểm mù của xe.
- **`rules_version` mới:** `v1.1.0`
- **Hiệu lực từ:** Vòng `rework` và toàn bộ đợt gán nhãn mở rộng cho 4 camera SVM (Front, Rear, Left, Right).

