from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password):
    """Generate a key from the password using PBKDF2"""
    salt = b'fixed_salt'  # In production, use a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_file(input_file, output_file, password):
    """Encrypt a file with password protection"""
    try:
        # Generate key from password
        key = generate_key(password)
        f = Fernet(key)

        # Read the input file
        with open(input_file, 'rb') as file:
            file_data = file.read()

        # Encrypt the data
        encrypted_data = f.encrypt(file_data)

        # Write the encrypted data to output file
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

        print(f"File successfully encrypted and saved as: {output_file}")
        return True
    except Exception as e:
        print(f"Error during encryption: {str(e)}")
        return False

def decrypt_file(input_file, output_file, password):
    """Decrypt a file using the password"""
    try:
        # Generate key from password
        key = generate_key(password)
        f = Fernet(key)

        # Read the encrypted file
        with open(input_file, 'rb') as file:
            encrypted_data = file.read()

        # Decrypt the data
        decrypted_data = f.decrypt(encrypted_data)

        # Write the decrypted data to output file
        with open(output_file, 'wb') as file:
            file.write(decrypted_data)

        print(f"File successfully decrypted and saved as: {output_file}")
        return True
    except Exception as e:
        print(f"Error during decryption: {str(e)}")
        return False

def main():
    while True:
        print("\nFile Encryption/Decryption Tool")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            input_file = input("Enter the path to the file to encrypt: ")
            output_file = input("Enter the path for the encrypted file: ")
            password = input("Enter password for encryption: ")
            encrypt_file(input_file, output_file, password)
            
        elif choice == '2':
            input_file = input("Enter the path to the encrypted file: ")
            output_file = input("Enter the path for the decrypted file: ")
            password = input("Enter password for decryption: ")
            decrypt_file(input_file, output_file, password)
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 