from solver.state import State
from solver.node import Node

def dfs(initial_state: State, max_depth: int=-1):
    """
    Performs depth first search, if max_depth is defined,
    then it will performs the limited depth dfs.

    Parameters
    ----------
    initial_state: State
        Initial problem configuration.
    max_detph: int
        Max depth of dfs search.

    Returns
    -------
    Node:
        Final node or None if no path is found
    """

    open_l = [Node(initial_state, None, True, 0)]
    closed_l = []
    visiteds = set()
    final_node = None

    while open_l:
        actual_node = open_l.pop(-1)
        visiteds.add(actual_node)

        if max_depth > -1 and actual_node.depth == max_depth:
            continue
        elif actual_node.state.is_done():
            return actual_node

        possible_movs = actual_node.possible_movs()
        print("Cheguei", possible_movs)
        for mov in possible_movs:
            if not mov in visiteds:
                depth = actual_node.depth + 1 if max_depth > -1 else -1
                new_node = Node(mov, actual_node, not actual_node.left, depth)
                open_l.append(new_node)

    return final_node


def bfs(initial_state: State):
    """
    Performs breadth first search, returning the final node if a path
    is found, otherwise returns None

    Paramters
    ---------
    initial_state: State
        Initial configuration of the problem.

    Returns
    -------
    Node:
        Final node or None.
    """

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

