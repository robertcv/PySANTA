from santa import SANTA
import networkx as nx
import matplotlib.pyplot as plt

# This example shows how to use SANTA
# on a simple graph shown in the method article


# initialize a new empty graph
g = nx.Graph()

# set sample nodes and edges
nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
edges = [('1','2'), ('1','3'), ('1','4'), ('2','3'), ('2','4'),
         ('3','4'), ('1','5'), ('5','6'), ('2','7'), ('7','8'),
         ('4','9'), ('9','10'), ('3','11'), ('11','12')]

# insert nodes and edges into graph
for n in nodes:
    g.add_node(n)
for n1, n2 in edges:
    g.add_edge(n1, n2)

# set node weights to the nodes we want to observe
node_w = {'1':1, '2':1}

# initialize SANTA
test_santa1 = SANTA(g, node_w)

# run Knet
k_net, auc_k_net = test_santa1.k_net()
print('Knet:')
print(k_net)
print('AUK for Knet: ', auc_k_net)

# calculate p-value using n repetition
n = 1000
p_value = test_santa1.auk_p_value(n)
print('P-value for Knet: ', p_value)

# run Knode and return m best nodes
m = 5
k_node = test_santa1.k_node(m)
print('Knode:')
for n in k_node:
    print(n)

# draw the graph
nx.draw_networkx(g)
plt.show()