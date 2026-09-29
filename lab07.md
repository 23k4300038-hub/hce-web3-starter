# BÁO CÁO LAB 7: TÍNH CHI PHÍ VẬN HÀNH THỰC TẾ (GAS COST ANALYSIS)

## 1. Bài toán kinh tế
Một câu lạc bộ sinh viên vận hành hệ thống thẻ tích điểm on-chain. Hệ thống phát sinh **1.000 giao dịch/tháng** (mỗi giao dịch ghi dữ liệu tiêu tốn ~20.000 gas).

---

## 2. Bảng tính toán chi phí vận hành hàng tháng

| Thông số | Mạng Ethereum Mainnet (Layer 1) | Mạng Layer 2 (Arbitrum / Optimism) |
| :--- | :--- | :--- |
| **Số lượng giao dịch / tháng** | 1.000 giao dịch | 1.000 giao dịch |
| **Tổng lượng gas tiêu thụ** | 20.000.000 gas | 20.000.000 gas |
| **Đơn giá Gas (Gas Price)** | 20 Gwei | 0,2 Gwei (Rẻ hơn 100 lần) |
| **Tổng phí giao dịch (ETH)** | 0,4 ETH | 0,004 ETH |
| **Giá ETH quy đổi** | 3.000 USD / ETH | 3.000 USD / ETH |
| **Tổng chi phí / tháng (USD)** | **1.200 USD** (~30 triệu VNĐ) | **12 USD** (~300.000 VNĐ) |

---

## 3. Phân tích mô hình và Kết luận khả thi

### A. Phân tích mô hình chi trả
* **Nếu áp dụng trên Layer 1 (Ethereum):** Chi phí $1.200 USD/tháng là quá đắt đỏ đối với một câu lạc bộ sinh viên. Nếu câu lạc bộ chi trả thì quỹ sẽ nhanh chóng cạn kiệt; nếu bắt sinh viên trả phí gas cho mỗi lần cộng điểm (~1,2 USD/lượt), sinh viên sẽ không chấp nhận sử dụng.
* **Nếu áp dụng trên Layer 2:** Chi phí chỉ $12 USD/tháng hoàn toàn nằm trong khả năng chi trả của quỹ câu lạc bộ, giúp trải nghiệm người dùng mượt mà và không tốn phí.

### B. Kết luận
Mô hình ứng dụng thẻ tích điểm sinh viên **chỉ khả thi khi triển khai trên các mạng Layer 2** (hoặc Sidechain) nhờ tối ưu hóa chi phí giao dịch đáng kể mà vẫn đảm bảo tính minh bạch on-chain.
