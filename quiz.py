import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title(" Quiz Game")
        self.root.configure(bg="steelblue")

        self.questions = [
            # Add your questions here
             {
                "question": "Where is the headquarters of ISRO located?",
                "choices": ["Pune", "Bangalore", "Delhi", "Mumbai"],
                "correct_choice": "Bangalore"
            },
            {
                "question": "Which country shares the shortest border with India?",
                "choices": ["Nepal", "Bhutan", "Bangadesh", "Afghanistan"],
                "correct_choice": "Afghanistan"
            },
            {
                "question": "With reference to the Internet, what is the full form of IP?",
                "choices": ["Internet Protocol", "Intra propaganda", "Intra protocol", "Internet Proposal"],
                "correct_choice": "Internet Protocol"
            },
            {
                "question": "What is the launch date for Chandrayaan 3 mission?",
                "choices": ["24 July 2023", "13 July 2023", "15 July 2023", "14 July 2023"],
                "correct_choice": "14 July 2023"
            },
            {
                "question": "When is World Environment Day celebrated?",
                "choices": ["8th June", "5th June", "5th July", "6th June"],
                "correct_choice": "5th June"
            },
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Cambria  ", 16), bg="ivory3",pady=10,padx=50)
        self.question_label.pack(pady=30)

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Constantia", 12), bg="seashell3", activebackground="rosybrown",
                               command=lambda i=i: self.check_answer(i))
            self.choice_buttons.append(button)
            button.pack(pady=8, padx=60, fill="x")

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            choices = question_data["choices"]
            random.shuffle(choices)

            for i in range(4):
                self.choice_buttons[i].config(text=choices[i])

            self.current_question += 1
        else:
            self.show_results()

    def check_answer(self, chosen_index):
        chosen_answer = self.choice_buttons[chosen_index].cget("text")
        correct_answer = self.questions[self.current_question - 1]["correct_choice"]

        if chosen_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Your answer is incorrect. The correct answer is {correct_answer}.")

        self.next_question()

    def show_results(self):
        messagebox.showinfo("Quiz Completed", f"Your final score: {self.score}/{len(self.questions)}")
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.current_question = 0
            self.score = 0
            self.next_question()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    quiz_game = QuizGame(root)
    root.mainloop()
