import curses
from curses import wrapper
import queue
import time

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

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)

def find_start(maze,start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
            
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze,start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze,stdscr,path)
        stdscr.refresh()
        time.sleep(0.5)

        if maze[row][col] == end:
            return path
        
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

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)
    find_path(maze,stdscr)
    stdscr.getch()


wrapper(main)

