from backend.structures.chain import Block, Blockchain
import datetime as date
NONCE = 1

blockchain = Blockchain()

blockchain.add_block(Block(NONCE, date.datetime.now(),"10 BTC de Alice para Bob"))
blockchain.add_block(Block(NONCE + 1, date.datetime.now(),"10 BTC de Charlie para Bob"))
blockchain.add_block(Block(NONCE + 2, date.datetime.now(),"10 BTC de Daniel para Bob"))
blockchain.add_block(Block(NONCE + 3, date.datetime.now(),"10 BTC de Ezekiel para Bob"))
blockchain.add_block(Block(NONCE + 4, date.datetime.now(),"10 BTC de Ferdinand para Bob"))

blockchain.read_chain()