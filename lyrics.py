import curses
import time

# Sample lyrics (you can replace with any lyrics you want)
lyrics = [
    
    ("Maybe I like this roller coaster",1),
    ("Maybe it keeps me high",1.25),
    ("Maybe the speed, it brings me closer",1),
    ("I could sparkle up your eye",1.38),

    ("Hit me and tell me you're mine",1.50),
    ("I don't know why, but i like it",1.50),
    ("Scary, my God, you're divine",1.50),
    ("Gimme them, gimme them, dope and diamonds",1.20),

    ("Diet Mountain Dew, baby, New York City",1),
    ("Never was there ever a girl so pretty",1),
    ("Do you think we'll be in love forever?",1.25),
    ("Do you think we'll be in love?",1.25),
    ("Diet Mountain Dew, baby, New York City",1.25),
    ("Can we get it now, low down and gritty?",1.05),
    ("Do you think we'll be in love forever?",1),
    ("Do you think we'll be in love?",1.25),
   

]

# Delay between characters (seconds)
char_delay = 0.05  
 

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    height, width = stdscr.getmaxyx()
    
    for line,delay in lyrics:
        # Center text horizontally
        x = (width // 2) - (len(line) // 2)
        y = height // 2
        
        # Typewriter effect for each line
        for i, ch in enumerate(line):
            stdscr.addstr(y, x + i, ch)
            stdscr.refresh()
            time.sleep(char_delay)

        # Wait before showing next line
        time.sleep(delay)
        stdscr.clear()

    stdscr.refresh()
    time.sleep(2)

curses.wrapper(main)
