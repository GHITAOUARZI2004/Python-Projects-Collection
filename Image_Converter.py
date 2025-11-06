import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import tkinter.ttk as ttk

# Create main window
root = tk.Tk()
root.geometry('700x400')
root.title('Image Format Converter - GHITA')
root.resizable(False, False)  # Disable resizing

# Configure styles
style = ttk.Style()
style.theme_use('clam')  # Modern theme

# Custom colors
BG_COLOR = '#f0f0f0'
ACCENT_COLOR = '#4a90e2'
BUTTON_COLOR = '#5cb85c'
TEXT_COLOR = '#333333'
LABEL_COLOR = '#2c3e50'

root.configure(bg=BG_COLOR)

# Header frame
header_frame = tk.Frame(root, bg=ACCENT_COLOR, height=80)
header_frame.pack(fill=tk.X)

# Title label
title_label = tk.Label(
    header_frame,
    text='Image Format Converter',
    font=('Segoe UI', 20, 'bold'),
    bg=ACCENT_COLOR,
    fg='white',
    pady=20
)
title_label.pack()

# Subtitle
subtitle_label = tk.Label(
    root,
    text='Easily convert between popular image formats',
    font=('Segoe UI', 10),
    bg=BG_COLOR,
    fg=LABEL_COLOR,
    pady=10
)
subtitle_label.pack()

# Main content frame
content_frame = tk.Frame(root, bg=BG_COLOR, padx=50, pady=20)
content_frame.pack(expand=True, fill=tk.BOTH)

# Store image in a mutable object
image_data = {"img": None, "path": ""}

def browse():
    try:
        filename = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if not filename:
            return
            
        image_data["img"] = Image.open(filename)
        image_data["path"] = filename
        # Show selected file name
        file_label.config(text=f"Selected: {filename.split('/')[-1]}", fg=LABEL_COLOR)
        messagebox.showinfo("Success", "Image loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {str(e)}")
        image_data["img"] = None
        image_data["path"] = ""
        file_label.config(text="No image selected")

def convert(to_format):
    if image_data["img"] is None:
        messagebox.showwarning("Warning", "Please browse and select an image first!")
        return
        
    try:
        ext = f".{to_format}"
        export_path = filedialog.asksaveasfilename(
            defaultextension=ext,
            filetypes=[(f"{to_format.upper()} Files", f"*{ext}")]
        )
        if export_path:
            # Handle transparency for PNG->JPG
            if to_format == "jpg" and image_data["img"].mode in ("RGBA", "LA"):
                background = Image.new(image_data["img"].mode[:-1], image_data["img"].size, (255, 255, 255))
                background.paste(image_data["img"], image_data["img"].split()[-1])
                background.save(export_path)
            else:
                image_data["img"].save(export_path)
            messagebox.showinfo("Success", f"Image saved as:\n{export_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert: {str(e)}")

# Browse button
browse_btn = tk.Button(
    content_frame,
    text='Browse Image',
    command=browse,
    font=('Segoe UI', 12, 'bold'),
    bg=ACCENT_COLOR,
    fg='white',
    padx=20,
    pady=8,
    relief=tk.RAISED,
    bd=0,
    cursor='hand2'
)
browse_btn.pack(pady=15)
browse_btn.bind('<Enter>', lambda e: browse_btn.config(bg='#3a80d2'))
browse_btn.bind('<Leave>', lambda e: browse_btn.config(bg=ACCENT_COLOR))

# Selected file label
file_label = tk.Label(
    content_frame,
    text="No image selected",
    font=('Segoe UI', 10),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    pady=5
)
file_label.pack()

# Separator
separator = ttk.Separator(content_frame, orient='horizontal')
separator.pack(fill=tk.X, pady=20)

# Conversion buttons frame
convert_frame = tk.Frame(content_frame, bg=BG_COLOR)
convert_frame.pack(pady=10)

# PNG to JPG button
png_to_jpg_btn = tk.Button(
    convert_frame,
    text='PNG to JPG',
    command=lambda: convert("jpg"),
    font=('Segoe UI', 11, 'bold'),
    bg=BUTTON_COLOR,
    fg='white',
    padx=25,
    pady=8,
    relief=tk.RAISED,
    bd=0,
    cursor='hand2'
)
png_to_jpg_btn.grid(row=0, column=0, padx=20)
png_to_jpg_btn.bind('<Enter>', lambda e: png_to_jpg_btn.config(bg='#4cae4c'))
png_to_jpg_btn.bind('<Leave>', lambda e: png_to_jpg_btn.config(bg=BUTTON_COLOR))

# JPG to PNG button
jpg_to_png_btn = tk.Button(
    convert_frame,
    text='JPG to PNG',
    command=lambda: convert("png"),
    font=('Segoe UI', 11, 'bold'),
    bg=BUTTON_COLOR,
    fg='white',
    padx=25,
    pady=8,
    relief=tk.RAISED,
    bd=0,
    cursor='hand2'
)
jpg_to_png_btn.grid(row=0, column=1, padx=20)
jpg_to_png_btn.bind('<Enter>', lambda e: jpg_to_png_btn.config(bg='#4cae4c'))
jpg_to_png_btn.bind('<Leave>', lambda e: jpg_to_png_btn.config(bg=BUTTON_COLOR))

# Footer
footer = tk.Label(
    root,
    text='Created by GHITA',
    font=('Segoe UI', 9),
    bg=BG_COLOR,
    fg=LABEL_COLOR,
    pady=10
)
footer.pack(side=tk.BOTTOM)

root.mainloop()