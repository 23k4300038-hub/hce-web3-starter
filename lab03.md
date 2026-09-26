# BÁO CÁO LAB 3: TÌM HIỂU ETHERSCAN VÀ ĐIỀU TRA ON-CHAIN

## 1. Phân tích giao dịch cá nhân trên Sepolia Etherscan

Dựa trên giao dịch chuyển 0.01 Sepolia ETH ở Lab 2 với Mã giao dịch (TxHash):
`0xb3abd9f53dfc50351d7531394de273db9037d0fed364ec13b662b788d96756f1`

* **Mã băm giao dịch (TxHash):** `0xb3abd9f53dfc50351d7531394de273db9037d0fed364ec13b662b788d96756f1`
* **Trạng thái giao dịch (Status):** `Success` (Thành công)
* **Địa chỉ gửi (From):** `0xfb6db4c6a6f1165d490c0cd055b8e99997ad7e07`
* **Địa chỉ nhận (To):** `0xf82424b9148d88e09e05a8f4c2c5fa23d1d96350`
* **Giá trị giao dịch (Value):** `0.01 ETH`
* **Phí giao dịch (Transaction Fee):** Chi phí Gas thực tế trả cho validator xử lý giao dịch.
* **Chi tiết thông số Gas:**
  * **Gas Limit:** `21,000` (Mức Gas tiêu chuẩn tối đa cho lệnh chuyển ETH đơn giản).
  * **Gas Used by Transaction:** `21,000` (100% lượng Gas ấn định đã được sử dụng).
  * **Gas Price:** Mức giá Gas tính theo Gwei tại thời điểm giao dịch được xác nhận.
  * **Base Fee & Priority Fee:** Mức phí cơ bản bị đốt bỏ (burned) và phí ưu tiên thưởng cho validator.

---

## 2. Tìm hiểu Smart Contract trên Ethereum Mainnet

Phân tích hợp đồng thông minh phổ biến: **Tether USD (USDT)**

* **Địa chỉ Hợp đồng (Contract Address):** `0xdAC17F958D2ee523a2206206994597C13D831ec7`
* **Mã nguồn đã được xác minh (Verified Source Code):**
  * Hợp đồng có dấu tích xanh **Contract Source Code Verified** trên Etherscan, đảm bảo tính công khai và minh bạch mã nguồn đối với cộng đồng.
* **Quyền chủ sở hữu (Owner/Admin privileges):**
  * Hợp đồng chứa các hàm quản trị đặc quyền như `issue` (in thêm token), `redeem` (thu hồi token), và `addBlackList` (khóa tài khoản/đóng băng tài sản).
  * **Đánh giá rủi ro:** Nếu khóa riêng tư (Private Key) của Owner bị lộ hoặc quản trị viên lạm quyền, họ có thể đóng băng tài sản của người dùng hoặc thao túng tổng nguồn cung token.

---

## 3. Câu hỏi lý thuyết & Suy ngẫm

**Câu hỏi:** Tại sao tính công khai của Etherscan vừa là ưu điểm vừa là thách thức đối với quyền riêng tư của người dùng?

**Trả lời:**
* **Ưu điểm (Tính minh bạch & Đáng tin cậy):** Mọi giao dịch, số dư ví và mã nguồn hợp đồng đều công khai. Điều này giúp ngăn chặn gian lận, cho phép bất kỳ ai cũng có thể tự kiểm tra (audit) dữ liệu mà không cần thông qua bên thứ ba trung gian.
* **Thách thức (Quyền riêng tư):** Mặc dù địa chỉ ví có tính ẩn danh (pseudonymous), nhưng một khi địa chỉ ví bị liên kết với danh tính đời thực (thông qua sàn giao dịch KYC, định danh ENS hoặc đăng tải công khai), toàn bộ lịch sử tài chính, biến động tài sản và thói quen giao dịch của người dùng sẽ bị theo dõi hoàn toàn trên Etherscan.
