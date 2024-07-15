# this will be the place where we write the GUI class!

from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk

image_url = "https://science.nasa.gov/wp-content/uploads/2023/04/heic1901a-jpg.webp?w=2048&format=webp"

root = tk.Tk()
data = urlopen(image_url)
image = ImageTk.PhotoImage(data=data.read())
tk.Label(root, image=image).pack()
root.mainloop()