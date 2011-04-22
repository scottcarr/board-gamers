import networkx as nx
import string

def build_from_file(board):
    G = nx.Graph()
    f_cities = open('./' + board + '/' + 'cities.txt','r')
    f_edges = open('./' + board + '/' + 'edges.txt','r')
    cities_list = f_cities.readlines()
    edges_list = f_edges.readlines()
    
    for line in edges_list:
        parts = string.split(line,',')
        w = int(parts[2])+1
        G.add_edge(parts[0], parts[1], weight=w)
    
    return G

def open_colors():
    f_colors = open('./' + board + '/' + 'colors.txt','r')
    colors_list = f_colors.readlines()
    
    rgb_colors=[]
    for item in colors_list:
        if item == 'blue\n':
            rgb_colors.append('#0000ff')
        if item == 'red\n':
            rgb_colors.append('#ff0000')
        if item == 'purple\n':
            rgb_colors.append('#ee00ee')
        if item == 'yellow\n':
            rgb_colors.append('#ffff0c')
        if item == 'teal\n':
            rgb_colors.append('#66ffff')
        if item == 'brown\n':
            rgb_colors.append('#cc6600')
    
    return rgb_colors
