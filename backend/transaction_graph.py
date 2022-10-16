import json
from initial_api_test import COLLECTION_LIST
import networkx as nx

from initial_api_test import TEST_COLLECTION, get_sales

G = nx.MultiDiGraph()
sale_response = get_sales(TEST_COLLECTION, 1000)
sale_response1 = sale_response
m_num_sales = len(sale_response1["results"])
nodes = []

for i in range(m_num_sales):
    if sale_response1["results"][i]["seller"] not in G.nodes:
                G.add_node(sale_response1["results"][i]["seller"])
    if sale_response1["results"][i]["buyer"] not in G.nodes:
                G.add_node(sale_response1["results"][i]["buyer"])

for sale in sale_response1["results"]:
            G.add_edge(sale["seller"], sale["buyer"],
                        tuple([sale["eth_price"], sale["usd_price"]]))
 
print(list(nx.find_cycle(G)))