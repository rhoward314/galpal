# this will be the place where we write the GUI class!

from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import pandas as pd

def prepare_image(image_url):
    # open image from link and create an image object that can be added to label in gui window
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
    elif h_old == w_old:
        h_new = box_size
        w_new = box_size
    else:
        print('something is wrong with this image')
    # resize image
    new_pil_image = pil_image.resize((w_new,h_new))
    tkimage = ImageTk.PhotoImage(new_pil_image)
    # create label widget in gui with image
    return tkimage

# read in list of galaxies
df = pd.read_csv('classifications.txt',sep='\s+')
which_gal = np.random.randint(0,10)
url = df['link'][which_gal]

# create a GUI window
root = tk.Tk()
# set title for window
root.title('Gal Pal Galaxy Classification')
# set size of window
root.geometry('800x600')


#image_url = "https://science.nasa.gov/wp-content/uploads/2023/04/heic1901a-jpg.webp?w=2048&format=webp"

# create label with box for image
image_label = tk.Label(root, width=500,height=500,bg='lightgray')
image_label.pack(pady=20)

image1 = prepare_image(url)
image_label.configure(image=image1)

# keeps gui window open until you close it
root.mainloop()