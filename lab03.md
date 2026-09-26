# BÁO CÁO LAB 3: TÌM HIỂU ETHERSCAN VÀ ĐIỀU TRA ON-CHAIN

## 1. Phân tích giao dịch cá nhân trên Sepolia Etherscan

Dựa trên giao dịch chuyển 0.01 Sepolia ETH ở Lab 2 với Mã giao dịch (TxHash):
`0xb3abd9f53dfc50351d7531394de273db9037d0fed364ec13b662b788d96756f1`

* **Mã băm giao dịch (TxHash):** `0xb3abd9f53dfc50351d7531394de273db9037d0fed364ec13b662b788d96756f1`
* **Địa chỉ gửi (From):** `0xfb6db4c6a6f1165d490c0cd055b8e99997ad7e07`
* **Địa chỉ nhận (To):** `0xf82424b9148d88e09e05a8f4c2c5fa23d1d96350`
* **Giá trị giao dịch (Value):** `0.01 ETH`
* **Trạng thái giao dịch:** `Success` (Thành công)
* **Số hiệu khối (Block Number):** Tìm thấy trên Etherscan
* **Ý nghĩa các trường dữ liệu bổ sung:**
  * **Gas Limit:** Lượng Gas tối đa mà người gửi cho phép sử dụng cho giao dịch này.
  * **Gas Used by Transaction:** Lượng Gas thực tế đã tiêu tốn để xử lý giao dịch.
  * **Base Fee / Max Priority Fee:** Mức phí cơ bản bị đốt bỏ và phí ưu tiên trả cho thợ đào/validator để giao dịch được xử lý nhanh hơn.

---

## 2. Tìm hiểu Smart Contract trên Ethereum Mainnet

Phân tích một hợp đồng thông minh phổ biến (Ví dụ: Uniswap V2 Router / Tether USD):

* **Địa chỉ Hợp đồng (Contract Address):** `0xdAC17F958D2ee523a2206206994597C13D831ec7` (Tether USD - USDT)
* **Mã nguồn đã được xác minh (Verified Source Code):**
  * Hợp đồng đã có dấu tích xanh **Contract Source Code Verified**, cho phép cộng đồng kiểm tra trực tiếp logic mã nguồn công khai.
* **Quyền chủ sở hữu (Owner/Admin privileges):**
  * Hợp đồng có chứa các hàm quản trị đặc quyền như `issue` (in thêm token), `redeem` (thu hồi token), hoặc `addBlackList` (khóa tài khoản).
  * **Đánh giá rủi ro:** Nếu khóa quản trị (Private Key của Owner) bị lộ hoặc người tạo hợp đồng có ý định xấu, họ có thể lạm quyền để đóng đóng băng tài sản người dùng hoặc thao túng nguồn cung token.

---

## 3. Câu hỏi lý thuyết & Suy ngẫm

**Câu hỏi:** Tại sao tính công khai của Etherscan vừa là ưu điểm vừa là thách thức đối với quyền riêng tư của người dùng?

**Trả lời:**
* **Ưu điểm (Tính minh bạch & Đáng tin cậy):** Mọi giao dịch, số dư ví và mã nguồn hợp đồng đều công khai. Điều này giúp ngăn chặn gian lận, cho phép bất kỳ ai cũng có thể tự kiểm tra (audit) dữ liệu mà không cần thông qua bên thứ ba trung gian.
* **Thách thức (Quyền riêng tư):** Mặc dù địa chỉ ví có tính ẩn danh (pseudonymous), nhưng một khi địa chỉ ví bị liên kết với danh tính đời thực (thông qua sàn giao dịch KYC, định danh ENS hoặc đăng tải công khai), toàn bộ lịch sử tài chính, biến động tài sản và thói quen giao dịch của người dùng sẽ bị theo dõi hoàn toàn trên Etherscan.
