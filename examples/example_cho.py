from santa import SANTA
from read_data import load_simple

# graph data from file
g = load_simple('data/net_file_CHO.tab')

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