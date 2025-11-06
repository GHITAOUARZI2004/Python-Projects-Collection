from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow = Tk()
mainwindow.title('Text-to-Speech & Speech-to-Text Converter by GHITA')
mainwindow.geometry('600x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='#f0f0f0')  # Light gray background

def say(text1):
    if not text1.strip():  # Check for empty input
        showinfo("Warning", "Please enter text to convert")
        return
        
    language = 'en'
    try:
        speech = gTTS(text=text1, lang=language, slow=False)
        speech.save("text.mp3")
        os.system("start text.mp3")
    except Exception as e:
        showinfo("Error", f"Conversion failed: {str(e)}")

def recordvoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        showinfo("Info", "Please start speaking...")
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = r.listen(source, timeout=5)  # 5-second timeout
        
    try:
        text = r.recognize_google(audio, language="en-US")
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Request failed: {str(e)}"
    except:
        return "Recording timed out or error occurred"

def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter')
    texttospeechwindow.geometry("600x500")
    texttospeechwindow.configure(bg='#e6f7ff')  # Light blue background
    texttospeechwindow.resizable(0, 0)
    
    # Title
    Label(texttospeechwindow, text='Text-to-Speech Conversion', 
          font=("Segoe UI", 18, 'bold'), bg='#e6f7ff', fg='#1a5276').pack(pady=20)
    
    # Text input label
    Label(texttospeechwindow, text='Enter text to convert:', 
          font=("Segoe UI", 12), bg='#e6f7ff', fg='#34495e').place(x=50, y=100)
    
    # Text input frame
    text_frame = Frame(texttospeechwindow, bg='white', bd=2, relief=GROOVE)
    text_frame.place(x=50, y=130, width=500, height=150)
    
    # Text input area
    text = Text(text_frame, height=7, width=55, font=('Segoe UI', 12), 
                borderwidth=0, highlightthickness=0)
    text.pack(padx=5, pady=5)
    
    # Speak button
    speakbutton = Button(texttospeechwindow, text='Play Speech', 
                        font=('Segoe UI', 14), bg='#3498db', fg='white',
                        padx=20, pady=5, bd=0, relief=FLAT, overrelief=RIDGE,
                        command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=250, y=320)
    
    # Help text
    Label(texttospeechwindow, text='Tip: Enter text and click "Play Speech" to convert', 
          font=("Segoe UI", 10), bg='#e6f7ff', fg='#7f8c8d').place(x=150, y=420)

def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("600x500")
    speechtotextwindow.configure(bg='#fef5e7')  # Light orange background
    speechtotextwindow.resizable(0, 0)
    
    # Title
    Label(speechtotextwindow, text='Speech-to-Text Conversion', 
          font=("Segoe UI", 18, 'bold'), bg='#fef5e7', fg='#d35400').pack(pady=20)
    
    # Record button
    recordbutton = Button(speechtotextwindow, text='Start Recording', 
                         font=('Segoe UI', 14), bg='#e67e22', fg='white',
                         padx=20, pady=5, bd=0, relief=FLAT, overrelief=RIDGE)
    
    # Result label
    Label(speechtotextwindow, text='Recognition Result:', 
          font=("Segoe UI", 12), bg='#fef5e7', fg='#34495e').place(x=50, y=150)
    
    # Result frame
    text_frame = Frame(speechtotextwindow, bg='white', bd=2, relief=GROOVE)
    text_frame.place(x=50, y=180, width=500, height=150)
    
    # Result text area
    text = Text(text_frame, height=7, width=55, font=('Segoe UI', 12), 
                borderwidth=0, highlightthickness=0)
    text.pack(padx=5, pady=5)
    
    # Configure record button command
    recordbutton.config(command=lambda: text.insert(END, recordvoice() + "\n\n"))
    recordbutton.place(x=250, y=100)
    
    # Clear button
    clear_btn = Button(speechtotextwindow, text='Clear Content', 
                      font=('Segoe UI', 12), bg='#ecf0f1', fg='#34495e',
                      padx=10, pady=2, command=lambda: text.delete(1.0, END))
    clear_btn.place(x=450, y=350)
    
    # Help text
    Label(speechtotextwindow, text='Tip: Click "Start Recording" then speak (5-second timeout)', 
          font=("Segoe UI", 10), bg='#fef5e7', fg='#7f8c8d').place(x=120, y=420)

# Main window title
Label(mainwindow, text='Text & Speech Converter',
      font=('Segoe UI', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=50)

# Main window buttons
Button(mainwindow, text='Text to Speech', command=TextToSpeech,
       font=('Segoe UI', 14), bg='#2980b9', fg='white',
       width=20, height=1, bd=0, relief=FLAT, overrelief=RIDGE).place(x=200, y=180)

Button(mainwindow, text='Speech to Text', command=SpeechToText,
       font=('Segoe UI', 14), bg='#27ae60', fg='white',
       width=20, height=1, bd=0, relief=FLAT, overrelief=RIDGE).place(x=200, y=280)

# Footer info
Label(mainwindow, text='A simple yet powerful text-speech conversion tool',
      font=('Segoe UI', 10), bg='#f0f0f0', fg='#7f8c8d').place(x=150, y=420)

mainwindow.mainloop()