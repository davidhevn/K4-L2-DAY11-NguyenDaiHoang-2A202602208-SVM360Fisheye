# Exit ticket

Đọc `docs/10-svm360-reading-vi.md` trước khi trả lời câu 1–2. Các câu về zone, `why`, rework, parking và sampling
đã nằm trong file tương ứng nên không hỏi lại ở đây.

1. Một vật ở vùng seam giữa hai camera thật xuất hiện với hai box khác nhau: đó là lỗi `DUPLICATE` hay cần một quy
   tắc riêng? Vì sao? 
   -> Cần một quy tắc riêng (Cross-camera Tracking). Vật thể ở vùng chồng mép (seam) bị nhìn thấy bởi 2 camera khác nhau, việc xuất hiện 2 box trên 2 hình 2D là hiển nhiên về mặt quang học. Nếu merge muộn ở Bird Eye View (BEV) thì ID phải đồng nhất, do đó không thể coi là lỗi Duplicate đơn thuần ở không gian ảnh 2D.

2. Một vật đi qua nhiều frame trên cùng camera: khi nào giữ cùng track ID, khi nào thêm keyframe hoặc trạng thái
   Outside? Nêu bằng chứng sẽ cần trước khi nối track qua hai camera.
   -> Giữ cùng Track ID khi vật di chuyển liên tục, bị che khuất một phần (occluded). Chuyển sang trạng thái Outside khi vật hoàn toàn biến mất khỏi khung hình. Bằng chứng cần trước khi nối track: Thuộc tính hình học khớp nhau khi chiếu lên BEV, vận tốc và quỹ đạo di chuyển (kalman filter) phải nhất quán trước và sau khi đổi camera.

3. Nhìn lại cả buổi: một chỗ bạn tin nhãn mình đúng nhưng reference hoặc người soát nghĩ khác (dẫn frame/`object_ref`),
   bạn đã xử lý thế nào, và nếu làm lại slice này bạn sẽ đổi gì trong cách làm?
   -> Ở ảnh `adasind_258420.jpg`, lỗi hệ thống tự động báo L5 có chiều cao < 40px (Spurious). Tuy nhiên, nếu soi kỹ, do hiệu ứng cong của fisheye, vật vẫn cung cấp đầy đủ thông tin nhận diện. Em đã note lỗi này vào Escalation Ticket báo cáo cho Guideline Owner để nới lỏng quy định chiều cao tối thiểu ở rìa. Nếu làm lại, em sẽ focus mạnh hơn vào việc đánh dấu rõ ignore_region để lọc bớt nhiễu thay vì ngồi soi kích thước từng pixel.
