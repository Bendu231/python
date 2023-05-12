from tkinter import *
from gtts import gTTS
from playsound import playsound
import random

root = Tk()
root.configure(bg='gray')
root.title("Welcome to JEB guessing game")

ran_num = random.randint(1, 50)
chances = 5

def JEBguessing():
    user_guess = int(Entry_field.get())
    if user_guess > ran_num:
        result_label.config(text=f"{user_guess} is too high")
    elif user_guess < ran_num:
        result_label.config(text=f"{user_guess} is too low")
    else:
        result_label.config(text="Congratulations, you guessed it!")
    speech = gTTS(text=str(user_guess))
    speech.save('speech.mp3')
    playsound('speech.mp3')

Label(root, text="Guessing game", font='arial 15 bold', bg='gray').pack()

msg = StringVar()
Label(root, text="Enter Text", font='arial 15 bold', bg='gray').place(x=20, y=60)

Entry_field = Entry(root, textvariable=msg, width='50')
Entry_field.place(x=20, y=100)

submit_button = Button(root, text="Submit", font="arial 12 bold", command=JEBguessing, width='10')
submit_button.place(x=150, y=140)

reset_button = Button(root, text="Reset", font="arial 12 bold", command=lambda: Entry_field.delete(0, 'end'), width='10')
reset_button.place(x=280, y=140)

exit_button = Button(root, text='Exit', font='arial 12 bold', command=root.destroy, width='10', bg='orangered1')
exit_button.place(x=410, y=140)

result_label = Label(root, text="", font='arial 12 bold', bg='gray')
result_label.place(x=20, y=180)

root.mainloop()
