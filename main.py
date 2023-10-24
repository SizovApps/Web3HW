from web3 import Web3

INFURA_URL = "https://sepolia.infura.io/v3/8e9688cd01144a5284efd4b277eecf9c"
CONTRACT_ADDRESS = "0xd55af75e926b2873B4C88D6FB2A351BC23435C85"
ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint64","name":"age","type":"uint64"}],"name":"PlayerAdded","type":"event"},{"inputs":[{"internalType":"address","name":"wallet_address","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint64","name":"age","type":"uint64"}],"name":"addPlayer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"addressToPlayer","outputs":[{"internalType":"address","name":"wallet_address","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint64","name":"age","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wallet_address","type":"address"}],"name":"removePlayer","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)


def add_player(contract, my_address):
    nonce = web3.eth.get_transaction_count(my_address)
    gas_price = web3.to_wei('20', 'gwei')
    gas = 200000
    chain_id = 11155111

    transaction = contract.functions.addPlayer(my_address, "Vlad Sizov", 21).build_transaction({
        'chainId': chain_id,
        'gas': gas,
        'gasPrice': gas_price,
        'nonce': nonce,
    })

    signed_transaction = web3.eth.account.sign_transaction(transaction,
                                                           "YOUR_PRIVATE_KEY")

    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    swap_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(swap_receipt)


def subscribe_on_player_added_async(contract):
    event_filter = contract.events.PlayerAdded.create_filter(fromBlock="latest")

    while True:
        for event in event_filter.get_new_entries():
            print("Player added!")


def get_player(contract, my_address):
    print(contract.functions.addressToPlayer(my_address).call())


# subscribe_on_player_added_async(contract) - Запуск event listener

add_player(contract, "0x3eF47f599aA52B700956d57Eb73349A7252660aE")

get_player(contract, "0x3eF47f599aA52B700956d57Eb73349A7252660aE")

