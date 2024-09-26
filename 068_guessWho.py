import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main window
window = tk.Tk()
window.title("Guess Who!")
window.geometry("400x400")

label = "Guess Who!"  # Label text for display


# Function to show the image based on user input
def showImage():
    person = text.get("1.0", "end")  # Retrieve the text input from the user
    if person.lower().strip() == "mo":
        canvas.itemconfig(container, image=mo)
    elif person.lower().strip() == "charlotte":
        canvas.itemconfig(container, image=charlotte)
    elif person.lower().strip() == "gerald":
        canvas.itemconfig(container, image=gerald)
    elif person.lower().strip() == "katie":
        canvas.itemconfig(container, image=katie)
    else:
        canvas.pack_forget()
        warning.pack()
        return
    warning.pack_forget()
    canvas.pack()


# Create and pack the label, text input field, and button
hello = tk.Label(text=label)
hello.pack()
warning = tk.Label(text="Unable to locate this image")
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()

# Create and pack the canvas for displaying images
canvas = tk.Canvas(window, width=400, height=380)

# Load the images to be displayed
charlotte = ImageTk.PhotoImage(Image.open("guessWho/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("guessWho/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("guessWho/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("guessWho/mo.jpg"))

# Initialize the canvas with an empty image container
container = canvas.create_image(150, 1, image=None)


tk.mainloop()
