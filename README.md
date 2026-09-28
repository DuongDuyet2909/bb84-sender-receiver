# BB84 Sender–Receiver

Mô phỏng bước chuẩn bị và đo qubit BB84 bằng Python.

## Chạy chương trình

Cần Python 3; không cần cài thư viện ngoài.

```bash
python bb84_sender_receiver.py
```

Chương trình minh họa 16 tín hiệu: Alice chọn bit và cơ sở Z/X, Bob chọn cơ sở đo. Khi trùng cơ sở, Bob thu đúng bit; khi khác cơ sở, kết quả ngẫu nhiên. Cột `Match` cho biết cơ sở có trùng nhau hay không. Kết quả thay đổi giữa các lần chạy.

## Phạm vi

Đây là mô phỏng xác suất trên máy tính cổ điển, chưa triển khai sàng lọc khóa, ước lượng QBER, sửa lỗi hay khuếch đại tính riêng tư. Không dùng chương trình để tạo khóa mật mã thực tế.
