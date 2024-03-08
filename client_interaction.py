from solathon import Client
from solathon.keypair import Keypair
from solathon.solana_pay import create_transfer, parse_url
from solathon.solana_pay.types import TransferRequestURL
from solathon.transaction import Transaction

def simulate_wallet_interaction(client: Client, url: str, CUSTOMER_WALLET) -> None:
    print("🔗 Decode the url and get transfer parameters")
    # decoded: name of the variable that will store the URL with all relevant info for transfer (label, message etc.)
    decoded: TransferRequestURL = parse_url(url)

    print("🔑 Create a transfer and simulate sending it")
    # new_transfer: name of the variable that will store the Transaction information
    new_transfer: Transaction = create_transfer(client, CUSTOMER_WALLET, {
        "recipient": decoded.recipient, "amount": decoded.amount, "reference": decoded.reference})

    client.send_transaction(new_transfer)