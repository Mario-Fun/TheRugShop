import math
import requests
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json

cred = credentials.Certificate("therugshop-f8614-firebase-adminsdk-6akik-f5758e10ef.json")
# firebase_admin.initialize_app(cred)

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app(cred)
db = firestore.client()


HEADERS = {
    "accept": "application/json",
    'X-API-KEY': '7avWNJ6gs97YBcywmr6veXjtm8OTSW1C'
}

TEST_COLLECTION = "0x7831729a089df41d7c5bcbd5cebb9d7d131addd3"

DUMMY_COLLECTION_LIST = ["0x7831729a089df41d7c5bcbd5cebb9d7d131addd3"]

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
    transfer_url = "https://api.transpose.io/nft/transfers-by-contract-address?contract_address=" + contract_addy + "&transfer_category=all&order=asc&limit=10"

    response = requests.get(transfer_url, headers=HEADERS)

    print(response.text)

    return response.text


def get_sales(contract_addy, transaction_limit = 10):
    sale_url = "https://api.transpose.io/nft/sales-by-contract-address?contract_address=" + contract_addy + "&order=asc&limit=" + str(transaction_limit)

    response = requests.get(sale_url, headers=HEADERS)

    print(response.text)

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
