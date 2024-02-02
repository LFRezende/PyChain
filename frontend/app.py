from flask import Flask, render_template, url_for, request, redirect
from backend.structures.chain import Block, Blockchain
from backend.scripts.functions import *
app = Flask(__name__)
NONCE = 1
blockchain = Blockchain()

@app.route('/')

def index():
    simTerminal(NONCE, blockchain)
    return render_template('index.html', chain = blockchain.chain)

def indexing():
    while True:
        index()
    
if __name__ == "__main__":
    app.run(debug=True)