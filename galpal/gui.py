# this will be the place where we write the GUI class!

from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import pandas as pd

def prepare_image(image_url):
    """Prepare-Image
    
    Opens an image from a link and makes a PhotoImage object that contains an image.
    
    Args:
        image_url (str): string. Link to galaxy image from 'classifications.txt'.
    
    Returns:
        PhotoImage: PhotoImage object containing image.
    """
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


def dropdown(window):
    options = [
        'Galaxy 1', 'Galaxy 2', 'Galaxy 3', 'Galaxy 4', 'Galaxy 5',
        'Galaxy 6', 'Galaxy 7', 'Galaxy 8', 'Galaxy 9', 'Galaxy 10'
    ]

    galaxy_option = tk.StringVar(window)
    galaxy_option.set(options[0])

    dropdown = tk.OptionMenu(window, galaxy_option, *options)
    dropdown.pack() 



def main():
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

    # create label with box for image
    image_label = tk.Label(root, width=500, height=500, bg='lightgray')
    image_label.place(x = 150, y = 30)
    image1 = prepare_image(url)
    image_label.configure(image=image1)

    # spiral/elliptical buttons
    spiral_button = tk.Button(root, text = 'Spiral')
    spiral_button.place(x = 690, y = 70)

    elliptical_button = tk.Button(root, text = 'Elliptical')
    elliptical_button.place(x = 678, y = 110)

    #dropdown menu
    dropdown(root)

    # keeps gui window open until you close it
    root.mainloop()

if __name__ == '__main__':
    main()