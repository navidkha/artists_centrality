import networkx as nx 
import csv


G = nx.Graph()

# Load Data
Data = open('archive/edges.csv', "r")
next(Data, None)  # skip the first line in the input file
Graphtype = nx.Graph()
G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype)

print(G.number_of_nodes())




