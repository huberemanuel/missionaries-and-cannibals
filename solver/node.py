from solver.state import State

class Node:

    def __init__(self, state, parent, left=True):
        self.state = state
        self.parent = parent
        self.left = left

    def print_solution(self):
        path = []
        actual_node = self
        while not actual_node is None:
            path.insert(0, actual_node)
            actual_node = actual_node.parent
        for i, node in enumerate(path):
            print(f"Node {i+1}: {node.state}")

    def possible_movs(self):
        possible_movs = []

        if self.left:
            movs = [
                State(self.state.lc-2, self.state.lm, self.state.rc+2, self.state.rm),
                State(self.state.lc-1, self.state.lm, self.state.rc+1, self.state.rm),
                State(self.state.lc, self.state.lm-2, self.state.rc, self.state.rm+2),
                State(self.state.lc, self.state.lm-1, self.state.rc, self.state.rm+1),
                State(self.state.lc-1, self.state.lm-1, self.state.rc+1, self.state.rm+1),
            ]
        else:
            movs = [
                State(self.state.lc+2, self.state.lm, self.state.rc-2, self.state.rm),
                State(self.state.lc+1, self.state.lm, self.state.rc-1, self.state.rm),
                State(self.state.lc, self.state.lm+2, self.state.rc, self.state.rm-2),
                State(self.state.lc, self.state.lm+1, self.state.rc, self.state.rm-1),
                State(self.state.lc+1, self.state.lm+1, self.state.rc-1, self.state.rm-1),
            ]
        for mov in movs:
            if mov.is_valid():
                possible_movs.append(mov)

        return possible_movs

