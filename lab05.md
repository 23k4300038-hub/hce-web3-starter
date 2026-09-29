# BÁO CÁO LAB 5: VIẾT ĐẶC TẢ CHO CÔNG CỤ PHÂN TÍCH DÒNG TIỀN VÍ ETHEREUM

## 1. Tổng quan bài thực hành
Bài lab này đóng vai trò Chuyên viên phân tích nghiệp vụ (BA) để lập bản đặc tả yêu cầu chi tiết (`SPEC.md`) cho công cụ phân tích dòng tiền vào/ra của một ví Ethereum trong 90 ngày gần nhất.

## 2. Liên kết tài liệu
- Bản đặc tả đầy đủ được lưu trữ tại tệp: [SPEC.md](./SPEC.md)

## 3. Tóm tắt các quy tắc nghiệp vụ chính (Business Rules)
- **R1 & R2:** Nhận diện dòng tiền vào (ví nhận trùng địa chỉ) và dòng tiền ra (ví gửi trùng địa chỉ).
- **R3 & R4:** Tính phí gas (`gasUsed * gasPrice`) vào dòng tiền ra, bao gồm cả các giao dịch thất bại (`isError == 1`).
- **R5:** Quy đổi toàn bộ giá trị từ đơn vị `wei` sang `ETH` (chia cho 10^18) trước khi hiển thị.
- **R6:** Sắp xếp chuỗi giao dịch theo mốc thời gian tăng dần.

## 4. Đánh giá hoàn thành
- Đã hoàn thành viết tệp `SPEC.md` chuẩn bị làm đầu vào cho bài thực hành sinh mã Python bằng AI tại Lab 6.
