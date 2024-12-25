import json
from datetime import datetime

transactions = [
    {"type": "gold", "amount": 100, "price": 56000, "date": "2024-11-06"},
    {"type": "money", "amount": 2000, "price": 1, "date": "2024-11-06"},
]

def save_transactions_to_file(transactions):

    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"{current_time}.json"

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(transactions, file, ensure_ascii=False, indent=4)
    
    print(f"Dữ liệu giao dịch đã được lưu vào tệp: {filename}")

def main():
    while True:

        choice = input("Bạn có muốn nhập giao dịch mới không? (1: Có, 0: Không): ")
        if choice == "0":
            break
        elif choice == "1":
            type_ = input("Nhập loại giao dịch (gold/money): ")
            amount = float(input("Nhập số lượng: "))
            price = float(input("Nhập giá: "))
            date = input("Nhập ngày (YYYY-MM-DD): ")
            transactions.append({"type": type_, "amount": amount, "price": price, "date": date})

    save_choice = input("Bạn có muốn ghi giao dịch vào tệp không? (1: Có, 0: Không): ")
    if save_choice == "1":
        save_transactions_to_file(transactions)
    else:
        print("Không lưu giao dịch vào tệp.")

if __name__ == "__main__":
    main()
