from Crypto.Hash import SHA256

def sha3(message):
    sha3_hash = SHA256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản: ")
    hashed_text = sha3(text.encode('utf-8'))
    print("SHA3 Hash của văn bản đã nhập:", hashed_text.hex())

if __name__ == "__main__":
    main()
