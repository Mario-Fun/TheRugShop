import json
import networkx as nx

from initial_api_test import TEST_COLLECTION, get_sales


# input: json response from the get_sales() function
# output: adjacency list of the transaction graph
class TransactionGraph:
    def __init__(self, sale_response):
        self.sale_response = json.loads(sale_response)
        self.m_num_sales = len(self.sale_response["results"])
        self.nodes = []

        # We iterate over all the responses and add the addresses to the nodes list
        for i in range(self.m_num_sales):
            if self.sale_response["results"][i]["seller"] not in self.nodes:
                print("appending seller")
                self.nodes.append(self.sale_response["results"][i]["seller"])

        self.m_adjacency_list = {node: set() for node in self.nodes}

        # We iterate over all the responses and add the edges to the adjacency list
        for sale in self.sale_response["results"]:
            print(sale)
            self.add_edge(sale["seller"], sale["buyer"],
                        tuple([sale["eth_price"], sale["usd_price"]]))
    
    def is_directed(self):
        return 1
    
    def add_edge(self, node1, node2,weight):
        self.m_adjacency_list[node1].add((node2,weight))

    def get_adj_list(self):
        return self.m_adjacency_list
    
    
# print(get_sales(TEST_COLLECTION))

# exit(0)

graph = TransactionGraph(get_sales(TEST_COLLECTION))
#print(graph.get_adj_list())
graph1 = nx.MultiDiGraph(graph.get_adj_list())
#print(graph1)
print(nx.find_cycle(graph1, orientation = None))