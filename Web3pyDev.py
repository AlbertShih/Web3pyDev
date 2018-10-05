# This file is for the interaction with xxx ERC20 contract 
import json
import web3
import sys
import json
from web3 import Web3
from web3.contract import ConciseContract

#########################################################
# This input params are for Ganache local server testing
# input=[{ "value": 1, "address": "0xD0cd64B231Ef7078077b081D868748D88D66295c" },{ "value": 2, "address": "0x25Eba3400Feb93D489988D0aFF511E6cE82Ed381" }, { "value": 3, "address": "0x63C6C52a743dABe4cB0e1427124CaeecC8cB89EC" }]


#########################################################
# Init the web3 instance
# Ganache local server
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Main Etheruem
# w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/c8f0cdc466974f8abc5465f70061595a"))
# print ("Make sure we access to the main etheruem, wallet balnace: %d" % w3.eth.getBalance("0xa616259816e44dE443C238B5C76d62283456721d"))


#########################################################
# Get the input data from console
inputList = []
inputList = input('Please Input the proper param:')
inputList = eval(inputList)
for x in inputList:
    print ("%s’s ether balance is %f" % (x['address'], w3.fromWei(w3.eth.getBalance(x["address"]), 'ether')))


#########################################################
# Load the xxx contract
# xxx's contract info: https://coinmarketcap.com/currencies/xxxxx
# Note that in Python, there is capital for the bool variables (e.g., true => True)
ContractABI = ""
#ByteCode = '0x'+ xxx

# Ganache local server
contract = w3.eth.contract(abi=ContractABI, address=w3.toChecksumAddress("0x1598dd449d98006381cf74f784e44d05ef098680"))
# print (contract.call().balanceOf("0x5d91CA927d1ad7b4B20ACcb57dBC4B3B53759DCd"))

# Main Ethereum
#contract = w3.eth.contract(abi=ContractABI, address=w3.toChecksumAddress(''))
#print ("%f" % (w3.fromWei(contract.call().balanceOf("0xa616259816e44dE443C238B5C76d62283456721d"), 'ether')))


#########################################################
# Output will be like:
# 0x5f35f44792c4b932a34847439a62ca4991fa9f71’s ether balance is 20.10293 
# 0x5f35f44792c4b932a34847439a62ca4991fa9f72’s ether balance is 0 
# 0x5f35f44792c4b932a34847439a62ca4991fa9f73’s ether balance is 2
# Sent 1 xxx token to 0x5f35f44792c4b932a34847439a62ca4991fa9f71 and txhash: 
# 0xaad614e7e38aa17bec5e96cc84ce1a546ac1ae3c0e4e1371da197d0d7a661c9d 
# Sent 2 xxx token to 0x5f35f44792c4b932a34847439a62ca4991fa9f72 and txhash: 
# 0xaad614e7e38aa17bec5e96cc84ce1a546ac1ae3c0e4e1371da197d0d7a661c9e 
# Sent 3 xxx token to 0x5f35f44792c4b932a34847439a62ca4991fa9f73 and txhash: 
# 0xaad614e7e38aa17bec5e96cc84ce1a546ac1ae3c0e4e1371da197d0d7a661c9f 

for x in inputList:
	nonce = w3.eth.getTransactionCount("0x5d91CA927d1ad7b4B20ACcb57dBC4B3B53759DCd")
	txn = contract.functions.transfer(
		x['address'],
		x['value'],
		).buildTransaction({
		'chainId': 1,
		'gas': 300000,
		'gasPrice': w3.toWei('2', 'gwei'),
		'nonce': nonce,
	})
	#private_key = "8c961c954752a2c3b62422e2ebbc610d876b9a9ee4818064af85546a33bf89e2"
	signed_txn = w3.eth.account.signTransaction(txn, private_key=private_key)
	TxHash=w3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print("Sent %d xxx token to %s and txhash:" % (x['value'], x['address']))
	print(TxHash.hex())

# print (contract.call().balanceOf("0xD0cd64B231Ef7078077b081D868748D88D66295c"))