# this will be the place where we write the GUI class!

from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk, Image

def prepare_image(image_url):
    # display the chosen image in an existing gui window
    # link to image
    #img_url = image_url
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
    # resize image
    new_pil_image = pil_image.resize((w_new,h_new))
    tkimage = ImageTk.PhotoImage(new_pil_image)
    # create label widget in gui with image
    return tkimage

def test_label(text,gui_window):
    tk.Label(gui_window,text=text).pack()


# create a GUI window
root = tk.Tk()
# set title for window
root.title('Gal Pal Galaxy Classification')
# set size of window
root.geometry('800x600')

'''
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

# resize image
new_pil_image = pil_image.resize((w_new,h_new))
image = ImageTk.PhotoImage(new_pil_image)

# create label widget in gui with image
tk.Label(root, image=image, width=500,height=500,bg='lightgray').pack(pady=20)'''

image_url = "https://science.nasa.gov/wp-content/uploads/2023/04/heic1901a-jpg.webp?w=2048&format=webp"
#display_image(url1,root)

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

# resize image
new_pil_image = pil_image.resize((w_new,h_new))
image = ImageTk.PhotoImage(new_pil_image)

# create label widget in gui with image
#image_label = tk.Label(root, image=image, width=500,height=500,bg='lightgray')
#image_label.pack(pady=20)

# create label with box for image
image_label = tk.Label(root, width=500,height=500,bg='lightgray')
image_label.pack(pady=20)

image1 = prepare_image(image_url)
image_label.configure(image=image1)

test_label('this is a label',root)

label2 = tk.Label(root,text='this is a different label')
label2.pack()
label2.configure(text='and even more labels')

url2 = 'https://science.nasa.gov/wp-content/uploads/2023/04/m51-and-companion_0-jpg.webp?w=2048&format=webp'

image2 = prepare_image(url2)
image_label.configure(image=image2)

# keeps gui window open until you close it
root.mainloop()