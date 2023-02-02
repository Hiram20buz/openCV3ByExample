import cv2

img = cv2.imread('a.jpg')

cv2.imwrite('output.png', img, [cv2.IMWRITE_PNG_COMPRESSION])
