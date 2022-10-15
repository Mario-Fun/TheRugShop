import math
import requests


url = "https://api.transpose.io/nft/transfers-by-contract-address?contract_address=0x7831729a089df41d7c5bcbd5cebb9d7d131addd3&transfer_category=all&order=asc&limit=10"

headers = {
    "accept": "application/json",
    'X-API-KEY': '7avWNJ6gs97YBcywmr6veXjtm8OTSW1C'
}

response = requests.get(url, headers=headers)

print(response.text)
