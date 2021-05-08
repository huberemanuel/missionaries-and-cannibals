from solver.state import State
from solver.node import Node

def bfs(initial_state: State):

    open_l = [Node(initial_state, None)]
    closed_l = []
    visiteds = set()
    
    final_node = None

    while open_l:
        actual_node = open_l.pop(0)
        visiteds.add(actual_node)

        if actual_node.state.is_done():
            final_node = actual_node
            break

        possible_movs = actual_node.possible_movs()
        for possible_mov in possible_movs:
            if not possible_mov in visiteds:
                new_node = Node(possible_mov, actual_node, not actual_node.left)
                open_l.append(new_node)
    return final_node

