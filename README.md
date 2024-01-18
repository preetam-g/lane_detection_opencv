# Lane Detection using OpenCV in python
A lane detection program using openCV in python. 
The region of interest has been selected has the bottom part of the image and then lines have been plotted. This has been to make sure that the program works for wide range of vidoes. 
This program also prints the houghlines array and its to type to show that in some cases we may have nonetype. To avoid errors an if statement has been added to check the type of houghlines array.

# Test Videos
Three test videos have been given to check the working of the program. This program may not be suitable for all types of videos but if you tune the thresholds in canny, matrix size in guassian blur, then you can use it according to your requirement. 

# How to use
Make sure the video file you want to test and the program file are in the same directory then use the terminal to change your working directory to the program directory. Then change the name "Video1.mp4" in cv.VideoCapture() with your video file in the main.py file. Then you can type "python main.py" in VSCode, "python3 main.py" in Ubuntu in the terminal to run the program. 