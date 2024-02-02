import hashlib
import datetime as datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
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
