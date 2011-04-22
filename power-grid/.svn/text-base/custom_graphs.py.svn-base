import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def draw_weighted_edges(G):
    edge_width=[]
    for a,b in G.edges():
        edge_width.append(G[a][b]['weight'])
        
    p = nx.spring_layout(G, weighted=True, iterations=300)
    nx.draw(G,pos=p, node_size=800, width=edge_width, font_size=9, edge_color='green', font_color='black',node_color='red')
    plt.show()
    
def draw_cheapest_connection(G, rgb_colors):
    cheapest_list = []
    for node in G.nodes():
        cost = 0
        cheapest = 99
        for neighbor in G[node]:
            if G[node][neighbor]['weight']-1 < cheapest:
                cheapest = G[node][neighbor]['weight']-1
        cheapest_list.append(cheapest)
        
    i = 0
    tuples = []
    cities = G.nodes()
    for item in rgb_colors:
        tuples.append((rgb_colors[i],cheapest_list[i], cities[i]))
        i=i+1
        
    s = sorted(tuples, key=lambda student: student[0])
    
    #print tuples[0][0]
    
    
    cheapest_list=[]
    rgb_colors=[]
    cities=[]
    for item in s:
        cheapest_list.append(item[1])
        rgb_colors.append(item[0])
        cities.append(item[2])
        #print s
        
    #print cheapest_list
        
    #some constants for making the plot look nice
    ind = np.arange(G.number_of_nodes())
    width = 1
    plt.bar(ind, cheapest_list, width, color=rgb_colors)
    plt.xticks(ind+width/2.,cities, rotation=80, size=8)
    plt.ylabel('Lowest connection cost')
    
    plt.show()    
        
