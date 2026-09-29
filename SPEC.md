# SPEC — BẢN ĐẶC TẢ CÔNG CỤ PHÂN TÍCH DÒNG TIỀN VÍ ETHEREUM (LAB 5)

## 1. Mục đích
Xây dựng công cụ nhận vào một địa chỉ ví Ethereum và xuất báo cáo phân tích dòng tiền vào/ra trong 90 ngày gần nhất kèm thống kê số dư.

## 2. Đầu vào
- Một địa chỉ ví Ethereum (chuỗi 42 ký tự bắt đầu bằng `0x`).
- Khóa API của Etherscan (đọc từ biến môi trường `ETHERSCAN_API_KEY`).
- Số ngày cần phân tích (mặc định 90 ngày).

## 3. Quy tắc nghiệp vụ
- **R1 (Dòng tiền vào):** Giao dịch có trường `to` trùng với địa chỉ ví đang xét được tính là dòng tiền vào.
- **R2 (Dòng tiền ra):** Giao dịch có trường `from` trùng với địa chỉ ví đang xét được tính là dòng tiền ra.
- **R3 (Tính phí giao dịch đi ra):** Với giao dịch đi ra, số tiền thực trừ khỏi ví = Giá trị chuyển + Phí giao dịch (`gasUsed * gasPrice`).
- **R4 (Xử lý giao dịch thất bại):** Giao dịch có trạng thái thất bại (`isError == 1`) vẫn bị trừ phí gas, phải tính phí gas đó vào dòng tiền ra.
- **R5 (Đổi đơn vị):** Mọi số tiền lấy về từ API ở đơn vị `wei` phải chia cho 10^18 để đổi sang `ETH` trước khi hiển thị.
- **R6 (Sắp xếp):** Sắp xếp danh sách giao dịch theo thời gian tăng dần.

## 4. Đầu ra
- Bảng dữ liệu chi tiết gồm: Thời gian, Loại giao dịch (Vào/Ra), Số tiền (ETH), Phí gas (ETH), Số dư lũy kế.
- Ba con số tổng hợp: Tổng dòng tiền vào, Tổng dòng tiền ra, Số dư ròng cuối kỳ.

## 5. Trường hợp ngoại lệ
- Nếu API trả về danh sách rỗng: In thông báo "Ví không có giao dịch trong kỳ", không báo lỗi.
- Nếu API trả về mã lỗi (khóa API sai/hết hạn): In thông báo lỗi và dừng chương trình.
- Nếu ví có hơn 10.000 giao dịch: Phải xử lý phân trang (pagination) để lấy đủ dữ liệu.

## 6. Ngoài phạm vi
- Không phân tích các giao dịch Token (ERC-20, ERC-721), chỉ phân tích ETH gốc.
- Không quy đổi giá trị sang VND/USD.
