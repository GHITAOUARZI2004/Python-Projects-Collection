from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
# Soft pink background
clock.config(bg="lightpink")
clock.title("GHITA OUARZI Alarm Clock")
clock.geometry("400x400")

# Updated label styles
time_format = Label(clock, text="Enter time in 24 hour format!", fg="deeppink", bg="mistyrose", font=("Arial", 10)).place(x=60, y=120)
addTime = Label(clock, text="Hour  Min   Sec", font=("Arial", 12), bg="lightcoral").place(x=110, y=10)

hour = StringVar()
min = StringVar()
sec = StringVar()

# Pink entry fields with a light border
hourTime = Entry(clock, textvariable=hour, bg="pink", width=15, highlightbackground="palevioletred", highlightthickness=1).place(x=110, y=40)
minTime = Entry(clock, textvariable=min, bg="pink", width=15, highlightbackground="palevioletred", highlightthickness=1).place(x=150, y=40)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15, highlightbackground="palevioletred", highlightthickness=1).place(x=200, y=40)

# Nicer button style
submit = Button(clock, text="Set Alarm", fg="white", bg="hotpink", width=10, command=actual_time, relief=RAISED, borderwidth=2).place(x=150, y=80)

clock.mainloop()