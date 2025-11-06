# import some packages
from tkinter import *
import pyttsx3

root = Tk()
root.geometry("350x300")
root.configure(bg='pink')
root.configure(bg='pink')
root.title("GHITA - TEXT TO SPEECH")

Label(root, text="TEXT_TO_SPEECH", font="arial 20 bold", bg='pink').pack()
Label(text="GHITA OUARZI", font='arial 10 bold', bg='pink', width='20').pack(side='bottom')

Msg = StringVar()
Label(root, text="Enter Text", font='arial 15 bold', bg='pink').place(x=20, y=60)

entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

def Text_to_speech():
    Message = entry_field.get()
    engine.say(Message)
    engine.runAndWait() # Blocks until speech is complete

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width='4', bg='blue').place(x=25, y=140)

Button(root, font='arial 15 bold', text='EXIT', width='4', command=Exit, bg='red').place(x=100, y=140)

Button(root, font='arial 15 bold', text='RESET', width='6', command=Reset, bg='green').place(x=175, y=140)

root.mainloop()