import string

def encrypt(text, shift):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            new_position = (alphabet.index(char) + shift) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char  # Keep spaces and punctuation unchanged
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just shifting in the opposite direction

# Example usage
message = "Mongkol"
shift_amount = 5

encrypted_message = encrypt(message, shift_amount)
decrypted_message = decrypt(encrypted_message, shift_amount)

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
