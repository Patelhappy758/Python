import tkinter as tk
import random

COLORS = ["R", "G", "B", "Y", "O", "P"]
COLOR_NAMES = {"R": "Red", "G": "Green", "B": "Blue", "Y": "Yellow", "O": "Orange", "P": "Purple"}
TRIES = 10
CODE_LENGTH = 4

class ColorMatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("4-Color Match Game")
        self.code = self.generate_code()
        self.attempts = 0
        self.guess = []
        self.history = []

        self.info_label = tk.Label(root, text=f"Available colors: {', '.join([COLOR_NAMES[c] for c in COLORS])}", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.guess_frame = tk.Frame(root)
        self.guess_frame.pack(pady=5)
        self.guess_labels = [tk.Label(self.guess_frame, text="_", width=4, font=("Arial", 16), relief="ridge") for _ in range(CODE_LENGTH)]
        for lbl in self.guess_labels:
            lbl.pack(side=tk.LEFT, padx=2)

        self.color_buttons_frame = tk.Frame(root)
        self.color_buttons_frame.pack(pady=5)
        for color in COLORS:
            btn = tk.Button(self.color_buttons_frame, text=COLOR_NAMES[color], bg=self.get_color(color), width=8,
                            command=lambda c=color: self.add_color(c))
            btn.pack(side=tk.LEFT, padx=2)

        self.submit_btn = tk.Button(root, text="Submit Guess", command=self.submit_guess, state="disabled")
        self.submit_btn.pack(pady=5)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        self.history_frame = tk.Frame(root)
        self.history_frame.pack(pady=5)

    def get_color(self, code):
        return {
            "R": "#ff4d4d",
            "G": "#4dff4d",
            "B": "#4d4dff",
            "Y": "#ffff4d",
            "O": "#ffa64d",
            "P": "#b84dff"
        }[code]

    def generate_code(self):
        return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

    def add_color(self, color):
        if len(self.guess) < CODE_LENGTH:
            self.guess.append(color)
            self.guess_labels[len(self.guess)-1].config(text=COLOR_NAMES[color], bg=self.get_color(color))
        if len(self.guess) == CODE_LENGTH:
            self.submit_btn.config(state="normal")

    def submit_guess(self):
        self.attempts += 1
        correct_position, incorrect_position = self.check_code(self.guess, self.code)
        guess_str = " ".join([COLOR_NAMES[c] for c in self.guess])
        feedback = f"Attempt {self.attempts}: {guess_str}\nCorrect position: {correct_position}, Wrong position: {incorrect_position}"
        tk.Label(self.history_frame, text=feedback, font=("Arial", 10)).pack()
        self.guess = []
        for lbl in self.guess_labels:
            lbl.config(text="_", bg="SystemButtonFace")
        self.submit_btn.config(state="disabled")

        if correct_position == CODE_LENGTH:
            self.feedback_label.config(text="Congratulations! You've guessed the code correctly!", fg="green")
            self.submit_btn.config(state="disabled")
            for btn in self.color_buttons_frame.winfo_children():
                btn.config(state="disabled")
        elif self.attempts >= TRIES:
            code_str = " ".join([COLOR_NAMES[c] for c in self.code])
            self.feedback_label.config(text=f"Game Over! The code was: {code_str}", fg="red")
            self.submit_btn.config(state="disabled")
            for btn in self.color_buttons_frame.winfo_children():
                btn.config(state="disabled")
        else:
            self.feedback_label.config(text=f"Correct colors in correct position: {correct_position}\nCorrect colors in incorrect position: {incorrect_position}", fg="blue")

    def check_code(self, guess, real_code):
        color_counts = {}
        correct_position = 0
        incorrect_position = 0

        for color in real_code:
            color_counts[color] = color_counts.get(color, 0) + 1

        # First pass: correct positions
        for i in range(CODE_LENGTH):
            if guess[i] == real_code[i]:
                correct_position += 1
                color_counts[guess[i]] -= 1

        # Second pass: correct colors, wrong positions
        for i in range(CODE_LENGTH):
            if guess[i] != real_code[i] and color_counts.get(guess[i], 0) > 0:
                incorrect_position += 1
                color_counts[guess[i]] -= 1

        return correct_position, incorrect_position

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorMatchGame(root)
    root.mainloop()