from solathon import Client, Keypair, PublicKey

# Client always stays the same, since we're using solana
client = Client("https://api.devnet.solana.com")

# Create public and private keys
new_account = Keypair()
print(new_account.public_key, new_account.private_key)

# Get balance 
public_key = PublicKey("B3BhJ1nvPvEhx3hq3nfK8hx4WYcKZdbhavSobZEA44ai")
balance = client.get_balance(public_key)

print(balance)
