import time
from io import BytesIO
from typing import Any, List, Literal
from solathon.core.types import TransactionSignature
from solathon.solana_pay import encode_url, create_qr, find_reference, validate_transfer
from solathon import Client, Keypair, PublicKey
from client_interaction import simulate_wallet_interaction

MERCHENT_WALLET = PublicKey("mvines9iiHiQTysrwkJjGf2gb9Ex9jXJX8ns3qwf2kN")

CUSTOMER_WALLET = Keypair.from_private_key([
    169, 48, 146, 127, 191, 185, 98, 158, 130, 159, 205, 137, 2, 146, 85, 1, 93, 107, 98, 90, 245, 69, 40, 39, 220,
    78, 226, 249, 231, 254, 92, 13, 186, 138, 174, 147, 156, 143, 248, 132, 28, 206, 134, 228, 241, 192, 94, 44,
    177, 15, 41, 219, 124, 116, 255, 78, 172, 209, 106, 78, 37, 169, 115, 146,
]) # This should be funded with some SOL

print(CUSTOMER_WALLET.public_key)