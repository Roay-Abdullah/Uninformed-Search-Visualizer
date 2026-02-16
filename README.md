# Uninformed Search Algorithms Visualizer

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)

Interactive **step-by-step visualizer** of classic uninformed (blind) search algorithms on a grid world, built with **Python** and **Tkinter**.

Perfect for students, educators, and anyone learning artificial intelligence search concepts.

https://github.com/YOUR-USERNAME/uninformed-search-visualizer

## Algorithms Included

| Algorithm              | Optimal | Complete | Uses              | Visual Features                              |
|------------------------|---------|----------|-------------------|----------------------------------------------|
| Breadth-First Search   | Yes     | Yes      | Queue             | Broad level-by-level expansion               |
| Depth-First Search     | No      | No¹      | Stack             | Deep, branching exploration                  |
| Uniform Cost Search    | Yes     | Yes      | Priority Queue    | Numeric cumulative cost displayed            |
| Depth-Limited Search   | No      | No       | Recursion + limit | Depth cutoff at 12                           |
| Iterative Deepening DFS| Yes     | Yes      | Iterative deepening | Gradually deeper attempts                  |
| Bidirectional Search   | Yes     | Yes      | Two queues        | Simultaneous forward + backward search       |

¹ With visited set (as implemented here) — avoids cycles but may not be complete in infinite spaces.

## Features

- 10×10 grid with static obstacles
- Start (green) at (1,1) • Goal (blue) at (8,8)
- **Yellow** = frontier nodes (in queue/stack)
- **Light orange** (#ffcc66) = explored/expanded nodes
- **Purple** = final reconstructed path
- UCS displays **path cost** on expanded nodes
- Real-time animation with adjustable `DELAY`
- Clean sidebar controls: algorithm selection, Run, Clear
- "Goal not found" message when no path exists

## Demo

*(Add a short GIF here once recorded — highly recommended)*

Example of BFS wavefront expanding:

<!-- Replace with your own GIF upload -->
<!-- ![BFS Demo](demo/bfs.gif) -->

## Requirements

- Python **3.8** or newer
- Tkinter (included in standard Python on Windows/macOS; on Linux: `sudo apt install python3-tk`)

No external pip packages required.

## Installation & Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Roay-Abdullah/Uninformed-Search-Visualizer.git
cd Uninformed-Search-Visualizer

# 2. (Optional) Create & activate virtual environment
python -m venv venv
source venv/bin/activate          # Linux/macOS
venv\Scripts\activate             # Windows
```

## Grid Configuration (February 2026)

- Size: 10 × 10
- Start: (1, 1)
- Goal:  (8, 8)
- Obstacles:
  (2,2) (2,3) (2,4)
  (4,4) (4,5)
  (5,7) (6,7) (7,7)
Random edge weights (1–10) are generated for UCS each run.

## Easy Customizations

Edit these lines in the code:

GRID_SIZE   = 12          # larger grid
CELL_SIZE   = 50
DELAY       = 0.02        # faster animation

self.startPos     = (0, 0)
self.targetPos    = (11, 11)

self.staticObstacles = {(3,3), (5,6), (7,2)}  # your own walls


## Project Structure

uninformed-search-visualizer/
├── main.py                 # main application (rename if needed)
├── README.md
└── (future: demo/           # GIFs & screenshots)

# 3. Run the visualizer
python main.py                    # or whatever you named the file
