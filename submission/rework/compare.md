# So sánh L với R

Chỉ số L/R là thứ tự box cao ≥ H=40 trong từng frame, theo thứ tự XML; bắt đầu từ 1.
Box L trong ignore_region được báo IGNORE_SCOPE, không tính SPURIOUS.

## adasind_062370.jpg
- R7 center MISSING
- R8 center MISSING
## adasind_086220.jpg
- L3+R1 mid ATTRIBUTE
- L4 center SPURIOUS
- L5 center SPURIOUS
- R4 center MISSING
## adasind_117120.jpg
- L4 center SPURIOUS
- L8 center SPURIOUS
- L9 center SPURIOUS

## Theo zone
| zone | n_ref | matched | missing | spurious |
|---|---|---|---|---|
| center | 13 | 10 | 3 | 5 |
| mid | 6 | 6 | 0 | 0 |
| edge | 1 | 1 | 0 | 0 |
