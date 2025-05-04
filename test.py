import hashlib
import datetime

class Block:
    def __init__(self, index, data, previous_hash, difficulty):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonse = 0
        self.hash = self.proof_of_work()

    def calculate_hash(self):
        block_string = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)+self(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
        