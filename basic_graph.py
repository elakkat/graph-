# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:17:06 2018

@author: Gireesh
"""

def generate_edges(graph): 
    edges=[]
    for nodes in graph:
        for neighbour in graph[nodes]:
            edges.append((nodes, neighbour))
        return (edges)
def find_path_two_vertices(graph, start, end, path=[]):
    path=path+[start]
    if start==end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath= find_path_two_vertices(graph, node, end, path)
            if newpath:
                return newpath
    return None        
def shortest_path_two_vertices(graph, start, end, path=[]):
    path=path+[start]
    if start==end:
        return path
    if not start in graph:
        return None
    shortest_path=None
    for node in graph[start]:
        if node not in path:
            newpath=shortest_path_two_vertices(graph, node,end, path)
            if newpath:
                if not shortest_path or len(shortest_path)<len(newpath):
                    shortest=newpath
    return newpath
def find_all_paths(graph, start, end, path=[]):
    path=path+[start]
    if start==end:
        return[path]
    if not start in graph:
        return[]
    found_paths=[]
    for node in graph[start]:
        if node not in path:
            newpath_find=find_all_paths(graph, node, end, path)
            for newpaths in newpath_find:
                found_paths.append(newpaths)
    return found_paths
def find_cycle_single_node(graph, start):
    for node in graph[start]: 
        for node in graph[start]:
            if node==start:
                return 1
        return 0
def find_isolated_node(graph):
    isolated_node=[]
    for node in graph:
        if not graph[node]:
            isolated_node.append(node)
    return isolated_node

def add_edge(graph, edge):
    edge=set(edge)
    (n1,n2)=tuple(edge)
    if n1 in graph:
        graph[n1].append(n2)
    else:
        graph[n1]=n2
    return graph

def find_degree(graph, node):
    degree=0
    t=[]
    for neighbour in graph [node]:
        t.append(neighbour)
        degree=degree+1
    return degree
def graph_connected (graph, seen_node=None, start=None):
    if seen_node==None:
        seen_node=set()
        nodes=list(graph. keys())
        if not start:
            start=nodes[0]
        seen_node.add(start)
        if len(seen_node)< len(nodes):
            for othernodes in graph[start]:
                if othernodes not in seen_node:
                    if graph_connected(graph, seen_node, othernodes):
                        return True
        else:
            return True
        return False
# Main function for creation of graph

if __name__=='__main__':
    graph={
       'A':['A','B','C','Q','X', 'Y'],
       'B':['C','D'],
       'C':['D'],
       'D':['C'],
       'E':['F'],
       'F':['C'],
       'G':[],
       'P':[]
           }
    print (graph['A'])
    print('the nodes (vertices) of the graphs', graph. keys(), '\n The edges of the graph: for keys{0} are {1}'. format (graph.keys(), graph. values()))
    print ('The generated edges are:', generate_edges(graph))
    print ('Path between two vertices:', find_path_two_vertices(graph,'A','D', path=[]))        
    print('shortest path between two vertices:', shortest_path_two_vertices(graph,'A','D', path=[]))
    cycle=find_cycle_single_node(graph,'D')
    if cycle:
        print ('Cycle exist')
    else:
        print ('No cycle exist')
        print ('isolated node is:' , find_isolated_node(graph))
        print('Add an edge:', add_edge(graph, {'A','B'}))
        Degree=find_degree(graph,'A')
        print('Degree of the veretx:', Degree)
        conn=graph_connected(graph, seen_node=None, start=None)
        if conn:
            print ('The graph is connected')
        else:
            print ('THe graph is not connected')
        
        
        
