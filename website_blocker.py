from tkinter import *
from tkinter import ttk
import tkinter.font as font

# Create main window
window = Tk()
window.geometry('650x400')
window.minsize(650, 400)
window.maxsize(650, 400)
window.title("🌸 Cute Website Blocker created by GHITA🌸")
window.configure(bg="#f0f8ff")  # Soft pinkish white background

# Custom fonts
title_font = font.Font(family="Comic Sans MS", size=20, weight="bold")
label_font = font.Font(family="Comic Sans MS", size=12)
button_font = font.Font(family="Comic Sans MS", size=10, weight="bold")

# Heading with color
heading = Label(
    window, 
    text='Website Blocker', 
    font=title_font,
    bg="#f0f8ff",
    fg="#ff69b4"  # Hot pink
)
heading.pack(pady=20)

# Host file path and IP
host_path = r'C:\Windows\System32\drivers\etc\hosts'  # Raw string to avoid issues
ip_address = '127.0.0.1'

# Input section
label1 = Label(
    window, 
    text='Enter Website(s) (comma-separated):', 
    font=label_font,
    bg="#f0f8ff",
    fg="#4682b4"  # Steel blue
)
label1.place(x=5, y=100)

# Styled text input
enter_Website = Text(
    window,
    font=label_font,
    height=2, 
    width=40,
    bd=2,
    relief=GROOVE,
    bg="white",
    fg="#333333"
)
enter_Website.place(x=140, y=100)

# Status label (reusable instead of creating new ones)
status_label = Label(
    window, 
    text='', 
    font=label_font,
    bg="#f0f8ff"
)
status_label.place(x=200, y=220)

def Blocker():
    website_lists = enter_Website.get(1.0, END).strip()  # Remove extra spaces/newlines
    if not website_lists:
        status_label.config(text="⚠️ Please enter a website!", fg="#ff4500")
        return

    websites = [web.strip() for web in website_lists.split(",") if web.strip()]
    
    try:
        with open(host_path, 'r+') as host_file:
            file_content = host_file.read()
            blocked = False
            
            for web in websites:
                if web in file_content:
                    status_label.config(text=f"😌 {web} is already blocked!", fg="#9370db")
                else:
                    host_file.write(f"{ip_address} {web}\n")
                    status_label.config(text=f"✅ {web} blocked successfully!", fg="#32cd32")
                    blocked = True
            
            if not blocked and len(websites) > 1:
                status_label.config(text="😌 All sites already blocked!", fg="#9370db")
    
    except PermissionError:
        status_label.config(text="❌ Run as Administrator!", fg="#ff0000")
    except Exception as e:
        status_label.config(text=f"❌ Error: {str(e)}", fg="#ff0000")

def Unblock():
    website_lists = enter_Website.get(1.0, END).strip()
    if not website_lists:
        status_label.config(text="⚠️ Please enter a website!", fg="#ff4500")
        return

    websites = [web.strip() for web in website_lists.split(",") if web.strip()]
    
    try:
        with open(host_path, 'r+') as host_file:
            lines = host_file.readlines()
            host_file.seek(0)
            host_file.truncate()
            unblocked = False

            for line in lines:
                # Keep line if it doesn't contain any of the websites
                if not any(web in line for web in websites):
                    host_file.write(line)
                else:
                    unblocked = True

            if unblocked:
                status_label.config(text="✅ Sites unblocked successfully!", fg="#32cd32")
            else:
                status_label.config(text="😌 Sites not blocked!", fg="#9370db")
    
    except PermissionError:
        status_label.config(text="❌ Run as Administrator!", fg="#ff0000")
    except Exception as e:
        status_label.config(text=f"❌ Error: {str(e)}", fg="#ff0000")

# Styled buttons
block_button = Button(
    window, 
    text='Block 🔒',
    font=button_font,
    pady=5,
    command=Blocker,
    width=10,
    bg="#ffb6c1",  # Light pink
    activebackground="#ff69b4",
    relief=RAISED,
    bd=3
)
block_button.place(x=200, y=180)

unblock_button = Button(
    window, 
    text='Unblock 🔓',
    font=button_font,
    pady=5,
    command=Unblock,
    width=10,
    bg="#87cefa",  # Light blue
    activebackground="#4682b4",
    relief=RAISED,
    bd=3
)
unblock_button.place(x=350, y=180)

# Decorative elements
decor1 = Label(window, text="✨", font=("Arial", 20), bg="#f0f8ff", fg="#ffd700")
decor1.place(x=50, y=300)

decor2 = Label(window, text="✨", font=("Arial", 20), bg="#f0f8ff", fg="#ffd700")
decor2.place(x=580, y=300)

window.mainloop()