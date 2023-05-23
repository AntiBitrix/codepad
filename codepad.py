#Here import module of tkinter for GUI stuff and ttk for defining functions (err..)
import tkinter as tk
from tkinter import ttk

#def or create a function to make togglable dark and white mode setup
def toggle_dark_mode():
    # Check the current background color of the main window
    if main["bg"] == "white":
        # Switch to dark mode
        main["bg"] = "black"
        label["bg"] = "black"
        label["fg"] = "white"
        textbox["bg"] = "black"
        textbox["fg"] = "white"
    else:
        # Switch back to light mode
        main["bg"] = "white"
        label["bg"] = "white"
        label["fg"] = "black"
        textbox["bg"] = "white"
        textbox["fg"] = "black"

# Create the main window
main = tk.Tk()
main.geometry('800x660')
main.title("CodePad")

# Create a label widget
label = tk.Label(main, text="C0depad", bg='white', fg='black', font=('Hack', 16))
label.pack(padx=4, pady=4)

# Create a text widget
textbox = tk.Text(main, font=('hack', 16))
textbox.pack()

# Create a button widget for toggling dark mode
toggle_button = ttk.Button(main, text="Dark Mode", command=toggle_dark_mode)
toggle_button.pack(anchor="ne", padx=10, pady=10)

# Run the main event loop
main.mainloop()
