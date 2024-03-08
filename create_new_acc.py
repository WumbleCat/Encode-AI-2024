from solathon import Client, Keypair

client = Client("https://api.devnet.solana.com")

new_account = Keypair()
print(new_account.public_key, new_account.private_key)