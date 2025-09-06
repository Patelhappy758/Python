import tkinter as tk
import time
import threading
import queue

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "O", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", "#", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "X", "#", "#", "#", "#", "#", "#", "#", "#"]
]

CELL_SIZE = 40

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Pathfinding Visualization")
        self.canvas = tk.Canvas(root, width=len(maze[0])*CELL_SIZE, height=len(maze)*CELL_SIZE)
        self.canvas.pack()
        self.draw_maze()
        self.start_button = tk.Button(root, text="Start Pathfinding", command=self.start_pathfinding)
        self.start_button.pack(pady=10)

    def draw_maze(self, path=[]):
        self.canvas.delete("all")
        for i, row in enumerate(maze):
            for j, value in enumerate(row):
                x1, y1 = j*CELL_SIZE, i*CELL_SIZE
                x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
                color = "white"
                if value == "#":
                    color = "black"
                elif value == "O":
                    color = "blue"
                elif value == "X":
                    color = "red"
                if (i, j) in path:
                    color = "yellow"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
                if value in ("O", "X"):
                    self.canvas.create_text(x1+CELL_SIZE//2, y1+CELL_SIZE//2, text=value, font=("Arial", 16, "bold"), fill="white")

    def find_start(self, start):
        for i, row in enumerate(maze):
            for j, value in enumerate(row):
                if value == start:
                    return i, j
        return None

    def pathfinding(self):
        start = "O"
        end = "X"
        start_pos = self.find_start(start)
        q = queue.Queue()
        q.put((start_pos, [start_pos]))
        visited = set()
        while not q.empty():
            current_pos, path = q.get()
            row, col = current_pos
            self.draw_maze(path)
            self.root.update()
            time.sleep(0.2)
            if maze[row][col] == end:
                self.draw_maze(path)
                return
            neighbors = [
                (row-1, col), # up
                (row+1, col), # down
                (row, col-1), # left
                (row, col+1)  # right
            ]
            for neighbor in neighbors:
                r, c = neighbor
                if (0 <= r < len(maze)) and (0 <= c < len(maze[0])) and maze[r][c] != "#" and neighbor not in visited:
                    visited.add(neighbor)
                    q.put((neighbor, path + [neighbor]))

    def start_pathfinding(self):
        threading.Thread(target=self.pathfinding, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()