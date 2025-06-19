import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    global number

    guess = guess_var.get()

    try:
        user_guess = int(guess)
        attempts += 1

        if user_guess < number:
            result_var.set("Too Low! Try Again.")
        elif user_guess > number:
            result_var.set("Too High! Try Again.")
        else:
            result_var.set(f"Great Job! You guessed it in {attempts} attempts.")
    except ValueError:
        result_var.set("Invalid Input! Enter a number.")

def reset_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    guess_var.set("")
    result_var.set("Game Reset. Guess a new number!")

root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

font_label = ("Arial", 12)
font_result = ("Arial", 12, "bold")

tk.Label(root, text="I'm thinking of a number between 1 and 100", font=font_label, bg="#f0f0f0").pack(pady=10)

guess_var = tk.StringVar()
tk.Entry(root, textvariable=guess_var, font=font_label, width=20).pack()

tk.Button(root, text="Submit Guess", command=check_guess, font=font_label, bg="#4caf50", fg="white", width=15).pack(pady=10)
tk.Button(root, text="Reset Game", command=reset_game, font=font_label, bg="#2196f3", fg="white", width=15).pack(pady=5)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=font_result, bg="#f0f0f0", justify="center").pack(pady=20)

root.mainloop()
