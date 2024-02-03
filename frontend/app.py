from flask import Flask, render_template, url_for, request, redirect
from backend.structures.chain import Block, Blockchain
from backend.scripts.functions import *
app = Flask(__name__)
blockchain = Blockchain()
Ok_Wallet = False
txRequest = False
@app.route('/', methods = ['POST', 'GET'])

def index():
    if request.method == 'POST':
        global Ok_Wallet
        global txRequest
        Ok_Wallet = False
        txRequest = False
        if "button_wallet" in request.form:
            createWalletWeb(blockchain.nonce, blockchain, "")
        if "button_allWallets" in request.form:
            Ok_Wallet = True
        if "button_tx" in request.form:
            txRequest = True
        if "send" in request.form:
            txValue = request.form["txPYC"]
            txSender = request.form["txYOURWallet"].strip()
            txReceiver = request.form["txWallet"].strip()
            if txValue < 0:
                txValue = 0
                print(f"txValue reverted: No cash sent.")
            # Check if sender exists:
            checkSender = False
            for k, v in enumerate(blockchain.wallets):
                if v["address"] == txSender:
                    checkSender = True
                    k1 = k
                    break
            if not checkSender:
                print("txSender reverted: No wallet as referenced was registered.")
            # Check if receiver exists:
            checkReceiver = False
            for k, v in enumerate(blockchain.wallets):
                if v["address"] == txReceiver:
                    checkReceiver = True
                    k2 = k
                    break
            if not checkReceiver:
                print("txReceiver reverted: No wallet as referenced was registered.")
            
            #Sender loses money
            blockchain.wallets[k1]["balance"] = blockchain.wallets[k1]["balance"] - txValue

            #Receiver gets money
            blockchain.wallets[k2]["balance"] = blockchain.wallets[k2]["balance"] + txValue

            # Appending block of the transaction
            blockchain.add_block(Block(blockchain.nonce, date.datetime.now(),f"Tx: {txSender[0:6]} ... -> {txReceiver[0:6]} ..."))

                    

        #noTerminal(globalNonce, blockchain)
        #nonce = simTerminal(NONCE, blockchain)
        return redirect("/")
        
    elif request.method == "GET":
        return render_template('index.html', chain = blockchain.chain, ok = Ok_Wallet, txRequest = txRequest, wallets = blockchain.wallets)
    
if __name__ == "__main__":
    app.run(debug=True)