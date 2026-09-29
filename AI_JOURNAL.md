# NHẬT KÝ LÀM VIỆC VỚI AI - LAB 4

## Lần 1: Thẩm định rủi ro Smart Contract USDT

**Prompt:** 
"Bạn là chuyên viên thẩm định rủi ro tài sản số. Dưới đây là mã nguồn hợp đồng USDT. Hãy liệt kê mọi quyền đặc biệt mà chủ sở hữu (Owner) có thể thực hiện (ví dụ: mint, blacklist, withdraw, pause...). Với mỗi quyền, nêu rõ: Tên hàm, số dòng chính xác, và rủi ro cụ thể cho người nắm giữ token. Trình bày dưới dạng bảng."

**AI trả về:** 
Bảng phân tích chi tiết 10 hàm có quyền `onlyOwner` bao gồm: `issue` (dòng 396-403), `destroyBlackFunds` (dòng 285-291), `addBlackList` (dòng 275-278), `pause` (dòng 248-251), `deprecate` (dòng 381-385)... kèm đánh giá mức độ rủi ro cụ thể.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không có sai sót đáng kể về logic. AI nhận diện chính xác các hàm đặc quyền.

**Cách sửa:** Sinh viên tự đối chiếu số dòng của hàm `issue` và `addBlackList` trên Etherscan để xác nhận vị trí chuẩn xác.

**Ai phát hiện:** AI phân tích và Sinh viên kiểm chứng đối chiếu lại.

---

## Lần 2: Khảo sát thị trường và Tokenomics - LAB 5

**Prompt:**
"Dựa trên hình ảnh dữ liệu CoinMarketCap của BTC và ETH, hãy lập bảng so sánh các chỉ số thị trường (Giá, Vốn hóa, Volume 24h, Cung lưu hành, Max supply) và phân tích rủi ro Tokenomics của 2 đồng tiền này."

**AI trả về:**
Bảng số liệu chính xác theo hình ảnh chụp thực tế (BTC ~2,19 tỷ VND, ETH ~71 triệu VND) kèm phân tích rủi ro lạm phát/nguồn cung của từng đồng.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không có. Số liệu trích xuất chính xác từ ảnh giao diện tiếng Việt của CoinMarketCap.

**Ai phát hiện:** Sinh viên chụp ảnh màn hình cung cấp dữ liệu đầu vào chuẩn xác cho AI.

---

## Lần 3: Sinh mã Python và kiểm tra kết quả - LAB 6

**Prompt:**
"Đọc tệp SPEC.md trong dự án và viết chương trình Python thực hiện đúng đặc tả đó. Tuân thủ các quy ước trong AGENTS.md. Trước khi viết mã, tóm tắt lại cách bạn hiểu yêu cầu."

**AI trả về:**
Mã nguồn Python `cashflow_analyzer.py` kết nối Etherscan API để truy vấn lịch sử giao dịch và tính toán dòng tiền.

**Đánh giá:** ⚠️ Phải sửa.

**Chỗ sai (Phát hiện 2 lỗi do AI sinh ra theo danh mục kiểm tra):**
1. **Lỗi 1 (Đơn vị tiền - Vi phạm R5):** AI giữ nguyên giá trị ở đơn vị `wei` mà không chia cho 10^18 để đổi sang `ETH` trước khi hiển thị.
2. **Lỗi 2 (Bỏ qua giao dịch thất bại & Phí gas - Vi phạm R3 & R4):** AI dùng lệnh `continue` bỏ qua các giao dịch lỗi (`isError == 1`). Theo quy tắc R4, giao dịch thất bại vẫn tốn phí gas nên phải tính phí gas đó vào tổng dòng tiền ra.

**Cách sửa:**
- Bổ sung phép chia `value_eth = value / (10**18)`.
- Tính phí gas `gas_fee = (int(tx['gasUsed']) * int(tx['gasPrice'])) / (10**18)` và cộng phí này vào dòng tiền ra ngay cả khi giao dịch bị thất bại.

**Ai phát hiện:** Sinh viên đối chiếu với danh mục kiểm tra Lab 6 và phát hiện.
