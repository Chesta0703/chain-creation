import hashlib
from .models import Block, Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []

        # Create the genesis block
        self.create_block(data="Genesis block")

    def create_block(self, data):
        block = Block(data=data)
        if len(self.chain) > 0:
            block.previous_hash = self.chain[-1].hash
        block.save()
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender=sender, recipient=recipient, amount=amount)
        self.transactions.append(transaction)
        return transaction

    def mine_block(self):
        # Create a new block with the pending transactions
        block = self.create_block(data="New block")
        for transaction in self.transactions:
            transaction.save()
            block.transactions.add(transaction)
        self.transactions = []
        return block
