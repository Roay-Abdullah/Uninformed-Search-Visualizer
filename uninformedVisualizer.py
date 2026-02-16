import tkinter as tk
from tkinter import ttk, messagebox
import collections
import heapq
import random
import time

GRID_SIZE = 10 
CELL_SIZE = 60
DELAY = 0.05

class AIPathfinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Uninformed Algos Visualizer") 
        
        #Sidebar for controls and status
        self.sidebar = tk.Frame(root, width=200, bg="#f0f0f0", padx=10, pady=10)
        self.sidebar.pack(side="right", fill="y")
        self.setupSidebar()

        self.canvas = tk.Canvas(root, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, bg="white")
        self.canvas.pack(side="left")

        # State and Static Obstacles
        self.staticObstacles = {(2, 2), (2, 3), (2, 4), (5, 7), (6, 7), (7, 7), (4, 4), (4, 5)} 
        self.startPos = (1, 1)
        self.targetPos = (8, 8)
        self.nodeStatus = {} # Tracks yellow nodes and expansion order
        self.exploredCount = 0
        self.isRunning = False
        
        # Path Costs for UCS
        self.weights = [[random.randint(1, 10) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        
        self.render()

    def setupSidebar(self):
        tk.Label(self.sidebar, text="Algorithm:", bg="#f0f0f0").pack(anchor="w")
        self.algoVar = tk.StringVar(value="BFS")
        self.algoCombo = ttk.Combobox(self.sidebar, textvariable=self.algoVar, state="readonly")
        self.algoCombo['values'] = ("BFS", "DFS", "UCS", "DLS", "IDDFS", "Bidirectional")
        self.algoCombo.pack(fill="x", pady=5)

        tk.Button(self.sidebar, text="RUN SEARCH", bg="black", fg="white", font=('Arial', 10, 'bold'), command=self.executeSearch).pack(fill="x", pady=10)  
        tk.Button(self.sidebar, text="Clear Path Only", command=self.clearVisualization).pack(fill="x", pady=2)
        
        self.statusLabel = tk.Label(self.sidebar, text="Status: Ready", bg="#f0f0f0", fg="blue")
        self.statusLabel.pack(pady=20)

    def render(self, path=None):
        self.canvas.delete("all")
        currentAlgo = self.algoVar.get()
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = "white"
                text = ""
                
                if (row, col) in self.nodeStatus:
                    statusData = self.nodeStatus[(row, col)]
                    status = statusData[0] if isinstance(statusData, tuple) else statusData
                    
                    if status == 'explored':
                        color = "#ffcc66" # Explored color
                       
                        if currentAlgo == "UCS" and isinstance(statusData, tuple):
                            text = str(statusData[1])
                    elif status == 'frontier': 
                        color = "yellow" # Frontier color

                if (row, col) in self.staticObstacles: 
                    color = "black" # Static walls
                if path and (row, col) in path:
                    color = "purple" # Final path
                if (row, col) == self.startPos: 
                    color = "green"
                if (row, col) == self.targetPos: 
                    color = "blue"

                x1, y1 = col * CELL_SIZE, row * CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x1+CELL_SIZE, y1+CELL_SIZE, fill=color, outline="#ddd")
                if text: 
                    self.canvas.create_text(x1+30, y1+30, text=text, font=("Arial", 12))
        self.root.update()

    def getNeighbors(self, row, col):
        # Clockwise Order: Up, Right, Bottom, Bottom-Right, Left, Top-Left 
        directions = [(-1, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, -1)]
        res = []
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and (nr, nc) not in self.staticObstacles:
                res.append((nr, nc))
        return res

    def executeSearch(self):
        if self.isRunning: 
            return
        self.clearVisualization()
        self.isRunning = True
        self.exploredCount = 0
        algo = self.algoVar.get()
        path = None

        if algo == "BFS":
            path = self.bfs() 
        elif algo == "DFS": 
            path = self.dfs() 
        elif algo == "UCS":
            path = self.ucs()
        elif algo == "DLS": 
            path = self.dls(self.startPos, self.targetPos, 12) 
        elif algo == "IDDFS": 
            path = self.iddfs() 
        elif algo == "Bidirectional": 
            path = self.bidirectional() 
        
        if path: 
            self.render(path)
        else: 
            messagebox.showinfo("Search", "Goal Not Found!")
        self.isRunning = False


    def bfs(self): 
        q = collections.deque([(self.startPos, [self.startPos])])
        visited = {self.startPos}

        while q:
            curr, path = q.popleft()

            if curr == self.targetPos:
                return path
            self.nodeStatus[curr] = 'explored'

            for n in self.getNeighbors(*curr):
                if n not in visited:
                    visited.add(n); self.nodeStatus[n] = 'frontier' 
                    q.append((n, path + [n]))
            self.render()
            time.sleep(DELAY)
        return None


    def ucs(self): 
        pq = [(0, self.startPos, [self.startPos])]
        visited = {}

        while pq:
            cost, curr, path = heapq.heappop(pq)

            if curr in visited and visited[curr] <= cost: 
                continue
            visited[curr] = cost

            if curr == self.targetPos: 
                return path
            self.exploredCount += 1
            self.nodeStatus[curr] = ('explored', self.exploredCount)

            for n in self.getNeighbors(*curr):
                self.nodeStatus[n] = 'frontier' 
                heapq.heappush(pq, (cost + self.weights[n[0]][n[1]], n, path + [n]))
            self.render()
            time.sleep(DELAY)
        return None


    def dls(self, start, goal, limit): 
        visited = set()

        def dfsRec(node, depth, path):
            if node == goal: 
                return path
            
            if depth >= limit: 
                return None
            self.nodeStatus[node] = 'explored'
            self.render()
            time.sleep(DELAY)
            visited.add(node)

            for n in self.getNeighbors(*node):
                if n not in visited:
                    self.nodeStatus[n] = 'frontier' # Show waiting node 
                    res = dfsRec(n, depth + 1, path + [n])
                    if res: 
                        return res
            return None
        return dfsRec(start, 0, [start])


    def iddfs(self): 
        for limit in range(GRID_SIZE * 3):
            self.nodeStatus.clear()
            path = self.dls(self.startPos, self.targetPos, limit)

            if path: 
                return path
        return None


    def bidirectional(self):
        forQ, bacQ = collections.deque([(self.startPos, [self.startPos])]), collections.deque([(self.targetPos, [self.targetPos])])
        forVis, bacVis = {self.startPos: [self.startPos]}, {self.targetPos: [self.targetPos]}

        while forQ and bacQ:
            forNode, forPath = forQ.popleft()
            self.nodeStatus[forNode] = 'explored'

            if forNode in bacVis:
                return forPath + bacVis[forNode][::-1][1:]
            
            for n in self.getNeighbors(*forNode):
                if n not in forVis:
                    forVis[n] = forPath + [n]
                    forQ.append((n, forVis[n]))
                    self.nodeStatus[n] = 'frontier'

            bacNode, bacPath = bacQ.popleft(); self.nodeStatus[bacNode] = 'explored'

            if bacNode in forVis:
                return forVis[bacNode] + bacPath[::-1][1:]
            
            for n in self.getNeighbors(*bacNode):
                if n not in bacVis:
                    bacVis[n] = bacPath + [n]
                    bacQ.append((n, bacVis[n]))
                    self.nodeStatus[n] = 'frontier'
            self.render(); time.sleep(DELAY)
        return None


    def dfs(self): 
        s = [(self.startPos, [self.startPos])]
        visited = {self.startPos}

        while s:
            curr, path = s.pop()
            self.nodeStatus[curr] = 'explored'

            if curr == self.targetPos:
                return path
            
            for n in self.getNeighbors(*curr):
                if n not in visited:
                    visited.add(n)
                    self.nodeStatus[n] = 'frontier' 
                    s.append((n, path + [n]))
            self.render()
            time.sleep(DELAY)
        return None

    def clearVisualization(self):
        self.nodeStatus.clear()
        self.exploredCount = 0
        self.render()

if __name__ == "__main__":
    root = tk.Tk() 
    app = AIPathfinder(root)
    root.mainloop()
