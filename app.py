# HoldWallet - Basic Transaction Model

class Transaction:
    def __init__(self, buyer, seller, amount):
        self.buyer = buyer
        self.seller = seller
        self.amount = amount
        self.buyer_confirmed = False
        self.seller_confirmed = False
        self.status = "Pending"

    def confirm_buyer(self):
        self.buyer_confirmed = True
        self.check_status()

    def confirm_seller(self):
        self.seller_confirmed = True
        self.check_status()

    def check_status(self):
        if self.buyer_confirmed and self.seller_confirmed:
            self.status = "Completed"
            self.release_funds()

    def release_funds(self):
        print(f"Funds released to {self.seller}")

# Example usage
transaction = Transaction("Alice", "Bob", 100)
transaction.confirm_buyer()
transaction.confirm_seller()

print("Transaction status:", transaction.status)
