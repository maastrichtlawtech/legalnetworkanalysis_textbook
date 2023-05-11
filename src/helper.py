
import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def load_graph_from_json(path):
    f = open(path, "r")
    data = json.load(f)
    graph = nx.node_link_graph(data)
    return graph

def score_normalize(dictvalues):
    dictvalues_arr = np.array([x for x in dictvalues])
    values_total = np.sum(np.abs(dictvalues_arr))
    return dictvalues_arr/values_total

def draw_spring(graph, seed=123, node_color="blue", figsize=(8,8)):
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(figsize))
    pos = nx.spring_layout(graph, seed = seed)
    nx.draw_networkx_nodes(graph, pos=pos, node_color=node_color, ax=ax)
    nx.draw_networkx_edges(graph, pos=pos, ax=ax)
    nx.draw_networkx_labels(graph, pos=pos, ax=ax);
