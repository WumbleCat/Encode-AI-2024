from solathon import Client, PublicKey

client = Client("https://api.devnet.solana.com")

public_key_customer = PublicKey("8fzQH38cNiT249QNc17dxjtGKxyyzEJyDcVxGEeEdiwu")
balance_customer = client.get_balance(public_key_customer)

public_key_merchant = PublicKey("mvines9iiHiQTysrwkJjGf2gb9Ex9jXJX8ns3qwf2kN")
balance_merchant = client.get_balance(public_key_merchant)

print(balance_customer)
print(balance_merchant)