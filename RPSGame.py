from tkinter import *
import random

root = Tk()
root.geometry('400x400')

root.title('GHITA OUARZI-Rock, Paper, Scissors')
root.config(bg='pink')

Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='yellow').pack()

user_take = StringVar()
Label(root, text='Choose any one: rock, paper, scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)

Result = StringVar()

def play():
    user_pick = user_take.get().lower()  # Convert to lowercase for case-insensitive comparison
    comp_pick = random.choice(['rock', 'paper', 'scissors'])  # Generate a new random choice each time

    if user_pick == comp_pick:
        Result.set('Tie, you both selected the same')
    elif (user_pick == 'rock' and comp_pick == 'paper') or (user_pick == 'paper' and comp_pick == 'scissors') or (user_pick == 'scissors' and comp_pick == 'rock'):
        Result.set(f'You lose, computer selected {comp_pick}')
    elif (user_pick == 'rock' and comp_pick == 'scissors') or (user_pick == 'paper' and comp_pick == 'rock') or (user_pick == 'scissors' and comp_pick == 'paper'):
        Result.set(f'You win, computer selected {comp_pick}')
    else:
        Result.set('Invalid: Choose rock, paper, or scissors')

def Reset():
    Result.set("")
    user_take.set("")

def Exit():
    root.destroy()

# Display the result using a Label instead of an Entry
Label(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

root.mainloop()