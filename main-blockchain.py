import time
from io import BytesIO
from typing import Any, List, Literal
from solathon.core.types import TransactionSignature
from solathon.solana_pay import encode_url, create_qr, find_reference, validate_transfer
from solathon import Client, Keypair, PublicKey
from client_interaction import simulate_wallet_interaction

str_customer_private_key = "qiFNjK8KMULzyJmLQeMik7Qpoj3Ji6at8cwxoBr3DDoBAkM87m9WyQiJAsYMdBmjTHoERYZLJh2NAjWt4yFhNPu"
str_merchant_public_key = "mvines9iiHiQTysrwkJjGf2gb9Ex9jXJX8ns3qwf2kN"

def checkout_params() -> List[Any]:
    label = "Jungle Cats store"
    message = "Jungle Cats store - your order - #001234"
    amount = 1
    reference = Keypair().public_key

    return [label, message, amount, reference]


MERCHENT_WALLET = PublicKey(str_merchant_public_key)

# CUSTOMER_WALLET is an object that stores the attributes public key and private key
# It only needs the private key as input
CUSTOMER_WALLET = Keypair.from_private_key(str_customer_private_key) # This should be funded with some SOL

def main():
    # Tracking payment status through out the process
    payment_status: Literal["pending", "confirmed", "validated"] = None

    print("⚡ Connect to cluster")
    client = Client("https://api.mainnet-beta.solana.com")

    '''
    * Simulate a checkout experience
    *
    * Recommendation:
    * `amount` and `reference` should be created in a trusted environment (server).
    * The `reference` should be unique to a single customer session,
    * and will be used to find and validate the payment in the future.
    '''
    print("⭐ Simulate a checkout and get transaction parameters")
    [label, message, amount, reference] = checkout_params()

    '''
    * Create a payment request link
    *
    * Solana Pay uses a standard URL scheme across wallets for native SOL and SPL Token payments.
    * Several parameters are encoded within the link representing an intent to collect payment from a customer.
    '''
    print("🔗 Generate a link for the transfer")
    url: str = encode_url({"recipient": MERCHENT_WALLET, "label": label, "message": message,
                    "amount": amount, "reference": reference})

    print("🤖 Generate a cutomized solana pay QR code for link")
    qr_image_stream: BytesIO = create_qr(url)

    '''
    * Simulate wallet interaction
    *
    * This is only for example purposes. This interaction will be handled by a wallet provider
    '''
    print(
        f"💲Use the generated url({url}) or QR Code on client side for user to send and confirm the transaction")
    simulate_wallet_interaction(client, url, CUSTOMER_WALLET)
    
    payment_status = "pending"

    print("⏳ Waiting for payment to be confirmed")
    time.sleep(15)

    '''
    * Wait for payment to be confirmed
    *
    * When a customer approves the payment request in their wallet, this transaction exists on-chain.
    * You can use any references encoded into the payment link to find the exact transaction on-chain.
    * Important to note that we can only find the transaction when it's **confirmed**
    '''
    print("🔍 Find the transaction signature from reference public key")
    sign: TransactionSignature = find_reference(client, reference)

    payment_status = "confirmed"

    '''
    * Validate transaction
    *
    * Once the `findTransactionSignature` function returns a signature,
    * it confirms that a transaction with reference to this order has been recorded on-chain.
    *
    * `validateTransactionSignature` allows you to validate that the transaction signature
    * found matches the transaction that you expected.
    '''
    print("🔑 Validate the transaction")
    validate_transfer(client, sign.signature, { "recipient": MERCHENT_WALLET, "amount": amount, "reference": [reference] })

    payment_status = "validated"
    print("🎉 Payment is validated")
    print("📦 Order can be shipped to customer")

if __name__ == "__main__":
    main()