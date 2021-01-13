# -- coding: utf-8 --
"""
Created on Wed Jul 22 12:49:43 2020

@author: stuar
"""
from PIL import Image

'''
!!!Make sure to install Pillow via pip!!!

Converts any image in the same directory as the file to a PDF document.

'''
conversion_process = True # this is the main loop - it will convert all it can while the user still wants that.
while conversion_process:

    filename = input("Please enter the name of the image you wish to convert to a PDF.")

    filetypes = ['.jpg', '.jpeg', '.png', '.gif', '.tiff']

    all_possible_files = [filename]

    for filetype in filetypes:
        all_possible_files.append(filename + filetype)

    image1 = None

    for filename in all_possible_files:
        try:
            image1 = Image.open(filename)
            correct_image = input('I found a file with the name ' + filename + '. Do you wish to convert this image? '
                                                                               'Please enter Y or N.')
            if correct_image == 'Y' or correct_image == 'y':
                im1 = image1.convert('RGB')
                im1.save(filename + '.pdf')
            elif correct_image == 'N' or correct_image == 'n':
                continue
            else:
                print('Please enter Y or N when prompted, and not some horse shit. No conversion for you!')
                break
        except FileNotFoundError:
            print('Oh no! There wasn\'t a file with the extension: ' + filename)
            pass

    if image1 is None:
        print('No images were found. FUUUUUUUUUUUUU')
        break
    feedback = input("Are you done? Y to exit")
    if feedback == 'Y' or feedback == 'y':
        conversion_process = False
