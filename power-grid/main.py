import networkx as nx
import pdb
import import_graph
import custom_graphs
import sys


G=import_graph.build_from_file(sys.argv[1])

rgb_colors = import_graph.open_colors(sys.argv[1])
  
custom_graphs.draw_weighted_edges(G)  

custom_graphs.draw_cheapest_connection(G, rgb_colors)





            
    
