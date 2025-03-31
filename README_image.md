# Image Encryption Tool

This is a command-line tool that allows you to encrypt and decrypt image files with password protection. It supports common image formats like JPG, PNG, and others.

## Features

- Encrypt image files with password protection
- Decrypt previously encrypted images
- Supports multiple image formats (JPG, PNG, etc.)
- Uses secure encryption (Fernet symmetric encryption)
- Password-based key derivation (PBKDF2)
- Preserves original image format and quality

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```
   python image_encryptor.py
   ```

2. Choose from the following options:
   - Option 1: Encrypt an image
   - Option 2: Decrypt an image
   - Option 3: Exit

3. Follow the prompts to:
   - Enter the path to the input image file
   - Enter the path for the output file
   - Enter the password for encryption/decryption

## Security Notes

- Keep your password safe and secure
- Never share your password with others
- The encrypted images cannot be decrypted without the correct password
- Make sure to backup your encrypted images

## Example

1. To encrypt an image:
   - Choose option 1
   - Enter the path to your image file (e.g., `photo.jpg`)
   - Enter the desired output path (e.g., `photo.encrypted`)
   - Enter your password

2. To decrypt an image:
   - Choose option 2
   - Enter the path to your encrypted image (e.g., `photo.encrypted`)
   - Enter the desired output path (e.g., `photo_decrypted.jpg`)
   - Enter the same password used for encryption

## Supported Image Formats

The tool supports all image formats that the Pillow library can handle, including:
- JPEG/JPG
- PNG
- BMP
- GIF
- TIFF
- And many others 