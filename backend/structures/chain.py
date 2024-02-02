import hashlib
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash = ""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.blockHash()

    def blockHash(self):
        nonce = str(self.index)
        blockTime = str(self.timestamp)
        blockData = str(self.data)
        prevHash = str(self.previous_hash)

        # Compile all and then return the hashed form.
        block_raw = nonce + blockTime + blockData + prevHash

        return hashlib.sha256(block_raw.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.genesis()]
    
    def genesis(self):
        return Block(0, date.datetime.now(), "Genesis Block")

    def last_block(self):
        return self.chain[-1]
    
    def add_block(self, next_block):
        # Self aqui é para a blockchain, não o bloco.
        # O previous hash sofre overwriting, mesmo que ele já tenha.
        next_block.previous_hash = self.last_block().hash
        self.chain.append(next_block)
    
    def check_chain(self):
        for j in range(1, len(self.chain)):
            current_block = self.chain[j]
            prev_block = self.chain[j - 1]

            if current_block.hash != current_block.blockHash():
                message = f"### Error in Hashing ###\n Block no.{current_block.index} hashes to {current_block.hash}, yet should be {current_block.blockHash()}."
                print(message)
                return (False, message)
            
            if current_block.previous_hash != prev_block.hash:
                message = f"### MISMATCH ###\n Block no.{current_block.index} mismatches with Block no.{prev_block.index}"
                print(message)
                return (False, message)
        return (True, "### Chain Verified ###")
    
    def read_chain(self):
        print("\n|_-_-_-_ PyChain Ledger _-_-_-_|")
        print(f"\nRequest time: {date.datetime.now()}")
        for k, v in enumerate(self.chain):
            print(f"\nBlock no.{v.index}:")
            print(f" - Hash: 0x{v.hash}")
            print(f" - Previous Hash: 0x{v.previous_hash}")
            print(f" - Data: {v.data} ")
            print(f" - Timestamp: {v.timestamp}")


