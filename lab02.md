# BÁO CÁO LAB 2: VÍ VÀ GIAO DỊCH ĐẦU TIÊN

## 1. Bảng đối chiếu giao dịch

| Trường thông tin | Giao dịch thành công | Giao dịch thất bại |
| :--- | :--- | :--- |
| **Mã băm giao dịch (TxHash)** | `0xb3abd9f53dfc50351d7531394de273db9037d0fed364ec13b662b788d96756f1` | N/A (MetaMask chặn do sai Checksum) |
| **Số tiền chuyển** | 0.01 Sepolia ETH | 0.01 Sepolia ETH |
| **Trạng thái** | Confirmed / Success | Rejected (Thất bại ngay tại ví) |
| **Nguyên nhân (nếu thất bại)** | N/A | Lỗi Checksum địa chỉ người nhận do nhập sai ký tự |

## 2. Câu hỏi lý thuyết

**Câu hỏi:** Nếu bạn chuyển nhầm tiền/token cho một địa chỉ người lạ trên blockchain, bạn có tự lấy lại được không? Vì sao?

**Trả lời:** 
Không, bạn hoàn toàn không thể tự lấy lại tiền hay đảo ngược giao dịch. Nguyên nhân là do mạng lưới blockchain hoạt động theo cơ chế bất biến (immutability), một khi giao dịch đã được xác nhận và ghi nhận vào khối thì không ai (kể cả quản trị viên) có quyền sửa đổi hay hủy bỏ. Cách duy nhất để lấy lại tiền là người nhận tự nguyện thực hiện một giao dịch mới để gửi trả lại cho bạn.
