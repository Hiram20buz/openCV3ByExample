import cv2
import numpy as np
import math

cap= cv2.VideoCapture(0)


while True:
    _,  frame = cap.read()
    
    rows, cols = frame.shape[:2]
    
    ##################### 
    # Vertical wave 
     
    img_output = np.zeros(frame.shape, dtype=frame.dtype) 
     
    for i in range(rows): 
        for j in range(cols): 
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180)) 
            offset_y = 0 
            if j+offset_x < rows: 
                img_output[i,j] = frame[i,(j+offset_x)%cols] 
            else: 
                img_output[i,j] = 0 
     
    cv2.imshow('Input', frame) 
    cv2.imshow('Vertical wave', img_output) 
     
    ##################### 
    # Horizontal wave 
     
    img_output = np.zeros(frame.shape, dtype=frame.dtype) 
     
    for i in range(rows): 
        for j in range(cols): 
            offset_x = 0 
            offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150)) 
            if i+offset_y < rows: 
                img_output[i,j] = frame[(i+offset_y)%rows,j] 
            else: 
                img_output[i,j] = 0 
     
    cv2.imshow('Horizontal wave', img_output) 
     
    ##################### 
    # Both horizontal and vertical  
     
    img_output = np.zeros(frame.shape, dtype=frame.dtype) 
     
    for i in range(rows): 
        for j in range(cols): 
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150)) 
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150)) 
            if i+offset_y < rows and j+offset_x < cols: 
                img_output[i,j] = frame[(i+offset_y)%rows,(j+offset_x)%cols] 
            else: 
                img_output[i,j] = 0 
     
    cv2.imshow('Multidirectional wave', img_output) 
     
    ##################### 
    # Concave effect 
     
    img_output = np.zeros(frame.shape, dtype=frame.dtype) 
     
    for i in range(rows): 
        for j in range(cols): 
            offset_x = int(128.0 * math.sin(2 * 3.14 * i / (2*cols))) 
            offset_y = 0 
            if j+offset_x < cols: 
                img_output[i,j] = frame[i,(j+offset_x)%cols] 
            else: 
                img_output[i,j] = 0 
     
    cv2.imshow('Concave', img_output) 
    
    #cv2.imshow("Original", frame)


    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
