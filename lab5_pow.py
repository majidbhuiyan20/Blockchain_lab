import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash, difficulty):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.proof_of_work()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def proof_of_work(self):
        print(f"Mining Block {self.index}...")
        start_time = time.time()
        computed_hash = self.calculate_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            self.nonce += 1
            computed_hash = self.calculate_hash()
        end_time = time.time()
        print(f"Block {self.index} mined with nonce {self.nonce} in {round(end_time - start_time, 2)} seconds.")
        return computed_hash

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", difficulty=4)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, latest_block.hash, self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Nonce: {block.nonce}")
            print(f"  Hash: {block.hash}")

# Example usage
if __name__ == "__main__":
    my_blockchain = Blockchain(difficulty=3)  # Set difficulty level (number of starting zeros in hash)

    my_blockchain.add_block("Transaction 1")
    my_blockchain.add_block("Transaction 2")
    my_blockchain.add_block("Transaction 3")

    my_blockchain.print_chain()
