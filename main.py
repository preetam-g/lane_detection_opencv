import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(f"Video1.mp4") # name of the video file you want to detect lines on

while cap.isOpened():

    success, frame = cap.read()
    # cv.imshow("test", frame)

    if success:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # converting frame into grayscale
        # cv.imshow("gray", gray)

        blur = cv.GaussianBlur(gray, (7,7), 0) # blurring the image to reduce noise
        # cv.imshow("blur", blur)

        canny = cv.Canny(blur, 100, 200) # detect edges using canny
        # cv.imshow("canny", canny)

        height, width = canny.shape # create a region of interest, in this case it is the bottom part of the image
        roi = canny[int(0.3*height): , :]

        # apply houghlines in the roi 
        hough_lines = cv.HoughLinesP(roi, 1, np.pi/180, 200, minLineLength = 40, maxLineGap = 10)
        print((hough_lines), type(hough_lines))


        if type(hough_lines) == np.ndarray: # to make sure that we have hough_lines, sometimes we get nonetype
            for line in hough_lines: # drawing lines on the bottom part of actual frame because roi was bottom part 
                x, y, w, h = line[0]
                res = cv.line(frame[int(0.3*height):, :], (x, y), (w, h), color = (120, 250, 0), thickness = 4)
        else: pass
        
        cv.imshow("hi there", res) # displaying the result

        if cv.waitKey(40) == ord('q'): break # if you press q during the run then exit
    else: cv.waitKey(1000); break # wait 1 sec when the whole video is read and then exit 


cv.destroyAllWindows()