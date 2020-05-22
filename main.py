import cv2

# Load two images
img = cv2.imread('i.jpg')
logo = cv2.imread('watermartk.jpg')

img_height = img.shape[0]
img_width = img.shape[1]

logo_height = logo.shape[0]
logo_width = logo.shape[1]

height_scale_percent = 8 # percent of original size
width_scale_percent = (height_scale_percent * img_height * logo_width) / (img_width * logo_height)

width = int(img_width * width_scale_percent  / 100)
height = int(img_height * height_scale_percent / 100)
# resize image
logo = cv2.resize(logo, (width, height), interpolation = cv2.INTER_AREA)

print('Resized Dimensions : ',logo.shape)
 
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = logo.shape
roi = img[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
logo_gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
logo_fg = cv2.bitwise_and(logo,logo,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img_bg,logo_fg)
img[0:rows, 0:cols ] = dst

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
