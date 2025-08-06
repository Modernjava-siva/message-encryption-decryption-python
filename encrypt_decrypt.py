# encrypt_decrypt.py

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def save_to_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()

# Sample usage
if __name__ == "__main__":
    message = input("Enter message to encrypt: ")
    shift = 3
    encrypted = caesar_encrypt(message, shift)
    print("Encrypted:", encrypted)

    save_to_file("encrypted_output.txt", encrypted)

    # Optional Decryption
    file_data = read_from_file("encrypted_output.txt")
    decrypted = caesar_decrypt(file_data, shift)
    print("Decrypted:", decrypted)
