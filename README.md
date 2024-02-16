# Pychain 
## (Still Ongoing - Not Finished Yet)
A custom-made Proof of Work Blockchain, made in Python.
It is a simple project, just for fun!

It is envisioned to work as a similar knock-off of Bitcoin, where transactions are appended, wallets have to sign transactions, the chain works with the previous hash having to be the same as the current one, and so forth.

The original piece of code that inspired me to develop this project was conceived in an article, available 
at this address: 

https://medium.com/pythoneers/building-a-blockchain-from-scratch-with-python-489e7116142e/

Hence, I'd like to first thank the author for the kickstart.

Other functions and improvements are my complete authorship, though.

## How it works

The overall working of this application is simple:

### In the backend folder, we have the blockchain and block component features and functions. 

The overall key features of the block are:
- The Index
- The Hash
- The Previous Hash
- The Data
- The Value
- The Timestamp of the Block Creation

As we transact through the simulated environment of the deploy.py, we can choose in the control panel which features we wish to implement:
- Wallet Creation
- Transfer tokens to another address
- Register some information

In the near future, I wish to implement theses tasks through the UI, and well as create output text files to save the made blockchain for future uses.

The blockchain is created (and therefore its genesis block) the second we enter to deploy the script.

For now, we can create wallets that are made hashing our names with some other data, such as datetime.

These are compiled into the blockchain, and when we finish inserting data, the flask server activates and the UI loads the transactions made in localhost:5000.

Note: For now, the first while loop of options must be disregarded.  Hit an end key (such as 4) to end the first loop. A second one will start, and this will be the one to add data.





## NEXT STEPS ##

### Operational ###
- IRT adding of new transactions/wallets
- Wallet pallet
- Output file for re-loading chain (with verification algorithm for validity and PoW)
- Add terminal commands and environment

### Aesthetic  ###
- Add better formatting to table
- Better webpage design




