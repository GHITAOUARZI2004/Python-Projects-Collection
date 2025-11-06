from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Create the main window
window = Tk()
window.title("Language Translator (GHITA)") 
window.minsize(700, 600)  # Slightly larger for better spacing
window.maxsize(700, 600)

# Set a soft pink background color (you can adjust the hex code for darker/lighter pink)
window.configure(bg="#FFD1DC")  # Soft pink hex code


# Define languages (more options for flexibility)
LANGUAGES = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Hindi': 'hi',
    'Chinese (Simplified)': 'zh-CN',
    'Japanese': 'ja',
    'Russian': 'ru',
    'Arabic': 'ar',
    'Italian': 'it',
    'Portuguese': 'pt'
}


def translate():
    try:
        input_text = text1.get(1.0, END).strip()
        if not input_text:
            messagebox.showinfo("Info", "Please enter text to translate!")
            return

        # Get selected languages
        src_lang_name = combo1.get()
        dest_lang_name = combo2.get()

        # Get language codes
        src_lang_code = LANGUAGES.get(src_lang_name)
        dest_lang_code = LANGUAGES.get(dest_lang_name)

        if not src_lang_code or not dest_lang_code:
            messagebox.showerror("Error", "Please choose valid languages!")
            return

        # Translate using Google Translate
        translated = GoogleTranslator(source=src_lang_code, target=dest_lang_code).translate(input_text)

        # Display result
        text2.delete(1.0, END)
        text2.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Translation Failed", f"Error: {str(e)}")


# Add a title label
title_label = Label(
    window, 
    text="Language Translator", 
    font=("Arial", 20, "bold"), 
    bg="#FFD1DC",  # Match window background
    fg="#8B008B"  # Dark magenta text (complements pink)
)
title_label.pack(pady=20)  # Add space above/below


# Frame for language dropdowns (to group them neatly)
lang_frame = Frame(window, bg="#FFD1DC")
lang_frame.pack(pady=10)

# Source language dropdown
Label(
    lang_frame, 
    text="From:", 
    font=("Arial", 12), 
    bg="#FFD1DC", 
    fg="#000000"
).grid(row=0, column=0, padx=10)

combo1 = ttk.Combobox(
    lang_frame, 
    values=list(LANGUAGES.keys()), 
    state='readonly',
    font=("Arial", 11),
    width=20
)
combo1.grid(row=0, column=1, padx=10)
combo1.set("English")  # Default source


# Target language dropdown
Label(
    lang_frame, 
    text="To:", 
    font=("Arial", 12), 
    bg="#FFD1DC", 
    fg="#000000"
).grid(row=0, column=2, padx=10)

combo2 = ttk.Combobox(
    lang_frame, 
    values=list(LANGUAGES.keys()), 
    state='readonly',
    font=("Arial", 11),
    width=20
)
combo2.grid(row=0, column=3, padx=10)
combo2.set("Spanish")  # Default target


# Frame for text boxes (input and output)
text_frame = Frame(window, bg="#FFD1DC")
text_frame.pack(pady=20)

# Input text box with pink border
f1 = Frame(
    text_frame, 
    bg="#FF69B4",  # Hot pink border
    bd=3  # Thicker border
)
f1.grid(row=0, column=0, padx=20)

text1 = Text(
    f1, 
    font=("Arial", 12), 
    bg="white", 
    wrap=WORD,
    height=10, 
    width=25,
    relief=FLAT  # No extra border (uses frame border)
)
text1.pack(padx=1, pady=1)  # Small padding inside the frame


# Output text box with pink border
f2 = Frame(
    text_frame, 
    bg="#FF69B4",  # Hot pink border
    bd=3
)
f2.grid(row=0, column=1, padx=20)

text2 = Text(
    f2, 
    font=("Arial", 12), 
    bg="white", 
    wrap=WORD,
    height=10, 
    width=25,
    relief=FLAT
)
text2.pack(padx=1, pady=1)


# Translate button with styling
translate_btn = Button(
    window, 
    text="Translate", 
    font=("Arial", 14, "bold"),
    bg="#FF69B4",  # Hot pink
    fg="white",    # White text
    padx=20,
    pady=5,
    command=translate,
    relief=RAISED,
    bd=2
)
translate_btn.pack(pady=20)


# Run the app
window.mainloop()