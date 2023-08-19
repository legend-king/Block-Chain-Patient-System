from django.shortcuts import render
from django.http import JsonResponse
from .Blockchain import Blockchain
import json
from django.views.decorators.csrf import csrf_exempt

blockchain = Blockchain()

# Create your views here.
@csrf_exempt
def new_transaction(request):
    file_data = json.loads(request.body.decode('utf-8')) #get json response
    print(file_data)
    required_fields = ["patient", "name", "description", "report_file"]
    #if any of the fields is missing dont append and throw the message
    for field in required_fields:
        if not file_data.get(field):
            return JsonResponse({"message":"Transaction does not have valid fields!"},status=404)
    #else append it to pending transaction
    blockchain.add_pending(file_data)
    result = blockchain.mine()
    if result:
        print("Block #{0} mined successfully.".format(result))
    else:
        print("No pending transactions to mine.")
    return JsonResponse({"message":"Success"}, status=201)

def get_chain(request):
    # consensus()
    chain = []
    #create a new chain from our blockchain
    for block in blockchain.chain:
        chain.append(block.__dict__)
    #print chain len
    print("Chain Len: {0}".format(len(chain)))
    return JsonResponse({"length" : len(chain), "chain" : chain})


# def validate_and_add_block(request):
#     block_data = request.get_json() #get the json response
#     #create a new block incl its hash
#     block = Block(block_data["index"],block_data["transactions"],block_data["prev_hash"])
#     hashl = block_data["hash"]
#     #append the new block
#     added = blockchain.add_block(block, hashl)
#     #if not added succesfully
#     if not added:
#         return JsonResponse({"messgae":"The Block was discarded by the node."}, 400)
#     return JsonResponse({"message":"The block was added to the chain."}, 201)