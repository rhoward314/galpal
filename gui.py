# this will be the place where we write the GUI class!

from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk


# this is the code i used to experiment with gui - delete later
# basic code to open an image from the internet
#image_url = "https://science.nasa.gov/wp-content/uploads/2023/04/heic1901a-jpg.webp?w=2048&format=webp"

#root = tk.Tk()
#data = urlopen(image_url)
#image = ImageTk.PhotoImage(data=data.read())
#tk.Label(root, image=image).pack()
#root.mainloop()

# create a GUI window
#root = tk.Tk()
#root.title('this is a title')
# things in the window will be added later

# add a label
#w_label = tk.Label(root, text='this is a label').grid(row=0)
#w_label.pack()

# add a button
#w_button = tk.Button(root,text='button', width=25,command=root.destroy).grid(row=1)
#w_button.pack()

# add input field
#tk.Label(root, text='input 1').grid(row=2)
#tk.Label(root, text='input 2').grid(row=3)
#e1 = tk.Entry(root).grid(row=2, column=1)
#e2 = tk.Entry(root).grid(row=3, column=1)

# add checkboxes
#tk.Checkbutton(root,text='option 1').grid(row=4)
#tk.Checkbutton(root,text='option 2').grid(row=4, column=1)

# this opens the window and keeps it open until you close it
#root.mainloop()


# actual code for the project starts here
#test

# image link (will eventually pull from a list of links)
image_url = "https://science.nasa.gov/wp-content/uploads/2023/04/heic1901a-jpg.webp?w=2048&format=webp"

# create a GUI window
root = tk.Tk()
root.title('Gal Pal Galaxy Classification')
root.geometry('800x600')

# add image
data = urlopen(image_url)
#resized_image = data.resize(('600,400'))
image = ImageTk.PhotoImage(data=data.read())
#resized_image = image.resize(('600,400'))
tk.Label(root, image=image).pack()

root.mainloop()