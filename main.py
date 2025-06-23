BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd

index = 0


def right_button():
    global  index
    if len(french_words) > 0 :
        front()
        french_words.append(french_words[0])
        french_words.pop(index)

        english_words.append(english_words[0])
        english_words.pop(index)


def wrong_button() :
    global index
    if len(french_words) > 0 :
        front()
        index += 1



my_window = Tk()
my_window.title("Flash Card Project")
my_window.config(bg=BACKGROUND_COLOR)

back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
image = PhotoImage(file="images/card_front.png")

my_canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
my_image = my_canvas.create_image(400,263,image=image)
my_canvas.grid(row=0,column=0,columnspan=2,pady=20,padx=20)

italic_text = my_canvas.create_text(400,150,text="Language",font=("arial",40,"italic"))
bold_text = my_canvas.create_text(400,263,text="Word",font=("arial",60,"bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=right_button)
right_button.grid(row=1,column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR,highlightthickness=0,command=wrong_button)
wrong_button.grid(row=1,column=1)
#
data = pd.read_csv("data/french_words.csv")
french_words = list(data["French"])
english_words = list(data["English"])



def front() :
    global index
    my_canvas.itemconfig(my_image, image=front_image)
    my_canvas.image = front_image
    my_canvas.itemconfig(italic_text, text="english")
    my_canvas.itemconfig(bold_text,text=english_words[index])
    my_window.after(3000,back)


def back() :
    global index
    my_canvas.itemconfig(my_image,image=back_image)
    my_canvas.image = back_image
    my_canvas.itemconfig(italic_text,text="french")
    my_canvas.itemconfig(bold_text,text=french_words[index-1])




my_window.mainloop()
