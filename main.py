from tkinter import *
import pandas
import random

# ________________Working________________ #
current_card = {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    raw_data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words_to_learn.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = raw_data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


def pop_card():
    data_dict.remove(current_card)
    print(len(data_dict))
    next_card()
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


# __________________UI__________________ #

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("French English")

flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 46, "bold"))

wrong_button = Button(height=100, width=99, image=wrong_image)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button = Button(height=100, width=99, image=right_image)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=pop_card)
right_button.grid(column=1, row=1)

next_card()



window.mainloop()
