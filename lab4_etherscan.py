import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash, gas_limit, gas_used, miner):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.miner = miner 
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)+str(self.gas_limit)+str(self.gas_used)+str(self.miner)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.get_genesis_block()]

    def get_genesis_block(self):
        return Block(0,datetime.datetime.now(), "Genesis Block: ","0", 0,0, "Genesis Miner")
    
    def get_latest_block(self):
        return self.chain[-1]
    def add_block(self, data, gas_limit, gas_used, miner):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.datetime.now(),data, latest_block.hash,gas_limit, gas_used, miner)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"Block : {block.index}")
            print(f"    Time Stamp : {block.timestamp}")
            print(f"    Data: {block.data}")
            print(f"    Previous Hash: {block.previous_hash}")
            print(f"    Hash : {block.hash}")
            print(f"    Gas Limit: {block.gas_limit}")
            print(f"    Gas Used: {block.gas_used}")
            print(f"    Miner : {block.miner}")
            print("*"*80)


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Transaction 1: ", 10000, 5000, "Miner 1")
    blockchain.add_block("Transaction 2: ", 20000, 2000, "Miner 2")
    blockchain.add_block("Transaction 3: ", 30000, 3000, "Miner 3")

    print("Etherscan BlockChain Done: ")
    blockchain.print_chain()
