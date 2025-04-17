import qrcode


def generate_qr(link, output_file="phishing_qr.png"):
    try:
        qr = qrcode.make(link)  # Generate the QR code
        qr.save(output_file)  # Save it to a file
        print(f"QR Code saved successfully as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Test QR code generation with a test URL
test_url = "https://example.com"
generate_qr(test_url)
