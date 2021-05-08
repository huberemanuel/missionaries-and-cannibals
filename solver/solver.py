from solver.state import State
from solver.search import bfs


def search(initial_state: State, method: str="bfs"):

    if method == "bfs":
        final_node = bfs(initial_state)
        if not final_node is None:
            final_node.print_solution()
        else:
            print("No solution was found :(")

def main():
    initial_state = State(3, 3, 0, 0)

    print("Initial state: ", initial_state)
    search(initial_state, "bfs")

if __name__ == "__main__":
    main()
