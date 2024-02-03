from backend.structures.chain import Block, Blockchain, wallets
import datetime as date
import hashlib
from random import randint


def tx(amount, payer, receiver):
    message = f" {str(payer).capitalize()} -> {str(receiver.capitalize())} "
    return (message.center(len(message) + 28), amount)



def createWallet(nonce, blockchain):
        name = str(input("State your name:      ")).capitalize().strip()
        time = date.datetime.now()
        name_raw = name + str(nonce) + str(time)
        wallet = "0x" +  hashlib.sha256(name_raw.encode()).hexdigest()
        blockchain.add_block(Block(nonce, time , (f"Wallet created: {wallet[0:8]} ...", 0 )))
        nonce = nonce + 1
        return nonce

def createWalletWeb(nonce, blockchain, name, infCash = True):
        #name = str(randint(1, 2**32 - 1))
        time = date.datetime.now()
        name_raw = name + str(nonce) + str(time)
        wallet = "0x" +  hashlib.sha256(name_raw.encode()).hexdigest()
        walletBalance = 0
        blockchain.add_block(Block(nonce, time , (f"Wallet created: {wallet[0:8]} ...", 0 )))
        nonce = nonce + 1
        blockchain.nonce = nonce
        if infCash:
             walletBalance = 100
        wallets.append({"address": wallet, "balance": walletBalance})
        blockchain.wallets = wallets
        return (nonce, name, wallet)

def listWalletsWeb(blockchain):
     print("Listing all wallets in server ... ")
     return blockchain.wallets

def simTerminal(nonce, blockchain):
    while True: 
        print("===== PyChain Environment ===== ")
        op = int(input("=============================== \n[1] - Register your name and get a wallet.\n[2] - Pay some PTC to some friend\n[3] - End.\n=============================== "))
        if op == 1:
            nonce = createWallet(nonce, blockchain)
        elif op == 3:
            break
        else:
            print("ERROR - Give one of the inputs required in the table.")
    return nonce

def noTerminal(nonce, blockchain):
  
    print("===== PyChain Environment ===== ")
    op = int(input("=============================== \n[1] - Register your name and get a wallet.\n[2] - Pay some PTC to some friend\n[3] - End.\n=============================== "))
    if op == 1:
        nonce = createWallet(nonce, blockchain)
    else:
        print("ERROR - Give one of the inputs required in the table.")
    return nonce

