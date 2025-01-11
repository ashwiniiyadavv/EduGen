from cryptography.fernet import Fernet

# Generate a key (only once and store it securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the API key
api_key = "your_api_key_here"
encrypted_api_key = cipher_suite.encrypt(api_key.encode())

# Save the encrypted API key (e.g., in a file)
with open("encrypted_api_key.txt", "wb") as f:
    f.write(encrypted_api_key)

# Decrypt the API key when needed
with open("encrypted_api_key.txt", "rb") as f:
    encrypted_api_key = f.read()

decrypted_api_key = cipher_suite.decrypt(encrypted_api_key).decode()
print("Decrypted API Key:", decrypted_api_key)
