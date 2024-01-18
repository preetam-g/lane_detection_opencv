import cv2 as cv
import numpy as np 

num = int(input("give video num you want to test on(1,2,3): "))
cap = cv.VideoCapture(f"Video{num}.mp4")

while cap.isOpened():

    success, frame = cap.read()
    # cv.imshow("test", frame)

    if success:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # cv.imshow("gray", gray)

        blur = cv.GaussianBlur(gray, (7,7), 0)
        # cv.imshow("blur", blur)

        canny = cv.Canny(blur, 100, 200)
        # cv.imshow("canny", canny)

        height, width = canny.shape
        roi = canny[int(0.3*height): , :]

        
        hough_lines = cv.HoughLinesP(roi, 1, np.pi/180, 200, minLineLength = 40, maxLineGap = 10)
        print((hough_lines), type(hough_lines))
        
        if type(hough_lines) == np.ndarray:
            for line in hough_lines:
                x, y, w, h = line[0]
                res = cv.line(frame[int(0.3*height):, :], (x, y), (w, h), color = (120, 250, 0), thickness = 4)
        else: pass
        
        cv.imshow("hi there", res)

        if cv.waitKey(40) == ord('q'): break
    else: cv.waitKey(1000); break


cv.destroyAllWindows()