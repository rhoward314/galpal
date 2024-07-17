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
    df = pd.read_csv('classifications.txt', sep='\s+')
    which_gal = np.random.randint(0, 10)
    url = df['link'][which_gal]

    # create a GUI window
    root = tk.Tk()
    # set title for window
    root.title('Gal Pal Galaxy Classification')
    # set size of window
    root_width = 1000 # width in pixels
    root_height = 650 # height in pixels
    root.geometry(f'{root_width}x{root_height}')

    # create label with box for image
    image_label_width = 500
    image_label_height = 500
    image_label_y_offset = 30
    margin_width = (root_width - image_label_width) / 2
    image_label = tk.Label(root, width=image_label_width, height=image_label_height, bg='gray')
    image_label.place(x=margin_width, y=image_label_y_offset)
    image1 = prepare_image(url)
    image_label.configure(image=image1)

    # spiral/elliptical buttons
    button_frame = tk.Frame(root)#, bg='green')
    spi_ell_pady = 5

    spiral_button = tk.Button(button_frame, text='Spiral')
    spiral_button.grid(row=0, column=0, pady=spi_ell_pady)

    elliptical_button = tk.Button(button_frame, text='Elliptical')
    elliptical_button.grid(row=1, column=0, pady=spi_ell_pady)

    # get width of button_frame, then use that to center button_frame in the empty space to the right of the image
    button_frame.place(x=0, y=0)
    button_frame.update()
    button_frame_width, button_info_height = button_frame.winfo_width(), button_frame.winfo_height()
    button_frame.place_forget()
    button_frame.place(x=root_width - margin_width + (margin_width - button_frame_width) / 2, y=70)

    # next/previous/random buttons
    npr_frame = tk.Frame(root)
    npr_padx = 3

    prev_button = tk.Button(npr_frame, text='Previous')
    prev_button.grid(row=0, column=0, padx = npr_padx)

    rand_button = tk.Button(npr_frame, text='Random')
    rand_button.grid(row=0, column=1, padx = npr_padx)

    next_button = tk.Button(npr_frame, text='Next')
    next_button.grid(row=0, column=2, padx = npr_padx)

    # center next/prev/rand button frame below galaxy image
    npr_frame.place(x=0, y=0)
    npr_frame.update()
    npr_frame_width, npr_frame_height = npr_frame.winfo_width(), npr_frame.winfo_height()
    npr_frame.place_forget()
    bottom_margin_height = root_height - image_label_y_offset - image_label_height
    npr_frame.place(x=(root_width - npr_frame_width) / 2,
                    y=image_label_y_offset + image_label_height + (bottom_margin_height - npr_frame_height)/4)

    #dropdown menu
    dropdown(root)

    # keeps gui window open until you close it
    root.mainloop()

if __name__ == '__main__':
    main()