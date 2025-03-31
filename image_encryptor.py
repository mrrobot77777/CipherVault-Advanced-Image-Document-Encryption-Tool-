from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from PIL import Image
import io

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

def encrypt_image(input_file, output_file, password):
    """Encrypt an image file with password protection"""
    try:
        # Generate key from password
        key = generate_key(password)
        f = Fernet(key)

        # Open and read the image
        with Image.open(input_file) as img:
            # Convert image to bytes
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format=img.format)
            img_byte_arr = img_byte_arr.getvalue()

        # Encrypt the image data
        encrypted_data = f.encrypt(img_byte_arr)

        # Write the encrypted data to output file
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

        print(f"Image successfully encrypted and saved as: {output_file}")
        return True
    except Exception as e:
        print(f"Error during encryption: {str(e)}")
        return False

def decrypt_image(input_file, output_file, password):
    """Decrypt an image file using the password"""
    try:
        # Generate key from password
        key = generate_key(password)
        f = Fernet(key)

        # Read the encrypted file
        with open(input_file, 'rb') as file:
            encrypted_data = file.read()

        # Decrypt the data
        decrypted_data = f.decrypt(encrypted_data)

        # Convert decrypted bytes back to image
        img = Image.open(io.BytesIO(decrypted_data))
        
        # Save the decrypted image
        img.save(output_file, format=img.format)
        
        print(f"Image successfully decrypted and saved as: {output_file}")
        return True
    except Exception as e:
        print(f"Error during decryption: {str(e)}")
        return False

def main():
    while True:
        print("\nImage Encryption/Decryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            input_file = input("Enter the path to the image file to encrypt: ")
            output_file = input("Enter the path for the encrypted image: ")
            password = input("Enter password for encryption: ")
            encrypt_image(input_file, output_file, password)
            
        elif choice == '2':
            input_file = input("Enter the path to the encrypted image: ")
            output_file = input("Enter the path for the decrypted image: ")
            password = input("Enter password for decryption: ")
            decrypt_image(input_file, output_file, password)
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 