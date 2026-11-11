# 3-coloring-graph-algorithm
This is a OES Python IV algorithm

A PyGame visualization of graph 3-coloring using backtracking.
The animation shows color assignments and reversals on a random connected graph.

## Setup

Tested with Python 3.13. Create a virtual environment in the project folder.

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `py -3.13 -m venv .venv` and activate it with
`.venv\Scripts\activate` in Command Prompt.

## Run

```bash
python main.py
```

The default graph has 8 nodes and 12 edges. Change `RandGraph(8, 12)` in
`main.py` to choose another size. Each animation step lasts 500 milliseconds.
Close the window to exit.

## Files

- `main.py` generates a graph and starts the animation.
- `graph_generator.py` contains `UnionFind` and `RandGraph(n, m)`.
- `coloring.py` contains `Color(G)`, which returns a color dictionary or `None`.
- `visualizer.py` contains `Visualize(G, coloring=None)` for a static view
  and `Animation(G)` for playback of the search.
- `requirements.txt` lists the tested dependency versions.

To display the final coloring instead of the animation, use these imports and
calls in `main.py`.

```python
from graph_generator import RandGraph
from coloring import Color
from visualizer import Visualize


def main():
    G = RandGraph(8, 12)
    coloring = Color(G)
    print("Coloring:", coloring)
    Visualize(G, coloring)


if __name__ == "__main__":
    main()
```

Calling `Visualize(G)` displays the graph with white node interiors.

## How it works

The generator samples exactly `m` edges and uses Union-Find to check connectivity.
It retries until the graph is connected. Valid inputs have `n >= 1` and
`n - 1 <= m <= n * (n - 1) // 2`.

The solver tries colors 1, 2, and 3 in vertex order, checking adjacent vertices
before each assignment. When a choice fails, it removes that color and tries
another. Animation saves a copy of the colors after each assignment and reversal,
then plays those snapshots in PyGame.

Use small graphs for demonstrations. Sparse graphs can require many generation
attempts. Backtracking can take exponential time, and animation stores every step
before opening its window, so large searches can take substantial time and memory.
