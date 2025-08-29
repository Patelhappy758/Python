import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the Typing Speed Test!")
    stdscr.addstr(1, 0, "Press any key to start...")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current,wpm=0):
    stdscr.clear()
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) 
        if char != correct_char:
            color = curses.color_pair(2)
        
        stdscr.addstr(0, i, char, color)


def load_text():
    with open("sample_texts.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()
    
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  # Make getkey non-blocking

    while True:
        display_text(stdscr, target_text, current_text, wpm)
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC key to exit
            break

        if key == '\n':  # Enter key to finish
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        elapsed_time = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (elapsed_time / 60)) / 5)

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "Test completed! Press any key to restart or ESC to exit.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)



# To run this code, ensure you have the 'windows-curses' package installed if you're on Windows.

