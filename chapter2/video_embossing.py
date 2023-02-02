import cv2
import numpy as np

cap= cv2.VideoCapture(0)


while True:
    _,  frame = cap.read()
    # generating the kernels 
    kernel_emboss_1 = np.array([[0,-1,-1], 
                                [1,0,-1], 
                                [1,1,0]]) 
    kernel_emboss_2 = np.array([[-1,-1,0], 
                                [-1,0,1], 
                                [0,1,1]]) 
    kernel_emboss_3 = np.array([[1,0,0], 
                                [0,0,0], 
                                [0,0,-1]]) 
     
    # converting the image to grayscale 
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
     
    # applying the kernels to the grayscale image and adding the offset to produce the shadow
    output_1 = cv2.filter2D(gray_img, -1, kernel_emboss_1) + 128 
    output_2 = cv2.filter2D(gray_img, -1, kernel_emboss_2) + 128 
    output_3 = cv2.filter2D(gray_img, -1, kernel_emboss_3) + 128 
     
    cv2.imshow('Input', frame) 
    cv2.imshow('Embossing - South West', output_1) 
    cv2.imshow('Embossing - South East', output_2) 
    cv2.imshow('Embossing - North West', output_3) 


    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
