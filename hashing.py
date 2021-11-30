import hashlib, random, json

def randstrhash(algo):
    h = hashlib.new(algo)
    h.update(f"{random.getrandbits(128)}".encode('utf-8'))
    return h.hexdigest()
  
def hashcontents(algo, contents):
    h = hashlib.new(algo)
    h.update(json.dumps(contents).encode('utf-8')))
    return h.hexdigest()
  
# def proof_of_work(difficulty, contents):
#     req_hash = hashcontents('sha256', contents)
#     while rhash[:difficulty] != req_hash[:difficulty]:
#         rhash = randstrhash('sha256')
#     return True


