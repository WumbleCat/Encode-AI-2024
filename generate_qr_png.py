import os
from solathon.solana_pay import create_qr

url = "solana:mvines9iiHiQTysrwkJjGf2gb9Ex9jXJX8ns3qwf2kN?amount=1e-09&label=Jungle+Cats+store&message=Jungle+Cats+store+-+your+order+-+%23001234&memo=JC%234098&reference=6DgHPm8gQp2mvQs5wuYTbJCH5KkkdJ7i4P76M31aegCQ"

def generate_qr_img(url):
    # Generate the QR Code
    qr_image = create_qr(url)
    # Move to the start of the BytesIO object
    qr_image.seek(0)
    # CONTAINS THE FINAL PNG FILE
    return qr_image.read()