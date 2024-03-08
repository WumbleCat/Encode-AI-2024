import os
from solathon.solana_pay import create_qr

def generate_qr_img(url):
    # Generate the QR Code
    qr_image = create_qr(url)
    # Move to the start of the BytesIO object
    qr_image.seek(0)
    # CONTAINS THE FINAL PNG FILE
    return qr_image.read()