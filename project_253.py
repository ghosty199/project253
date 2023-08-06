# --------------253 Proj----------------
from web3 import Web3
# Import time module here
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x794252DC1fd16086b562740B3A10560F1637e383'
James_account = '0xDBA3e692bb02308332863fce7DfF666e8b6f6Ae9'
Ryan_account  = '0x5A11E471F766a55A384b68db654eD40232AA374f'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce':"nonce2",
    'to':"James_account",
    'value':web3_ganache_connection.to_wei(2, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x2f553b215adb03b8cd2f3e50d2864201f95211678674aee6918b22571af7cdab'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.toHex("Print the Hash of the Block 1 here"))



# -----------------
"Define the print statement and" 
"sleep() function here"
# -----------------



nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.toWei(1, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(40,'gwei')
}

private_key2 = '0x2b729794a629dc859f37aae3b2f302d4aa3633217c919e1987f33f98bd3d5d01'

singed_transaction2 = web3_ganache_connection.eth.account.signTransaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.toHex("Print the Hash of the Block 2 here"))



