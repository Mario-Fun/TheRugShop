import math
import requests

HEADERS = {
    "accept": "application/json",
    'X-API-KEY': '7avWNJ6gs97YBcywmr6veXjtm8OTSW1C'
}

TEST_COLLECTION = "0x0747118C9F44C7a23365b2476dCD05E03114C747"


def get_transfer(contract_addy):
    transfer_url = "https://api.transpose.io/nft/transfers-by-contract-address?contract_address=" + contract_addy + "&transfer_category=all&order=asc&limit=10"

    response = requests.get(transfer_url, headers=HEADERS)

    print(response.text)

    return response.text


def get_sales(contract_addy):
    sale_url = "https://api.transpose.io/nft/sales-by-contract-address?contract_address=" + contract_addy + "&order=asc&limit=10"

    response = requests.get(sale_url, headers=HEADERS)

    print(response.text)

    return response.text


get_sales(TEST_COLLECTION)
