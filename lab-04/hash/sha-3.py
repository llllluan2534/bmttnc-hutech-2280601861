from Crypto.Hash import SHA3_256

def sha3(message):
    """Compute the SHA-3 hash of a message."""
    # Create a SHA3_256 hash object
    sha3_hash = SHA3_256.new()
    
    # Update the hash object with the bytes of the message
    sha3_hash.update(message)
    
    # Return the hexadecimal digest of the hash
    return sha3_hash.digest()

def main():
    text = input("Nhap chuoi van ban: ").encode('utf-8')
    hashed_text = sha3(text)
    
    print("Chuoi van ban da nhap: ", text.decode('utf-8'))
    print("SHA-3 Hash: ", hashed_text.hex())
    
if __name__ == "__main__":
    main()