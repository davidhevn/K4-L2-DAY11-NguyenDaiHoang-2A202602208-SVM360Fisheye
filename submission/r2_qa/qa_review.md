# QA review · B2-center

Mã khóa: 07D9-DDBA

| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_062370.jpg | L1 | R05 | Box Bike chạm mép phải khung ảnh (xbr=1080.0) nhưng chưa bật thuộc tính `truncated=true`. |
| adasind_062370.jpg | L3 | R05 | Box ThreeWheeler chạm mép trái khung ảnh (xtl=0.0) bị cắt ngang nhưng chưa bật `truncated=true`. |
| adasind_086220.jpg | L1 | R01 | Box Bike có chiều cao đo được H = 39.08 px < 40 px, vi phạm ngưỡng chiều cao tối thiểu bắt buộc của bài. |
| adasind_117120.jpg | L4 | R01 | Box Car nhỏ ở hậu cảnh có chiều cao H = 21.6 px < 40 px, không thuộc phạm vi cần gán nhãn. |

Ghi finding r2_qa: cell=L_only, rule_id có giá trị, why để trống.
