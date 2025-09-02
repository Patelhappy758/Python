import tkinter as tk
import random
import time

OPERATERS = ['+', '-', '*', '//']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_CHALLENGES = 5

class MathChallengeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Challenges")
        self.challenge_num = 0
        self.right = 0
        self.wrong = 0
        self.start_time = None
        self.challenges = []
        self.answers = []
        self.current_answer = None

        self.label = tk.Label(root, text="Press Start to begin!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.config(state='disabled')

        self.button = tk.Button(root, text="Start", font=("Arial", 14), command=self.start_game)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def generate_challenge(self):
        operand1 = random.randint(MIN_OPERAND, MAX_OPERAND)
        operand2 = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(OPERATERS)
        expr = f"{operand1} {operator} {operand2}"
        answer = eval(expr)
        return expr, answer

    def start_game(self):
        self.challenge_num = 0
        self.right = 0
        self.wrong = 0
        self.challenges = []
        self.answers = []
        self.result_label.config(text="")
        self.button.config(text="Submit", command=self.check_answer)
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.start_time = time.time()
        self.next_challenge()

    def next_challenge(self):
        if self.challenge_num < TOTAL_CHALLENGES:
            expr, answer = self.generate_challenge()
            self.challenges.append(expr)
            self.answers.append(answer)
            self.current_answer = answer
            self.label.config(text=f"Challenge {self.challenge_num+1}: {expr} = ?")
            self.entry.delete(0, tk.END)
            self.challenge_num += 1
        else:
            self.end_game()

    def check_answer(self):
        guess = self.entry.get()
        if guess == str(self.current_answer):
            self.result_label.config(text="Correct!", fg="green")
            self.right += 1
            self.root.after(1000, self.next_challenge)
        else:
            self.result_label.config(text=f"Wrong! The answer was {self.current_answer}", fg="red")
            self.wrong += 1
            self.root.after(1000, self.next_challenge)

    def end_game(self):
        elapsed_time = time.time() - self.start_time
        self.label.config(text="Game Over!")
        self.entry.config(state='disabled')
        self.button.config(text="Restart", command=self.start_game)
        self.result_label.config(
            text=f"You got {self.right} right and {self.wrong} wrong out of {TOTAL_CHALLENGES}.\n"
                 f"Time: {elapsed_time:.2f} seconds."
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = MathChallengeApp(root)
    root.mainloop()