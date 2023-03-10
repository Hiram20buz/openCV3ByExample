import cv2
import numpy as np

cap= cv2.VideoCapture(0)
#x_medium = 0
#y_medium = 0

while True:
    _,  frame = cap.read()
    #hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # red color
    #low_red  = np.array([161, 155, 84])
    #high_red = np.array([179, 255 ,255])
    #red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    rows, cols = frame.shape[:2]
    src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
    dst_points = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])
    affine_matrix = cv2.getAffineTransform(src_points, dst_points)
    img_output = cv2.warpAffine(frame, affine_matrix, (cols,rows))


    
    
    



    #contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    #for cnt in contours:
        #(x, y, w, h) = cv2.boundingRect(cnt)

        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #x_medium = int((x + x + w) / 2)
        #y_medium = int((y + y + h) / 2)
        #break

    #cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    #cv2.line(frame, (0, y_medium), (640, y_medium), (0, 255, 0), 2)
    cv2.imshow("Original", frame)
    cv2.imshow('Mirror', img_output)


    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
