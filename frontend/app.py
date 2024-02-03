from flask import Flask, render_template, url_for, request, redirect
from backend.structures.chain import Block, Blockchain
from backend.scripts.functions import *
app = Flask(__name__)
blockchain = Blockchain()
Ok = False
@app.route('/', methods = ['POST', 'GET'])

def index():
    if request.method == 'POST':
        global Ok
        Ok = False
        if "button_wallet" in request.form:
            createWalletWeb(blockchain.nonce, blockchain, "")
        if "button_tx" in request.form:
            return "Not avaiable yet :("
        if "button_allWallets" in request.form:
            Ok = True
        #noTerminal(globalNonce, blockchain)
        #nonce = simTerminal(NONCE, blockchain)
        return redirect("/")
        
    elif request.method == "GET":
        return render_template('index.html', chain = blockchain.chain, ok = Ok, wallets = blockchain.wallets)
    
if __name__ == "__main__":
    app.run(debug=True)