# this will be the place where we write the GUI class!

from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk, Image


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

# create a GUI window
root = tk.Tk()
# set title for window
root.title('Gal Pal Galaxy Classification')
# set size of window
root.geometry('800x600')

# image link (will eventually pull from a list of links)
image_url = "https://science.nasa.gov/wp-content/uploads/2023/04/heic1901a-jpg.webp?w=2048&format=webp"
# open image from link
data = urlopen(image_url)

# create image object
pil_image = Image.open(data)
# get original image size
w_old,h_old = pil_image.size

# size of label box for image (square)
box_size = 500 

if w_old > h_old:
    w_new = box_size
    h_new = int(w_new * (h_old/w_old))
elif h_old > w_old:
    h_new = box_size
    w_new = int(h_new * (w_old/h_old))

#crop_size = np.min((w_old,h_old))
#print(crop_size)
#center_w = w_old / 2
#center_h = h_old / 2
#left_crop = center_w - (crop_size/2)
#right_crop = center_w + (crop_size/2)
#top_crop = center_h - (crop_size/2)
#bottom_crop = center_h + (crop_size/2)
#cropped_image = pil_image.crop((left_crop,top_crop,right_crop,bottom_crop))

# resize image
new_pil_image = pil_image.resize((w_new,h_new))
image = ImageTk.PhotoImage(new_pil_image)

# create label widget in gui with image
tk.Label(root, image=image, width=500,height=500,bg='gray').pack(pady=20)

# keeps gui window open until you close it
root.mainloop()