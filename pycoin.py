import time, hashlib, json, random

def blockchain(file_string=None):
    if file_string:
        return json.load(open(file_string))

    blocks = []
    return {"supply": 2.1e+7, "blocks": []}

def hash_contents(contents):

    h = hashlib.new('sha256')
    h.update(json.dumps(contents, sort_keys=True).encode('utf-8'))    
   
    return h.hexdigest()

def save_blockchain(blockchain, file_string="blockchain.json"):
    with open(f"{file_string}", "w") as f:
        json.dump(blockchain, f, indent=4)
    return True

def mine_block(blockchain, txs, miner_address):

    difficulty = 3

    prev_hash = hash_contents(blockchain["blocks"][-1])
    index = len(blockchain["blocks"])
    block = {"timestamp": time.time(), "txs": txs, "nonce": 0, "index": index,
             "prev_hash": prev_hash, "miner_address": miner_address}

    coinbase = {"timestamp": time.time(), "from": "0x00",
                "to": miner_address, "amount": 10, "msg": "block mined."}

    tx = {"tx": coinbase, "sig": hash_contents([coinbase, "0"])}

    block["txs"].append(tx)

    while not (hash_contents(block).startswith('0' * difficulty)):
        block["nonce"] += 1

    return block

def mine_gblock(blockchain, miner_address):
    
    if len(blockchain["blocks"]) > 0:
        return False

    prev_hash = 0
    gblock = {"timestamp": time.time(), "txs": [], "nonce": 0, "index": 0,
             "prev_hash": prev_hash, "miner_address": miner_address}

    coinbase = {"timestamp": time.time(), "from": "0x00",
                "to": miner_address, "amount": 10, "msg": "block mined."}

    tx = {"tx": coinbase, "sig": hash_contents([coinbase, "0"])}

    gblock["txs"].append(tx)

    gblock["nonce"] = 0
    while not (hash_contents(gblock).startswith('0' * 3)):
        gblock["nonce"] += 1

    return gblock

def add_latest_block(blockchain, verified_block):
    blockchain["blocks"].append(verified_block)



# blockchain = blockchain()

# gblock = mine_gblock(blockchain, "0x00893266390")
# add_latest_block(blockchain, gblock)


# for i in range(10):
#     b = mine_block(blockchain, [], "0x00893266390")
#     add_latest_block(blockchain, b)

# save_blockchain(blockchain, file_string="blockchain.json")

