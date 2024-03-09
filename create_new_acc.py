from solathon import Client, Keypair, PublicKey

# Client always stays the same, since we're using solana
client = Client("https://api.devnet.solana.com")

# Create public and private keys
# new_account = Keypair()
# print(new_account.public_key, new_account.private_key)

# print(new_account.public_key)




# Get balance 
public_key = Keypair.from_private_key("qiFNjK8KMULzyJmLQeMik7Qpoj3Ji6at8cwxoBr3DDoBAkM87m9WyQiJAsYMdBmjTHoERYZLJh2NAjWt4yFhNPu")
balance = client.get_balance(public_key)

print(balance)

# lamport_to_sol(6000000000)