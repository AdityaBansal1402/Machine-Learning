import cv2

img=cv2.imread('dog.png')

cv2.imshow('Dog Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()