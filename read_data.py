import networkx as nx


def load_simple(filename):
    """
    Reads simply formatted files for graph.

    The format is as followed:
    node1
    ...
    nodeN

    node1   nodei
    ...
    nodei   nodeN
    :param filename: string file name
    :return: netwotkx Graph
    """

    g = nx.Graph()

    # reade file
    with open(filename, 'r') as f:
        rows = f.readlines()

    # parse rows into nodes and edges
    for row in rows:
        r = row.rstrip()
        if '\t' in r:
            g.add_edge(r.split('\t')[0], r.split('\t')[1])
        elif (' ' == r) or ('' == r):
            pass
        else:
            g.add_node(r)
    return g


if __name__ == '__main__':

    import matplotlib.pyplot as plt

    g = load_simple('examples/data/net_file_CHO.tab')
    nx.draw_networkx(g)
    plt.show()