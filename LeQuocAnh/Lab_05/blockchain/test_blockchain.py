from blockchain import Blockchain

# Testing the blockchain
my_blockchain = Blockchain()
# #dữ liệu tĩnh
# # Adding transactions
# my_blockchain.add_transaction('Alice', 'Bob', 10)
# my_blockchain.add_transaction('Bob', 'Charlie', 5)
# my_blockchain.add_transaction('Charlie', 'Alice', 3)

# # Mining a new block
# previous_block = my_blockchain.get_previous_block()
# previous_proof = previous_block.proof
# new_proof = my_blockchain.proof_of_work(previous_proof)
# previous_hash = previous_block.hash
# my_blockchain.add_transaction('Genesis', 'Miner', 1)
# new_block = my_blockchain.create_block(new_proof, previous_hash)

# # Displaying the blockchain
# for block in my_blockchain.chain:
#     print(f"Block #{block.index}:")
#     print("Index:", block.index, "                          Timestamp:", block.timestamp)
    
#     if not block.transactions:
#         print(f"Transactions: Rỗng ({block.transactions}), tức là không có giao dịch nào trong khối này.")
#     else:
#         print(f"Transactions: {block.transactions}")
    
#     print(f"Proof: {block.proof}                           Previous Hash: {block.previous_hash} - giá trị Hash của khối trước đó.")
#     print(f"Hash: {block.hash} - Giá trị hash của khối này")

# # Check if the blockchain is valid
# print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
 
 
 #dữ liệu động
 # Thêm các giao dịch nhập vào từ người dùng
num_transactions = int(input("Nhập số lượng giao dịch bạn muốn thêm vào blockchain: "))
for i in range(num_transactions):
    print(f"Giao dịch thứ {i + 1}:")
    sender = input("Nhập tên người gửi: ")
    receiver = input("Nhập tên người nhận: ")
    amount = float(input(f"Nhập số tiền giao dịch từ {sender} đến {receiver}: "))
    
    # Giả sử 'my_blockchain' có phương thức add_transaction để thêm giao dịch vào blockchain
    my_blockchain.add_transaction(sender, receiver, amount)
    
    # Thông báo giao dịch đã hoàn thành
    print(f"Hoàn thành giao dịch thứ {i + 1}")
# Tạo một block mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1) 

# Tạo khối mới và thêm vào chuỗi
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị chuỗi blockchain
for block in my_blockchain.chain:
    print(f"\nBlock #{block.index}:")
    print("Index:", block.index, "                          Timestamp:", block.timestamp)
    
    if not block.transactions:
        print(f"Transactions: Rỗng ({block.transactions}), tức là không có giao dịch nào trong khối này.")
    else:
        print(f"Transactions: {block.transactions}")
    
    print(f"Proof: {block.proof}                           Previous Hash: {block.previous_hash} - giá trị Hash của khối trước đó.")
    print(f"Hash: {block.hash} - Giá trị hash của khối này")