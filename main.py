import cv2

# Load two images
img = cv2.imread('i.jpg')
logo = cv2.imread('watermark.png')

img_height, img_width, channels = img.shape

logo_height, logo_width, channels = logo.shape

height_scale_percent = 6 # percent of original size
width_scale_percent = (height_scale_percent * img_height * logo_width) / (img_width * logo_height)

#calculate new width and height of logo
logo_width = int(img_width * width_scale_percent  / 100)
logo_height = int(img_height * height_scale_percent / 100)
# resize image
logo = cv2.resize(logo, (logo_width, logo_height), interpolation = cv2.INTER_AREA)
 
# I want to put logo on top-left corner, So I create a ROI
distance_from_picture_side_percent = 5

distance_from_bottom = int(img_height * distance_from_picture_side_percent / 100)
distance_from_side = int(img_width * distance_from_picture_side_percent / 100)

logo_starting_height = img_height - logo_height - distance_from_bottom
logo_starting_width = distance_from_side
logo_ending_height = img_height - distance_from_bottom
logo_ending_width = logo_width + distance_from_side

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
