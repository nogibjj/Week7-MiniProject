def encrypt(text, shift):
    result = ""
    
    for c in text:
        if c.isalpha():
            # Check if character is lowercase or uppercase and get the base 'a' or 'A'
            base = ord('a') if c.islower() else ord('A')
            offset = (ord(c) - base + shift) % 26
            result += chr(base + offset)
        else:
            result += c
    
    return result

def decrypt(text, shift):
    return encrypt(text, 26 - shift)

def main():
    plaintext = "the quick brown fox jumps over the lazy dog"
    shift = 3
    ciphertext = encrypt(plaintext, shift)
    decrypted_text = decrypt(ciphertext, shift)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
