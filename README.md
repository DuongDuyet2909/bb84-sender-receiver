# Mô phỏng bên gửi–bên nhận BB84 — Sender–Receiver

Mô phỏng bước chuẩn bị và đo qubit BB84 bằng Python.

## Chạy chương trình

Cần Python 3; không cần cài thư viện ngoài.

```bash
python bb84_sender_receiver.py
```

Chương trình minh họa 16 tín hiệu: Alice chọn bit và cơ sở Z/X, Bob chọn cơ sở đo. Khi trùng cơ sở, Bob thu đúng bit; khi khác cơ sở, kết quả ngẫu nhiên. Cột `Match` cho biết cơ sở có trùng nhau hay không. Kết quả thay đổi giữa các lần chạy.

## Phạm vi

Đây là mô phỏng xác suất trên máy tính cổ điển, chưa triển khai sàng lọc khóa, ước lượng QBER, sửa lỗi hay khuếch đại tính riêng tư. Không dùng chương trình để tạo khóa mật mã thực tế.

## Thuật ngữ và cách đọc đầu ra

| Thuật ngữ | Ý nghĩa |
| --- | --- |
| Sender / receiver | Bên gửi Alice / bên nhận Bob |
| Bit / qubit | Bit cổ điển / bit lượng tử |
| Basis Z / X | Hai cơ sở chuẩn bị và đo của BB84 |
| `Match` | Cơ sở của Alice và Bob có trùng nhau hay không |
| Sifting | Sàng lọc, giữ các vị trí trùng cơ sở; bản này chưa thực hiện |
| QBER — Quantum Bit Error Rate | Tỷ lệ bit sai sau sàng lọc; bản này chưa ước lượng |
| Privacy amplification | Khuếch đại tính riêng tư; bước rút ngắn khóa để giảm thông tin của bên nghe lén |

Tên cột trong chương trình giữ nguyên để dễ đối chiếu mã. `Match` nói về **cơ sở**, không chứng nhận khóa bí mật hoặc an toàn.
