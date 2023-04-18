# QR Code Generator Documentation

The QR Code Generator is a simple Python script that generates QR codes from user-provided URLs or text. 
This documentation covers the installation, usage, and description of the functions included in the `qr_code_generator.py` script.

This was built with the help of GPT-4 to challenge assumptions and find bugs.

## Installation
Before using the QR Code Generator script, ensure that you have Python 3.6 or higher installed.

Next, install the required libraries using pip:

`pip install qrcode[pil]`

After installing the necessary libraries, download the `qr_code_generator.py` script.

## Usage

To use the QR Code Generator script, run the following command:

`python qr_code_generator.py`

The script will prompt you to enter a URL or text that you want to encode into a QR code. 
After that, you will be asked to provide a filename for the QR code image (e.g., 'qr_code.png').

Once you provide the required information, the script will generate a QR code and save it as an image file in the same directory. 
Optionally, the generated QR code will also be displayed using the Python Imaging Library (PIL).

## Function Descriptions

### create_qr_code

`def create_qr_code(data: str, filename: str) -> None:`

#### Parameters:

- `data` (str): The URL or text to encode into a QR code.
- `filename` (str): The filename to save the generated QR code image.

#### Returns:

- None.

#### Description:

This function generates a QR code from the provided data and saves it as an image file with the specified filename. 
The QR code is created using the `qrcode` library with the following configuration:

- Version: 1
- Error Correction: Level L (7%)
- Box Size: 10
- Border: 4

The generated QR code will have a white background and black data pixels.

### main

`def main() -> None:`

#### Parameters:

- None

#### Returns:

- None

#### Description:

This function serves as the entry point for the script. 
It prompts the user to enter a URL or text that they want to encode into a QR code, as well as a filename for the QR code image. 
After obtaining the user input, the function calls `create_qr_code` to generate the QR code and save it as an image file. 
Finally, the function displays a message indicating that the QR code has been saved and, optionally, 
shows the generated QR code using the Python Imaging Library (PIL).

