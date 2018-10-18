
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 23:24:11 2018

@author: Gireesh
"""

""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""
#import networkx as nx
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import seaborn as sns

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()
    
    def degree(self):
        """rerurns the degree of each element"""
#        print(self.__graph_dict)
        degree={k:len(v) for k, v in self.__graph_dict.items()}
        self.degree=degree
#        print(self.degree)
        return self.degree

    def add_vertex(self, vertex,target):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            self.__graph_dict[target].append(vertex)
            self.__graph_dict[vertex].append(target)
        return self
    
    def add_edge(self,u,v): 
        print(u,v)
        if u in self.__graph_dict:
            self.__graph_dict[u].append(v)
        else:
            self.__graph_dict[u] = [v]
#        self.__graph_dict[u]=[v]
#        print(self.__graph_dict)
        return self
    
#    def addedge(self, edge):
#        """ assumes that edge is of type set, tuple or list; 
#            between two vertices can be multiple edges! 
#        """
##        edge = set(edge)
##        (vertex1, vertex2) = tuple(edge)
#        if vertex1 in self.__graph_dict:
#            self.__graph_dict[vertex1].append(vertex2)
#        else:
#            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def remove_vertex(self, vertex):
#        print("in remove vertex:", vertex)
#        print("DICT KEYS:", self.__graph_dict.keys())
#        vertex=vertex-1
        if vertex in self.__graph_dict.keys():
#            print("before:", self.__graph_dict)
#            print('vertex:',self.__graph_dict[vertex])
            del self.__graph_dict[vertex]
#            del self.__graph_dict[vertex][:]
#            print("after:", self.__graph_dict)
            for v in self.__graph_dict.values():
                if (vertex) in v:
                    v.remove((vertex))             
        return self 
    
    def prefered_node_for_attachment(self):
        degree={k:len(v) for k, v in self.__graph_dict.items()}
#        print('ASSESSING DEGREE:', self.__graph_dict)
#        print('degree:', degree)
        degrees =  list(degree.values())
#        print("DEGREES", degrees)
        array=np.array(degrees)
#        (m,index) = max((v,i) for i,v in enumerate(array))
        index=np.argmax(array)
#        print('INDEX:', index)
        self.preferred_node = list(self.__graph_dict)[index]; # as indexing start from 0
#        print("PREFERRED:",list(self.__graph_dict)[index])
        
#        print("preferred node for attachment:", self.preferred_node)
        return self.preferred_node  
    
    def prefered_node_for_deletion(self):
        degree={k:len(v) for k, v in self.__graph_dict.items()}
#        print(degree)
        degrees = list(degree.values())
#        print (degrees)
        number_of_nodes=len(G.vertices())
#        print(degrees.values())
        array=np.array(degrees)
#        print(array)
        nt_dt_diff=number_of_nodes -array
#        print(nt_dt_diff)
        nt_squared_mt_diff=number_of_nodes**2-2*(len(G.edges()))
        prob_deletion=nt_dt_diff/nt_squared_mt_diff
        (m,index) = max((v,i) for i,v in enumerate(prob_deletion))
        self.preferred_node_d =list(self.__graph_dict)[index]; # as indexing start from 0
        return self.preferred_node_d 
    
    def printgraph(self):
        print(self.__graph_dict)
        return self
    
    
        
        
if __name__ == "__main__":
        
        number_of_iterations=[10000,20000,30000,40000, 50000]
        probabilities=[0.6,0.75,0.9]
        node_number={}
        edge_number={}
        mult_factor=100
        number_of_it=[]
        g = { '0' : ['0']
        }
        G = Graph(g)  
#        G.add_vertex(0)
#        G.add_edge(0,0)
        for pind in range (0,3):            
            for n in range (0,5):
                for i in range (1,mult_factor*(n+1)):
                    random_number=random.random()
        #            print(random_number)    
#                    print(probabilities[pind])        
                    if random_number < probabilities[pind]:
                       
        #                print("edges length:", len(G.edges()))
    #                    new_node_number=len(G.edges())+1
                        preferred_node=G.prefered_node_for_attachment()
                        G.add_vertex(i, preferred_node)
        #                print("i:",i)
        #                G.add_edge(preferred_node,i)
        #               print(preferred_node)
        #               G.printgraph()
        #               print('p:', preferred_node)
                    else:
                        preferred_node_d=G.prefered_node_for_deletion()
        #               del G[preferred_node_d]
        #               if G.has_node(preferred_node_d): 
        #                print('d:', preferred_node_d)
                        G.remove_vertex(preferred_node_d)          
                    if  len(G.vertices())==0:
        #                print(len(G.vertices()))
                        G.add_vertex(0,0)
#                node_number.append(len(G.vertices()))
#                edge_number.append(len(G.edges()))
                node_number[pind,n]=len(G.vertices())
                edge_number[pind,n]=len(G.edges())
                g = { '0' : ['0']
                }
                G = Graph(g)
#                print(i+1)    
                number_of_it.append(i+1)    
        
#        print('nodes:', node_number)
#        print('edges:', edge_number)
        
        node_theoretical={}
        edge_theoretical={}
        for pind in range (0,3):
            for i in range (1,mult_factor*(i+1)):
               n_t= (probabilities[pind]-(1-probabilities[pind]))*i+(2*(1-probabilities[pind]))
               node_theoretical[pind,i]=n_t
               e_t=probabilities[pind]*(probabilities[pind]-(1-probabilities[pind]))
               edge_theoretical[pind,i]=n_t
        theoretical_nodes=list(node_theoretical.values())
        theoretical_edges=list(edge_theoretical.values())
        t_t_step=list(range (1,mult_factor*5))
        
        nodes=list(node_number.values())
        edges=list(edge_number.values())
        plt.plot(number_of_it[0:5], nodes[0:5], 'o', number_of_it[0:5],  nodes[5:10], 'x', number_of_it[0:5], nodes[10:16], '*',\
                 t_t_step,theoretical_nodes[0:(mult_factor*5-1)],t_t_step,theoretical_nodes[mult_factor*5-1 : mult_factor*10-2],\
                 t_t_step,theoretical_nodes[mult_factor*10-2 : mult_factor*15-3] )
        
        plt.title('Nodes')
        plt.show()
#        plt.plot(number_of_it[0:5], edges[0:5], 'o', number_of_it[0:5],  edges[5:10], 'x', number_of_it[0:5], edges[10:16], '*')
#        plt.title('Edges')
#        plt.show()
#        np.save('assignment2_10k.npy', node_number,edge_number) 
##        G.printgraph()
            
            
#        nx.draw_shell(G, nlist=[range(1, 100), range(100)], with_labels=True, font_weight='bold')
#    
    #G.add_nodes_from([1,2])
#   G.add_edge(0,0)
    #G.add_edge(1,2)
    #G.add_path([0,2])
    #G.add_path([2,9,7,'A'])
    #G.remove_edge(0,1)

    
    
#    print("Vertices of graph:")
#    print(graph.vertices())
#
#    print("Edges of graph:")
#    print(graph.edges())
#
#    print("Add vertex:")
#    graph.add_vertex("z")
#
#    print("Vertices of graph:")
#    print(graph.vertices())
# 
#    print("Add an edge:")
#    graph.add_edge({"a","z"})
#    
#    print("Vertices of graph:")
#    print(graph.vertices())
#
#    print("Edges of graph:")
#    print(graph.edges())
#
#    print('Adding an edge {"x","y"} with new vertices:')
#    graph.add_edge({"x","y"})
#    print("Vertices of graph:")
#    print(graph.vertices())
#    print("Edges of graph:")
#    print(graph.edges())
#  

