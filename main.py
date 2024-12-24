import json
from tkinter import Canvas, Tk, Entry, font, Label, Button
import random

window = Tk()
window.title("Speed Test App")
score = 0
# Word List
with open("word_list") as file:
    word_list = json.load(file)
    word_list = word_list["commonWords"]


def timer(second):
    global window_timer
    if second > 0:
        second_label.config(text=f"{second}")
        window_timer = window.after(1000, timer, second - 1)
    else:
        second_label.config(text="Time's up!")
        label.config(text=f"Your speed is {score} wpm", font=font.Font(size=30), fg="#8D0B41")
        user_input.unbind("<space>")


def start(event):
    global random_word
    random_word = random_word_gen()
    timer(5)
    user_input.unbind("<Return>")


def random_word_gen():
    r = random.choice(word_list)
    label.config(text=r)
    return r


# Making the space key function
def submit(event):
    global random_word, score
    entered_word = user_input.get()
    entered_word = entered_word.lower()
    if entered_word == random_word:
        label.config(fg="green")
        score += 1
    else:
        label.config(fg="red")
    random_word = random_word_gen()
    user_input.delete(0, "end")
    return "break"


def reset():
    global score, random_word, window_timer
    if window_timer:
        window.after_cancel(window_timer)
    timer(10)
    score = 0
    user_input.delete(0, "end")
    label.config(fg="#8D0B41", font=("arial", 45, "bold"))
    random_word = random_word_gen()
    user_input.bind("<space>", submit)


# Making the canvas
canvas = Canvas(height=600, width=600, bg="#FFF8E6")
canvas.grid(column=0, row=0)
# Making the title of the game
canvas.create_text(300, 60, text="Typing Speed Test ", font=("Parkinsans", 32, "bold"), fill="#D39D55")
# Making the entry bar
user_input = Entry(window, width=20, bg="#D6CFB4", highlightthickness=0, borderwidth=0, font=font.Font(size=18))
canvas.create_window(300, 400, window=user_input)
user_input.focus()
# Binding the input bar to the space key
user_input.bind("<space>", submit)
user_input.bind("<Return>", start)
# Creating the word label
label = Label(text="Enter to start", font=("arial", 45, "bold"), fg="#8D0B41", bg="#FFF8E6")
canvas.create_window(300, 270, window=label)
# Making the timer label
second_label = Label(text="60", fg="red", font=("arial", 25, "normal"), bg="#FFF8E6")
canvas.create_window(300, 165, window=second_label)
# Making the reset btn
btn = Button(text="Reset", font=("arial", 12, "bold"), bg="#A5BFCC", command=reset)
canvas.create_window(300, 450, window=btn)
# Making the guide not
canvas.create_text(200, 550, text="*After typing each word, hit space btn to submit", font=("Parkinsans", 12, "normal"))
window.mainloop()
