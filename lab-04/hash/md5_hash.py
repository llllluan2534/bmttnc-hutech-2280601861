def left_rotate(value, shift):
    """Rotate bits to the left."""
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    """Compute the MD5 hash of a message."""
    # Initialize variables
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Preprocessing: Padding the message
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'  # Append a single '1' bit (0x80 in hex)
    
    # Padding with zeros until the length is congruent to 448 mod 512
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    
    # Append the original length as a 64-bit integer
    message += original_bit_len.to_bytes(8, byteorder='little')

    # Process the message in 512-bit chunks
    for i in range(0, len(message), 64):
        block = message[i:i + 64] 
        words = [int.from_bytes(block[j:j + 4], byteorder='little') for j in range(0, 64, 4)]

        # Initialize working variables to current hash value
        a0, b0, c0, d0 = a, b, c, d

        # Main loop
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16
            
            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)) & 0xFFFFFFFF
            a = temp
        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF
    
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

input_string = input ("Nhap chuoi can bam: ") 
md5_hash = md5(input_string.encode('utf-8'))

print("Ma băm MD5 của chuỗi là '{}' la: {}".format(input_string, md5_hash))