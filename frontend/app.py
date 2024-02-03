from flask import Flask, render_template, url_for, request, redirect
from backend.structures.chain import Block, Blockchain
from backend.scripts.functions import *
app = Flask(__name__)
blockchain = Blockchain()
Ok_Wallet = False
txRequest = False
k1 = 0
k2 = 0
checkSender = False
checkReceiver = False
enoughPYC = True
txValue = 0
@app.route('/', methods = ['POST', 'GET'])

def index():
    if request.method == 'POST':
        global Ok_Wallet
        global txRequest
        global k1
        global k2
        global checkSender
        global checkReceiver
        global enoughPYC
        global txValue
        txValue = 0
        Ok_Wallet = False
        txRequest = False
        k1 = 0
        k2 = 0
        checkSender = True
        checkReceiver = True
        enoughPYC = True
        if "button_wallet" in request.form:
            createWalletWeb(blockchain.nonce, blockchain, "")
        if "button_allWallets" in request.form:
            Ok_Wallet = True
        if "button_tx" in request.form:
            txRequest = True
        if "send" in request.form:
            txValue = int(request.form["txPYC"].strip())
            txSender = request.form["txYOURWallet"].strip()
            txReceiver = request.form["txWallet"].strip()
            if txValue < 0:
                txValue = 0
                print(f"txValue reverted: No cash sent.")
            # Check if sender exists:
            checkSender = False
            enoughPYC = True
            for k, v in enumerate(blockchain.wallets):
                if v["address"] == txSender:
                    checkSender = True
                    k1 = k
                    if txValue > v["balance"]:
                        enoughPYC = False
                        print("Transaction Reverted: txSender lacks funds for this tx.")
                    break
            if not checkSender:
                print("txSender reverted: This txSender does not exist.")
            # Check if receiver exists:
            checkReceiver = False
            for k, v in enumerate(blockchain.wallets):
                if v["address"] == txReceiver:
                    checkReceiver = True
                    k2 = k
                    break
            if not checkReceiver:
                print("txReceiver reverted: This txReceiver does not exist.")
            
            if checkReceiver and checkSender and txValue > 0 and enoughPYC:
                #Sender loses money
                blockchain.wallets[k1]["balance"] = blockchain.wallets[k1]["balance"] - txValue

                #Receiver gets money
                blockchain.wallets[k2]["balance"] = blockchain.wallets[k2]["balance"] + txValue

                # Appending block of the transaction
                blockchain.add_block(Block(blockchain.nonce, date.datetime.now(),(f"Tx: {txSender[0:6]} ... ---> {txReceiver[0:6]} ...", txValue)))
            else:
                if not enoughPYC:
                    pass
                if not checkSender:
                    pass
                if not checkReceiver:
                    pass
                if txValue <= 0:
                    pass


        #noTerminal(globalNonce, blockchain)
        #nonce = simTerminal(NONCE, blockchain)
        return redirect("/")
        
    elif request.method == "GET":
        return render_template('index.html', chain = blockchain.chain, ok = Ok_Wallet, txRequest = txRequest, wallets = blockchain.wallets, enoughPYC = enoughPYC, txValue = txValue )
    
if __name__ == "__main__":
    app.run(debug=True)