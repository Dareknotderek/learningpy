import qrcode
from PIL import Image

def create_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    url = input("Enter the URL or text you want to create a QR code for: ")
    file_name = input("Enter the filename for the QR code image (e.g., 'qr_code.png'): ")

    create_qr_code(url, file_name)

    print(f"QR code saved as {file_name}")

    # Optional: Display the generated QR code
    img = Image.open(file_name)
    img.show()

if __name__ == "__main__":
    main()
