# this will be the place where we write the GUI class!

from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
from functools import partial
import galaxy  # delete this later when everything is set up right

def prepare_image(image_url):
    """Prepare-Image
    
    Opens an image from a link and makes a PhotoImage object that contains an image.
    
    Args:
        image_url (str): string. Link to galaxy image from 'image_links.txt'.
    
    Returns:
        PhotoImage: PhotoImage object containing image.
    """
    # open image from link and create an image object that can be added to label in gui window
    data = urlopen(image_url) # open image from link
    pil_image = Image.open(data) # create image object
    w_old, h_old = pil_image.size # get original image size
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

class temp_gui_class:
    def __init__(self, which_gal, url=0):
        # which_gal and url need to be attributes of an object to update with buttons
        # url should go in galaxy class, not sure where which_gal will go
        # using this for now just to get buttons working
        self.which_gal = which_gal
        self.url = url
        self.grade = 0
        self.attempts = 0

def update_gal(gui_obj, gal_obj, link_df, desc_df):
    #name, classification, distance in LY, Mass in M_sun, Constellation location, SFR (M_sun/year, if applicable)
    gal_obj.number = gui_obj.which_gal
    gal_obj.name = link_df['#name'][gal_obj.number]
    gal_obj.morph_type = desc_df[' classification'][gal_obj.number]
    gal_obj.distance = desc_df[' distance in LY'][gal_obj.number]
    gal_obj.stellar_mass = desc_df[' Mass in M_sun'][gal_obj.number]
    gal_obj.constellation = desc_df[' Constellation location'][gal_obj.number]
    gal_obj.star_formation = desc_df[' SFR (M_sun/year if applicable)'][gal_obj.number]
    gui_obj.url = link_df['link'][gal_obj.number]  # should the link be part of the galaxy class?

def get_info_text(gal_obj):
    # spiral text
    if gal_obj.morph_type == 'spiral':
        info_text = str(gal_obj.name) + ' is a spiral galaxy! '
        info_text += 'It is located ' + str(gal_obj.distance) +' light years away in the ' + str(gal_obj.constellation)+'. '
        info_text += 'It has a stellar mass that is ' + str(gal_obj.stellar_mass) + ' times greater than our sun. '
        info_text += 'This is a star-forming galaxy with a star-formation rate of roughly ' + str(gal_obj.star_formation) +' solar masses per year! '
        info_text += 'For comparison, the Milky Way forms stars at a rate of roughly one solar mass per year.'
    # elliptical text
    elif gal_obj.morph_type == 'elliptical':
        info_text = str(gal_obj.name) + 'is an elliptical galaxy! '
        info_text += 'It is located ' +str(gal_obj.distance) + ' light years away in the ' + str(gal_obj.constellation)+'. '
        info_text += 'It has a stellar mass that is ' + str(gal_obj.stellar_mass) + 'times greater than our sun. '
        info_text += 'It contains an old stellar population, and it is not actively forming stars.'
    else:
        info_text = gal_obj.morph_type
        print(type(gal_obj.morph_type))
    return info_text


# check if user selection of spiral or elliptical is correct
def is_correct(gui_obj,gal_obj,score_label):
    gui_obj.attempts += 1
    if gal_obj.choice == gal_obj.morph_type:
        gal_obj.grade = 1
        gui_obj.grade += 1
        score_text = str(gui_obj.grade) + ' correct out of ' + str(gui_obj.attempts)+ ' attempts.'
        score_label.configure(text=score_text,width=25,wraplength=200)
        return 'That is correct!'
    else:
        gal_obj.grade = 0
        score_text = str(gui_obj.grade) + ' correct out of ' + str(gui_obj.attempts)+ ' attempts.'
        score_label.configure(text=score_text,width=25,wraplength=200)
        return 'That is incorrect.'

# make button function
def spiral_func(gui_obj,gal_objs,info_label,score_label):
    galaxy_obj = gal_objs[gui_obj.which_gal]
    galaxy_obj.choice = 'spiral'
    label_text = 'You selected spiral.\n' + is_correct(gui_obj,galaxy_obj,score_label)
    label_text += '\n\n'
    label_text += get_info_text(galaxy_obj)
    info_label.configure(text=label_text)

def elliptical_func(gui_obj,gal_objs,info_label,score_label):
    galaxy_obj = gal_objs[gui_obj.which_gal]
    galaxy_obj.choice = 'elliptical'
    label_text = 'You selected elliptical.\n' + is_correct(gui_obj,galaxy_obj,score_label)
    label_text += '\n\n'
    label_text += get_info_text(galaxy_obj)
    info_label.configure(text=label_text)

def prev_gal(gui_obj, gal_objs, link_df, desc_df, image_label, info_label, galaxy_option, options):
    info_label.configure(text='')
    if gui_obj.which_gal > 0:
        gui_obj.which_gal -= 1
    else:
        gui_obj.which_gal = len(gal_objs) - 1
    update_gal(gui_obj, gal_objs[gui_obj.which_gal], link_df, desc_df)
    new_image = prepare_image(gui_obj.url)
    image_label.configure(image=new_image)
    image_label.image = new_image
    galaxy_option.set(options[gui_obj.which_gal])

def rand_gal(gui_obj, gal_objs, link_df, desc_df, image_label, info_label, galaxy_option, options):
    info_label.configure(text='')
    which_gal_old = gui_obj.which_gal
    while gui_obj.which_gal == which_gal_old:
        gui_obj.which_gal = np.random.randint(0, len(gal_objs))
    update_gal(gui_obj, gal_objs[gui_obj.which_gal], link_df, desc_df)
    new_image = prepare_image(gui_obj.url)
    image_label.configure(image=new_image)
    image_label.image = new_image
    galaxy_option.set(options[gui_obj.which_gal])

def next_gal(gui_obj, gal_objs, link_df, desc_df, image_label, info_label, galaxy_option, options):
    info_label.configure(text='')
    if gui_obj.which_gal < len(gal_objs) - 1:
        gui_obj.which_gal += 1
    else:
        gui_obj.which_gal = 0
    update_gal(gui_obj, gal_objs[gui_obj.which_gal], link_df, desc_df)
    new_image = prepare_image(gui_obj.url)
    image_label.configure(image=new_image)
    image_label.image = new_image
    galaxy_option.set(options[gui_obj.which_gal])

def dropdown_select_gal(selection,gui_obj, gal_objs, link_df, desc_df, image_label):
    #info_label.configure(text='')  <-- this will only work if dropdown menu is set up after the info box
    # but right now dropdown menu is set up first and info box placement depends on dropdown placement
    # this could be changed but i'm not going to do it now
    print(selection)
    sel_list = selection.split()
    print(sel_list)
    gui_obj.which_gal = int(sel_list[-1])-1
    print(gui_obj.which_gal)
    update_gal(gui_obj, gal_objs[gui_obj.which_gal], link_df, desc_df)
    new_image = prepare_image(gui_obj.url)
    image_label.configure(image=new_image)
    image_label.image = new_image

def main():

    # create galaxy object (this will probably go in main.py?)
    #current_gal = Galaxy.Galaxy(0,0,0,0,0,0)

    # read in text files with galaxy info
    link_df = pd.read_csv('txt_files/image_links.txt', sep='\s+')
    desc_df = pd.read_csv('txt_files/description_info.txt')
    # create list of galaxy objects so they all exist and can be modified by functions
    gal_objs = [galaxy.Galaxy(i,0,0,0,0,0,0) for i in range(len(link_df['#name']))]
    gui_obj = temp_gui_class(0)
    update_gal(gui_obj, gal_objs[gui_obj.which_gal], link_df, desc_df)

    root = tk.Tk() # create a GUI window
    root.title('Gal Pal Galaxy Classification') # set title for window
    # set size of window
    root_width = 1000 # width in pixels
    root_height = 650 # height in pixels
    root.geometry(f'{root_width}x{root_height}')

    # create label with box for image
    image_label_width = 500
    image_label_height = 500
    image_label_y_offset = 30
    margin_width = (root_width - image_label_width) / 2
    image_label = tk.Label(root, width=image_label_width, height=image_label_height, bg='lightgray')
    image_label.place(x=margin_width, y=image_label_y_offset)
    image1 = prepare_image(gui_obj.url)
    image_label.configure(image=image1)

    # dropdown menu
    options = [f'Galaxy {i}' for i in range(1, len(gal_objs) + 1)]

    galaxy_option = tk.StringVar(root)
    galaxy_option.set(options[0])

    dropdown = tk.OptionMenu(root, galaxy_option, *options, command = partial(dropdown_select_gal,gui_obj=gui_obj, gal_objs=gal_objs, link_df=link_df, desc_df=desc_df, image_label=image_label))
    dropdown.place(x=0, y=0)
    dropdown.update()
    dropdown_width, dropdown_height = dropdown.winfo_width(), dropdown.winfo_height()
    dropdown.place_forget()
    dropdown_y = 70
    dropdown.place(x=(margin_width - dropdown_width) / 2, y=dropdown_y)

    # create label for info box
    info_label = tk.Label(root,text='',width=25,wraplength=200)
    info_label.place(x=0,y=0)
    info_label_width = info_label.winfo_width()
    #info_label.place_forget()
    #info_label_x = (margin_width - info_label_width)/2
    info_label_y = dropdown_y + dropdown_height + 200
    info_label.place(x=15,y=info_label_y)

    # create label for score
    score_text = str(gui_obj.grade) + ' correct out of ' + str(gui_obj.attempts)+ ' attempts.'
    score_label = tk.Label(root, text=score_text,width=25,wraplength=200)
    score_label.place(x=15,y=root_height-90)

    # next/previous/random buttons
    npr_frame = tk.Frame(root)
    npr_padx = 3

    prev_button = tk.Button(npr_frame, text='Previous', command=partial(prev_gal, gui_obj, gal_objs, link_df, desc_df, image_label,info_label,galaxy_option,options))
    prev_button.grid(row=0, column=0, padx = npr_padx)

    rand_button = tk.Button(npr_frame, text='Random', command=partial(rand_gal, gui_obj, gal_objs, link_df, desc_df, image_label,info_label,galaxy_option,options))
    rand_button.grid(row=0, column=1, padx = npr_padx)

    next_button = tk.Button(npr_frame, text='Next', command=partial(next_gal, gui_obj, gal_objs, link_df, desc_df, image_label,info_label,galaxy_option,options))
    next_button.grid(row=0, column=2, padx = npr_padx)

    # center next/prev/rand button frame below galaxy image
    npr_frame.place(x=0, y=0)
    npr_frame.update()
    npr_frame_width, npr_frame_height = npr_frame.winfo_width(), npr_frame.winfo_height()
    npr_frame.place_forget()
    bottom_margin_height = root_height - image_label_y_offset - image_label_height
    npr_frame.place(x=(root_width - npr_frame_width) / 2,
                    y=image_label_y_offset + image_label_height + (bottom_margin_height - npr_frame_height)/4)
    
    # spiral/elliptical buttons
    button_frame = tk.Frame(root)#, bg='green')
    spi_ell_pady = 5

    spiral_button = tk.Button(button_frame, text='Spiral', command=partial(spiral_func, gui_obj,gal_objs,info_label,score_label))
    spiral_button.grid(row=0, column=0, pady=spi_ell_pady)

    elliptical_button = tk.Button(button_frame, text='Elliptical', command=partial(elliptical_func, gui_obj,gal_objs,info_label,score_label))
    elliptical_button.grid(row=1, column=0, pady=spi_ell_pady)

    # get width of button_frame, then use that to center button_frame in the empty space to the right of the image
    button_frame.place(x=0, y=0)
    button_frame.update()
    button_frame_width, button_frame_height = button_frame.winfo_width(), button_frame.winfo_height()
    button_frame.place_forget()
    button_frame.place(x=root_width - margin_width + (margin_width - button_frame_width) / 2, y=70)
    
    #print('created buttons')

    # keeps gui window open until you close it
    root.mainloop()

    #print(gui_obj.which_gal)

    #print(gal_objs[gui_obj.which_gal].choice)

if __name__ == '__main__':
    main()