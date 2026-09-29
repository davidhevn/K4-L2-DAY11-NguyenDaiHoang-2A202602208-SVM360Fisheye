# Error Card: R10 Lỗi tách người xe

- Tên file/Frame: adasind_258420.jpg
- Object Ref (nếu có): L4
- Bạn đang làm bước nào: r2_qa
- Ai là người bị bắt lỗi: annotator
- Ngữ cảnh (kể tóm tắt vật thể đang làm gì, ở đâu): Người đi bộ và xe đạp đang di chuyển sát nhau trên đường.
- Cảm giác của bạn (dễ nhìn, khó nhìn, bị che...): Bị che lấp một phần nên dễ gây nhầm lẫn là 2 vật thể tách biệt.
- Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy: E1_annotator_error (Người gán nhãn quên luật gộp chung người và xe).
- Cách sửa và ai nhận việc (`owner`): Xóa box Pedestrian và gộp chung vào box Bike. (owner: annotator).
- Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule): R10, file ảnh qa_overlay.
