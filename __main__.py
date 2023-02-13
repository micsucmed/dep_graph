import json
from typing import Dict, List
from .dep_graph import read_dep_file, construct_graph, Node

def print_graph(nodes: List[Node], count_ind: int = 0):
    """
    Prints the graph in a recursive matter that makes sure the whole tree is printed
    
    Parameters
    __________
    nodes: List[Node]
        A list of all the packages mapped in the graph in Node representation
    count_ind: int
        The depth of dependency of a package, every time a package calls a dependancy
        the indentetion of the printing is incremented.
    """
    for node in nodes:
        print(f"{' '*count_ind}-{node.name}")
        if node.children:
            print_graph(node.children, count_ind=count_ind+1)


if __name__ == '__main__':
    """
    Executes the module and creates the dependency graph 
    """
    dependencies = read_dep_file('test.json')
    
    # We check if the dependencies are not reduntant so there is not an infinite recurtion in the
    # printing of the graph
    if all(dependencies.values()):
        print("No redundant dependencies found")
    else:
        print("Most likely there is a redundant dependency on your list, or a base dependency is missing")
    
    graph = construct_graph(dependencies)
    print_graph(graph.values())