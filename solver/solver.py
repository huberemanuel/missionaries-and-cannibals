import argparse

from solver.state import State
from solver.search import bfs, dfs, idfs


def search(initial_state: State, method: str="bfs", max_depth: int=-1):
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
    elif method == "dfs":
        final_node = dfs(initial_state, max_depth)
    elif method == "idfs":
        final_node = idfs(initial_state)
    else:
        raise NotImplemented(f"{method} is not currently implemented")

    if not final_node is None:
        final_node.print_solution()
    else:
        print("No solution was found :(")

def main():
    parser = argparse.ArgumentParser("Resolução do problema dos missionários e canibais")
    parser.add_argument("method", type=str, help="Método de busca a ser utilizado, opções disponíveis (dfs,idfs,bfs")
    parser.add_argument("--max_depth", type=int, default=-1, help="Profundidade máxima para dfs")
    args = parser.parse_args()
    initial_state = State(3, 3, 0, 0)

    print("Initial state: ", initial_state)
    search(initial_state, args.method, args.max_depth)

if __name__ == "__main__":
    main()

