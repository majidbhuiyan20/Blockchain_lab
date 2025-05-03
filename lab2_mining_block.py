import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index 
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data)+ str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()
    

class Blockchain:
    def __init__(self):
        self.chain = [self.get_genesis_block()]

    
    def get_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block: ", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.datetime.now(), data, latest_block.previous_hash)
        self.chain.append(new_block)
    


    def print_chain(self):
        for block in self.chain:
            print(f"Block : {block.index}")
            print(f"    Time Stamp : {block.timestamp}")
            print(f"    Data: {block.data}")
            print(f"    Previous Hash: {block.previous_hash}")
            print(f"    Hash : {block.hash}")
            print("*"*90)


if __name__ == "__main__":
    blockchain = Blockchain()
    
    blockchain.add_block("Block 1: Hi")
    blockchain.add_block("Block 2: Hello")
    blockchain.add_block("Block 3: Bye")
    print("Before Mining the Block Chain is : ")
    blockchain.print_chain()

    blockchain.add_block("Block 4: Good Bye")
    print()
    print("After mining the Blockchain is: ")
    blockchain.print_chain()
