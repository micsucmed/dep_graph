
import json
from typing import List, Dict, Union

class Node:
    """
    A class to represent a node within the Dependecies graph.

    ...

    Attributes
    __________
    name: str
        Name of the package represented by the node
    children: List[Node]
        List of all the packages the current package depends on,
        this  will be representes as Nodes themselfs

    Methods
    _______

    """
    def __init__(self, name: str, children: List['Node'] = None):
        self.name = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.name})"

def read_dep_file(filename: str) -> Dict[str, List[str]]:
    """
    Reads the json file passed to the module

    Parameters
    __________
        filename: str
            path to the file containing the package list and their 
            dependencies
    """
    with open(filename, 'r') as file:
        dep_file = json.load(file)
    
    return dep_file

def construct_graph(filename: str) -> Dict[str, Node]:
    """
    Cunstructs the graph of dependancies based on the json file with the
    package dependencies

    Parameters
    __________
        filename: str
            path to the file containing the package list and their 
            dependencies
    """
    with open(filename, 'r') as file:
        dependencies = json.load(file)

    graph = {}
    for pkg, children in dependencies.items():
        if pkg not in graph:
            graph[pkg] = Node(pkg)
        for child in children:
            if child not in graph:
                graph[child] = Node(child)
            graph[pkg].children.append(graph[child])
    return graph