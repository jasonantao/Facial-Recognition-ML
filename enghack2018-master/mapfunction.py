import glob


for image_file in glob.iglob('/path/to/image/dir/*.jpg'):
    your_resize_function(image_file)