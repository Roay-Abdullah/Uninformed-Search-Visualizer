# Uninformed Search Algorithms Visualizer

An interactive Python-based visualization tool designed to demonstrate how various **Uninformed Search Algorithms** navigate a grid-based environment to find a path from a start point to a target.

## 🚀 Features

* **Real-time Visualization:** Watch the frontier expand and nodes get explored in real-time.
* **Multiple Algorithms:** Includes implementations for:
* **BFS** (Breadth-First Search)
* **DFS** (Depth-First Search)
* **UCS** (Uniform Cost Search) - featuring randomized path costs.
* **DLS** (Depth-Limited Search)
* **IDDFS** (Iterative Deepening Depth-First Search)
* **Bidirectional Search** - searching from both start and goal simultaneously.


* **Interactive UI:** Sidebar controls to switch algorithms and clear the board.
* **Obstacle Handling:** Includes static "walls" that the algorithms must navigate around.

---

## 🛠️ Prerequisites & Installation

### 1. Python

Ensure you have **Python 3.x** installed on your system. You can check your version by running:

```bash
python --version

```

### 2. Dependencies

This project uses **Tkinter**, which is Python’s built-in GUI library.

* **Windows/macOS:** Tkinter comes pre-installed with Python.
* **Linux (Ubuntu/Debian):** If not present, install it via:
```bash
sudo apt-get install python3-tk

```


## 🏃 How to Run

1. **Clone the Repository:**
```bash
git clone https://github.com/Roay-Abdullah/Uninformed-Search-Visualizer.git
cd Uninformed-Search-Visualizer

```


2. **Run the Application:**
```bash
python uninformedVisualizer.py

```



---

## 📖 How to Use

1. **Select Algorithm:** Use the dropdown menu in the right-hand sidebar to choose a search strategy.
2. **Run Search:** Click the **RUN SEARCH** button to begin the visualization.
3. **Understanding the Colors:**
* 🟩 **Green:** Start Position
* 🟦 **Blue:** Target Position
* ⬛ **Black:** Static Obstacles (Walls)
* 🟨 **Yellow:** Frontier (Nodes currently in the queue/stack)
* 🟧 **Light Orange:** Explored Nodes
* 🟪 **Purple:** Final Path found by the algorithm


4. **Clear:** Use the **Clear Path Only** button to reset the grid for a new run.

---

## 📂 Project Structure

* `main.py`: The core script containing the Tkinter GUI logic and algorithm implementations.
* `README.md`: Project documentation and setup instructions.

---

### 🤝 Contributing

Feel free to fork this project, submit PRs, or suggest new algorithms (like A* or Greedy Best-First Search) to be added to the visualizer!
