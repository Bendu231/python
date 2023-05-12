from tkinter import*
from gTTs import gTTS
from playsound import playsound
import random

# ran_num = random.radiant(1, 50)
# chances = 5
root = Tk()
root.configure(bg='gray')
root.title("welcome to JEB guessing game")

ran_num = random.randint(1, 50)
chances = 5

while(chances>0):
    user_guess=int(input("please guess a number"))
    if (user_guess>ran_num):
        print(user_guess,"too high")
        chances-=1
        print("you have", chances, "chance(s)")
    elif (user_guess<ran_num):
        print(user_guess, "too low")
        chances-=1
        print("you have", chances, "chance(s)")


Label(root, text ="Guessing game", font = 'arial 15 bold', bg ='gray').pack()
# print = int(input("please guess a number:"))

msg = StringVar()
Label(root, text ="Enter Text", front = 'arial 15 bold"', bg ='gray'). place(x=20, y = 60)

Entry_field = Entry(root, textvariable= msg , width ='50')
Entry_field.place(x=20, Y=100)
# user_guess = Entry_field.get
# speech = gTTS()

def JEBguessing():
   message = Entry_field.get()
speech =  gTTS(text=user_guess)
speech_save = ('speech.mp3')
playsound('speech.mp3')


# def submit():
#     root.submit("")

def exit():
    root.destroy("")
def Reset():
    root.reset("")


Button(root,"submit guess", font = "arial 15 bold", command =submit, width= '5'). place(x=100, y=140)
#Button(root,text="Reset", font = "arial 15 bold", command = "Reset", width='5').place(x=100, y=140)
#Button(root, text = "PLAY", font = 'arial 15 bold', command = "JEB guessing", width = '4').place(x =25, y=140)
Button(root,text = 'Exit', font = 'arial 14 bold',command = 'Exit', width ='4', bg = 'orangered1').place(x=10, y=140)