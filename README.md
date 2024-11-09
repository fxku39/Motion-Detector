## Motion-Detector
Python Project for detecting motion using a webcam and obtain a report of times were the motion was detected

##Background for Project
We wanted to create a motion detector using a webcam as a base so we can use it as a vigilance camera or as a motion detector for animals in the garden. We create a code that receives
the data of each frame or imagen from the webcam and use it in a comparison to detect changes in the video (motion). 
After that we use another script which take the dataframe obtained in the motion_detector.py and use bokeh to generate an .html file with the quad graphic plot. 
Lastly we add some labels to the plot so it can show the datetime we detected motion in the video.

#Example Plot
![alt text](https://github.com/fxku39/Motion-Detector/blob/main/bokeh_quad_plot.png "Bokeh_Quad_Plot")

#Posible upgrades or New functions
1. With the information we obtain, aside from the plot we would like to obtain a series of images or frames when something was detected, so we can see a recopilatory of what provoked each
detection.

2.Also we can add to the existing label the duration of each detection in seconds.

3. We can implement uploading this images and plots to a web page so we can observe the updates the next day.
