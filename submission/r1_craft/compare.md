# So sánh L với R

Chỉ số L/R là thứ tự box cao ≥ H=40 trong từng frame, theo thứ tự XML; bắt đầu từ 1.
Box L trong ignore_region được báo IGNORE_SCOPE, không tính SPURIOUS.

## adasind_145860.jpg
## adasind_167700.jpg
- L5 mid IGNORE_SCOPE
- L6+R4 center WRONG_CLASS
- L11 mid SPURIOUS
## adasind_199770.jpg
- L1 mid IGNORE_SCOPE
- L5 center SPURIOUS
- R3 mid MISSING
- R4 mid MISSING
- R6 edge MISSING

## Theo zone
| zone | n_ref | matched | missing | spurious |
|---|---|---|---|---|
| center | 9 | 8 | 1 | 2 |
| mid | 7 | 5 | 2 | 1 |
| edge | 4 | 3 | 1 | 0 |
