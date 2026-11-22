
import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "Who developed Python?",
        "options": ["James Gosling", "Guido van Rossum",
                    "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores multiple values?",
        "options": ["int", "float", "list", "bool"],
        "answer": "list"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which function displays output?",
        "options": ["input()", "print()", "show()", "display()"],
        "answer": "print()"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["if", "while", "for", "switch"],
        "answer": "for"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["*", "**", "//", "%"],
        "answer": "**"
    },
    {
        "question": "Which keyword is used for a condition?",
        "options": ["if", "for", "def", "import"],
        "answer": "if"
    },
    {
        "question": "Which function takes input from the user?",
        "options": ["print()", "input()", "scan()", "get()"],
        "answer": "input()"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [".java", ".cpp", ".py", ".html"],
        "answer": ".py"
    }
]

# Variables
current_question = 0
score = 0

# Check Answer
def check_answer():
    global score

    selected = selected_option.get()

    if selected == "":
        messagebox.showwarning("Warning", "Please select an option!")
        return

    correct = questions[current_question]["answer"]

    if selected == correct:
        score += 1
        messagebox.showinfo("Result", "Correct Answer!")
    else:
        messagebox.showinfo(
            "Result", f"Wrong Answer!\nCorrect Answer: {correct}"
        )

    next_button.config(state="normal")
    submit_button.config(state="disabled")

# Next Question
def next_question():
    global current_question

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_result()

# Display Question
def show_question():
    selected_option.set("")
    submit_button.config(state="normal")
    next_button.config(state="disabled")

    q = questions[current_question]

    question_label.config(
        text=f"Question {current_question + 1}/10\n\n{q['question']}"
    )

    for i in range(4):
        option_buttons[i].config(text=q["options"][i],
                                 value=q["options"][i])

# Final Result
def show_result():
    question_label.config(
        text=f"Quiz Completed!\n\nYour Score: {score}/10"
    )

    for button in option_buttons:
        button.pack_forget()

    submit_button.pack_forget()
    next_button.pack_forget()

    restart_button.pack(pady=20)

# Restart Quiz
def restart_quiz():
    global current_question, score

    current_question = 0
    score = 0

    for button in option_buttons:
        button.pack(anchor="w", padx=40, pady=5)

    submit_button.pack(pady=10)
    next_button.pack(pady=10)
    restart_button.pack_forget()

    show_question()

# Main Window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("550x500")
root.configure(bg="#eaf2f8")
selected_option = tk.StringVar(master=root)

# Heading
heading = tk.Label(
    root, text="PYTHON QUIZ APPLICATION",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8", fg="#154360"
)
heading.pack(pady=20)

# Question Label
question_label = tk.Label(
    root, text="", font=("Arial", 15, "bold"),
    bg="#eaf2f8", wraplength=450
)
question_label.pack(pady=20)

# Options
option_buttons = []

for i in range(4):
    rb = tk.Radiobutton(
        root, text="", variable=selected_option,
        value="", font=("Arial", 12),
        bg="#eaf2f8", anchor="w"
    )
    rb.pack(anchor="w", padx=40, pady=5)
    option_buttons.append(rb)

# Submit Button
submit_button = tk.Button(
    root, text="Submit Answer",
    command=check_answer,
    bg="#2874a6", fg="white",
    font=("Arial", 12, "bold")
)
submit_button.pack(pady=10)

# Next Button
next_button = tk.Button(
    root, text="Next Question",
    command=next_question,
    state="disabled",
    bg="#239b56", fg="white",
    font=("Arial", 12, "bold")
)
next_button.pack(pady=10)

# Restart Button
restart_button = tk.Button(
    root, text="Restart Quiz",
    command=restart_quiz,
    bg="#d35400", fg="white",
    font=("Arial", 12, "bold")
)

show_question()

root.mainloop()
