from backend.structures.chain import Block, Blockchain
import datetime as date
import hashlib

def tx(amount, payer, receiver):
    message = f"  {str(payer).capitalize()} -> {str(receiver.capitalize())}: {amount:.1f} PTC  "
    return message.center(len(message) + 28) 

def store():
    Block()



blockchain = Blockchain()
NONCE = 1
while True:
    print("--- Select your option: --- ")
    op = int(input(" _-_-_-_-_- \n1 - Register your name and get a wallet.\n 2 - Pay some PTC to some friend\n 3- End.\n  _-_-_-_-_- "))
    if op == 1:
        name = str(input("Input your name")).capitalize().strip()
        time = date.datetime.now()
        name = name + str(NONCE) + str(time)
        wallet = "0x" +  hashlib.sha256(name.encode()).hexdigest()
        blockchain.add_block(Block(NONCE, time , f"Wallet created: {wallet[0:8]} ..."))
        NONCE = NONCE + 1
    elif op >= 3 or op <= 0:
        break


blockchain.add_block(Block(NONCE, date.datetime.now(),tx(5, "Alice", "Senai")))
blockchain.add_block(Block(NONCE + 1, date.datetime.now(),tx(10, "Memelo", "Zezélia")))
blockchain.add_block(Block(NONCE + 2, date.datetime.now(),tx(1.5, "Zézélia", "Baltor")))
blockchain.add_block(Block(NONCE + 3, date.datetime.now(),tx(8.5, "Lisa", "Mimira")))
blockchain.add_block(Block(NONCE + 4, date.datetime.now(),tx(50, "Elfo", "Bixaral")))

blockchain.read_chain()



