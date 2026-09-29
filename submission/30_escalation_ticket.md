# Escalation ticket

## Ticket 1

- **Frame:** adasind_258420.jpg
- **Ảnh chụp:** (Không đính kèm, sử dụng mô tả lỗi H<40)
- **Expected impact:** Việc yêu cầu vẽ các box quá nhỏ (<40px) ở mép rìa ảnh fisheye làm mất thời gian gán nhãn mà AI model không học được vì đặc thù mờ nhòe.
- **Owner:** `guideline`
- **Recommendation:** Bổ sung rule bỏ qua (ignore) các vật thể có kích thước <40px bị méo dạng ở sát rìa fisheye để tối ưu thời gian label.
