import math
import numpy as np
from multiprocessing.connection import wait
from time import sleep
import requests
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json

cred = credentials.Certificate("backend/therugshop-f8614-firebase-adminsdk-6akik-f5758e10ef.json")

# firebase_admin.initialize_app(cred)

import json

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app(cred)
db = firestore.client()


HEADERS = {
    "accept": "application/json",
    'X-API-KEY': '7avWNJ6gs97YBcywmr6veXjtm8OTSW1C'
}

TEST_COLLECTION = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"

json_file_path = "backend/playground-export.json"

with open(json_file_path, 'r') as j:
    data = json.loads(j.read())

DUMMY_COLLECTION_LIST = []

i = 0

to_use = np.array(data)

while i < to_use.shape[0]:
    DUMMY_COLLECTION_LIST.append(data[i]["contract_address"])
    i = i + 1

DUMMY_FRAUD_DATA = {}
DUMMY_FRAUD_DATA[u'walletAddress'] = u"0x1eea95f2d2ed24cd3451da93a69efdd08767cc5b"
DUMMY_FRAUD_DATA[u'twitterHandle'] = u"0xMario"
DUMMY_FRAUD_DATA[u'numWashCycles'] = 7
DUMMY_FRAUD_DATA[u'name'] = u"Mario"
DUMMY_FRAUD_DATA[u'ethWashed'] = 5
PROJECT_TEMP = {}
PROJECT_TEMP[u'address'] = u"0x7831729a089df41d7c5bcbd5cebb9d7d131addd3"
PROJECT_TEMP[u'name'] = u"Digital Monkeys"
DUMMY_FRAUD_DATA[u'project'] = PROJECT_TEMP


def get_transfer(contract_addy):
    transfer_url = "https://api.transpose.io/nft/transfers-by-contract-address?contract_address=" + contract_addy + "&transfer_category=all&order=asc&limit=1000"

    response = requests.get(transfer_url, headers=HEADERS)

    # print(response.text)

    return response.text


def get_sales(contract_addy, transaction_limit = 1000):
    # if depth == 0:
    #     return []
    
    # sale_url = "https://api.transpose.io/nft/sales-by-contract-address?contract_address=" + contract_addy + "&order=asc&limit=" + str(transaction_limit)

    # sales = []

    # response = requests.get(sale_url, headers=HEADERS)
    # sleep(0.5)
    # if "results" not in response.json():
    #     return
    # else:
    #     results = response.json()["results"]
    #     for result in results:
    #         print(len(sales))
    #         seller = result['seller']
    #         buyer = result['buyer']
    #         sales += [[seller, buyer]]
    #         get_sales(buyer, transaction_limit, depth - 1)
            
    # return sales
    
        
    # total_response = response[:]
    
    # for tx in response.text:
        # address = tx[0]
        # total_response += get_sales(address, transaction_limit, depth - 1)
        
    sale_url = "https://api.transpose.io/nft/sales-by-contract-address?contract_address=" + str(contract_addy) + "&order=asc&limit=" + str(transaction_limit)
    response = requests.get(sale_url, headers=HEADERS)
    response.raise_for_status() 
    if response.status_code != 204:
        return response.json()

    # print("response: " + response.text)
    
    return response.text
    


def push_firebase_obj(obj):
    db.collection('test_group').add(obj)

    return 0

push_firebase_obj(DUMMY_FRAUD_DATA)


def main():
    collections = DUMMY_COLLECTION_LIST
    # Collect a list of collections to monitor
    for collection_id in collections:
        # Get sales data
        sale_data = get_sales(collection_id)
        # get suspicious address data
        suspicious_add_data = TODO()
        # push said data to firestore
        push_firebase_obj(suspicious_add_data) 
