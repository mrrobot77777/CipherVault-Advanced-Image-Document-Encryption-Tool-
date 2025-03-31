# File Encryption Tool

This is a simple command-line tool that allows you to encrypt and decrypt text files with password protection.

## Features

- Encrypt text files with password protection
- Decrypt previously encrypted files
- Uses secure encryption (Fernet symmetric encryption)
- Password-based key derivation (PBKDF2)

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```
   python file_encryptor.py
   ```

2. Choose from the following options:
   - Option 1: Encrypt a file
   - Option 2: Decrypt a file
   - Option 3: Exit

3. Follow the prompts to:
   - Enter the path to the input file
   - Enter the path for the output file
   - Enter the password for encryption/decryption

## Security Notes

- Keep your password safe and secure
- Never share your password with others
- The encrypted files cannot be decrypted without the correct password
- Make sure to backup your encrypted files

## Example

1. To encrypt a file:
   - Choose option 1
   - Enter the path to your text file (e.g., `document.txt`)
   - Enter the desired output path (e.g., `document.encrypted`)
   - Enter your password

2. To decrypt a file:
   - Choose option 2
   - Enter the path to your encrypted file (e.g., `document.encrypted`)
   - Enter the desired output path (e.g., `document_decrypted.txt`)
   - Enter the same password used for encryption 