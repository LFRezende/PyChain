from flask import Flask, render_template, url_for, request, redirect
from backend.structures.chain import Block, Blockchain
from backend.scripts.deploy import blockchain, NONCE
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html', chain = blockchain.chain)

if __name__ == "__main__":
    app.run(debug=True)