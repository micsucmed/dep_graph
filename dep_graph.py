import json
from typing import List, Dict, Union

class Node:
    def __init__(self, name: str, children: List['Node'] = None):
        self.name = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.name})"

def read_dep_file(filename: str) -> Dict[str, List[str]]:
    with open(filename, 'r') as file:
        dep_file = json.load(file)
    
    return dep_file

def construct_graph(dependencies: Dict[str, List[str]]) -> Dict[str, Node]:
    graph = {}
    for pkg, children in dependencies.items():
        if pkg not in graph:
            graph[pkg] = Node(pkg)
        for child in children:
            if child not in graph:
                graph[child] = Node(child)
            graph[pkg].children.append(graph[child])
    return graph