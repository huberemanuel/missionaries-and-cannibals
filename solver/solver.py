from solver.state import State
from solver.search import bfs


def search(initial_state: State, method: str="bfs"):
    """
    Performs search on the provided initial_state using the provided
    search method.

    Parameters
    ----------
    initial_state: State
        Initial configuraiton of the problem.
    method: str
        Search method to be used

    Raises
    ------
    NotImplementedError:
        If the provided search method is not implemented.
    """

    if method == "bfs":
        final_node = bfs(initial_state)
        if not final_node is None:
            final_node.print_solution()
        else:
            print("No solution was found :(")
    else:
        raise NotImplemented(f"{method} is not currently implemented")

def main():
    initial_state = State(3, 3, 0, 0)

    print("Initial state: ", initial_state)
    search(initial_state, "bfs")

if __name__ == "__main__":
    main()

