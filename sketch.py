import cv2

img = cv2.imread('enter_name.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_img = 255 - gray_img
blurred_img = cv2.GaussianBlur(inverted_gray_img, (77, 77), 0)
inverted_blurred_img = 255 - blurred_img
sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

cv2.imshow('Original', img)
cv2.imshow('Sketch', sketch_img)

cv2.waitKey(0)

cv2.imwrite('enter_name_sketch.jpg', sketch_img)