#!/usr/bin/python

import cv2
import sys, getopt
import re

args = sys.argv[1:]
image_file_path = logo_file_path = None

# Set default logo place, which is bottom left
bottom = True
left = True

# percent of original size
height_scale_percent = 6

# percent of distance from sides
distance_from_sides_of_picture_percent = 5
distance_from_up_bottom_of_picture_percent = 5

# Pars arguments
try:
    opts, args = getopt.getopt(args,"hi:l:p:r:u:",["image=", "logo=", "percents="])
except getopt.GetoptError:
    print('Use `python main.py -h` to see how this code has to used.')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('$ python main.py')
        print('Options:')
        print('-i <image path>')
        print('-l <watermark path>')
        print('-p <watermark scale percents>')
        print('-r <distance from left or right >')
        print('-u <distance from up or bottom>')
        print('')
        print('If you don\'t gave image path and watermark, script consume them by default as image.jpg and logo.png')
        print('With -p option, declare logo should be how many percents of the main image')
        print('By defalt, this value is 6%')
        print('You can set logo distance from picture sides using -r')
        print('You can set logo distance from up or bottom using -u')
        print('Defualt value for these are 5%')
        print('Use top, bottom, left and right key words to declare watermark place')
        print('Watermark palce is by default bottom and left')
        sys.exit()
    elif opt in ("-i", "--image"):
        image_file_path = arg
    elif opt in ("-l", "--logo"):
        logo_file_path = arg
    elif opt in ("-p", "--percents"):
        height_scale_percent = int(arg)
    elif opt in ("-r"):
        distance_from_sides_of_picture_percent = int(arg)
    elif opt in ("-u"):
        distance_from_up_bottom_of_picture_percent = int(arg)


for arg in args:
    if arg == 'right':
        left = False
        continue
    elif arg == 'top':
        bottom = False
        continue

    arg = re.split("=", arg)
    if len(arg) == 2:
        argument, value = arg
        if argument == 'image':
            image_file_path = value
        elif argument == 'logo':
            logo_file_path = value
        elif argument == 'percents':
            height_scale_percent = value

if image_file_path is None or image_file_path is '':
    print('You didn\'t give image file path. I consume it as image.jpg')
    image_file_path = "image.jpg"

if logo_file_path is None or logo_file_path is '':
    print('You didn\'t give logo file path. I consume it as logo.png')
    logo_file_path = "logo.png"

# Load image and watermark
img = cv2.imread(image_file_path)
logo = cv2.imread(logo_file_path)

img_height, img_width, channels = img.shape

logo_height, logo_width, channels = logo.shape

width_scale_percent = (height_scale_percent * img_height * logo_width) / (img_width * logo_height)

# Calculate new width and height of logo
logo_width = int(img_width * width_scale_percent  / 100)
logo_height = int(img_height * height_scale_percent / 100)

# Calculate distance from image sides
distance_from_bottom = int(img_height * distance_from_up_bottom_of_picture_percent / 100)
distance_from_side = int(img_width * distance_from_sides_of_picture_percent / 100)


print('Main Image: %s' % image_file_path)
print('Watermark: %s' % logo_file_path)
print('Watermark Location: %s %s' % ('Bottom' if bottom else 'Top', 'Left' if left else 'Right'))

print('Watermark distance from %s: %d' % ('bottom' if bottom else 'top', distance_from_bottom))
print('Watermark distance from %s: %d' % ('left' if left else 'right', distance_from_side))
print('Image width: %d' % img_width)
print('Image height: %d' % img_height)
print('Watermark width: %d' % logo_width)
print('Watermark height: %d' % logo_height)
print('----------------------------------------------------------')
print('Adding watermark to image...')

# Resize image
logo = cv2.resize(logo, (logo_width, logo_height), interpolation = cv2.INTER_AREA)

# Set logo coordinates
if bottom:
    logo_starting_height = img_height - logo_height - distance_from_bottom
    logo_ending_height = img_height - distance_from_bottom
else:
    logo_starting_height = distance_from_bottom
    logo_ending_height = logo_height + distance_from_bottom

if left:
    logo_starting_width = distance_from_side
    logo_ending_width = logo_width + distance_from_side
else:
    logo_starting_width = img_width - logo_width - distance_from_side
    logo_ending_width = img_width - distance_from_side

# I want to put logo on top-left corner, So I create a ROI
roi = img[logo_starting_height: logo_ending_height, logo_starting_width: logo_ending_width]

# Now create a mask of logo and create its inverse mask also
logo_gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

# Take only region of logo from logo image.
logo_fg = cv2.bitwise_and(logo,logo,mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img_bg,logo_fg)
img[logo_starting_height: logo_ending_height, logo_starting_width: logo_ending_width] = dst

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
