from backend.structures.chain import Block, Blockchain
from backend.scripts.functions import *
import datetime as date
import hashlib
NONCE = 1
blockchain = Blockchain()
blockchain.add_block(Block(NONCE, date.datetime.now(),tx(5, "Alice", "Senai")))
blockchain.add_block(Block(NONCE + 1, date.datetime.now(),tx(10, "Memelo", "Zezélia")))
blockchain.add_block(Block(NONCE + 2, date.datetime.now(),tx(1.5, "Zézélia", "Baltor")))
blockchain.add_block(Block(NONCE + 3, date.datetime.now(),tx(8.5, "Lisa", "Mimira")))
blockchain.add_block(Block(NONCE + 4, date.datetime.now(),tx(50, "Elfo", "Bixaral")))

blockchain.read_chain()
