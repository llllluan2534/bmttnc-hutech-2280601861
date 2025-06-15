import hashlib

def calculate_mad5(input_string):
    """Calculate the MD5 hash of the input string."""
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the bytes of the input string
    md5_hash.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return md5_hash.hexdigest()

input_string = input("Nhap chuoi can bam: ")
md5_hash = calculate_mad5(input_string)

print("ma băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))

