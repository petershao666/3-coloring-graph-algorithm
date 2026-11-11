from graph_generator import RandGraph
from visualizer import Animation


def main():
    G = RandGraph(8, 12)
    print("Graph:", G)
    Animation(G)


if __name__ == "__main__":
    main()
