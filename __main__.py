import json
from typing import Dict, List
from .dep_graph import read_dep_file, construct_graph, Node

def print_graph(nodes: List[Node], count_ind: int = 0):
    for node in nodes:
        print(f"{' '*count_ind}-{node.name}")
        if node.children:
            print_graph(node.children, count_ind=count_ind+1)


if __name__ == '__main__':
    dependencies = read_dep_file('test.json')
    
    if all(dependencies.values()):
        print("No redundant dependencies found")
    else:
        print("Most likely there is a redundant dependency on your list, or a base dependency is missing")
    
    graph = construct_graph(dependencies)
    print_graph(graph.values())