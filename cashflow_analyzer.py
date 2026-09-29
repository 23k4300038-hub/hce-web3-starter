import os
import requests
import datetime

def analyze_wallet(wallet_address, days=90):
    api_key = os.getenv("ETHERSCAN_API_KEY", "YourApiKeyToken")
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&sort=asc&apikey={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    if data["status"] != "1":
        print(f"Lỗi API: {data.get('message', 'Không xác định')}")
        return

    transactions = data["result"]
    total_in = 0
    total_out = 0
    
    print(f"--- BÁO CÁO DÒNG TIỀN VÍ: {wallet_address} ({days} NGÀY GẦN NHẤT) ---")
    
    for tx in transactions:
        # LỖI AI 1: Giữ nguyên đơn vị wei, quên chia cho 10^18 để sang ETH (Vi phạm R5)
        value = float(tx["value"]) 
        
        # LỖI AI 2: Dùng continue bỏ qua giao dịch thất bại, không tính phí gas vào dòng tiền ra (Vi phạm R3 & R4)
        if tx["isError"] == "1":
            continue
            
        if tx["to"].lower() == wallet_address.lower():
            total_in += value
        elif tx["from"].lower() == wallet_address.lower():
            total_out += value

    print(f"Tổng dòng tiền vào: {total_in} wei")
    print(f"Tổng dòng tiền ra: {total_out} wei")
    print(f"Số dư ròng: {total_in - total_out} wei")

if __name__ == "__main__":
    test_wallet = "0x0000000000000000000000000000000000000000"
    analyze_wallet(test_wallet)
