#import numpy as np

def create_adjacency_list(filename):
    # initialize empty dictionary
    graph = {}

    # open file and read the content in a list
    with open(filename, 'r') as file:
        # iterate over the list
        for line in file:
            # remove line break ('\n') from list element
             if line[0] != '#':
                temp = line.split()

                # convert list element into integers
                temp = [int(i) for i in temp]

                # if the first node is not in dictionary, add it
                if temp[0] not in graph:
                    graph[temp[0]] = []
                if temp[1] not in graph:
                    graph[temp[1]] = []

                # append second node to the key of the first node
                graph[temp[0]].append(temp[1])

    return graph

def get_vertices(edges):
    vertices = [n for n in edges.keys()]
    return vertices
