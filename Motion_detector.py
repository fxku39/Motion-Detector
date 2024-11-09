import cv2, time, pandas
from datetime import datetime

video_obj2=cv2.VideoCapture(0)

first_frame = None #Our first frame it's going to be defined as None 

status_list=[None, None] #We create a list with None elements so we can compare and fill later and don't get an error of "not defined"
times=[] # An empty list which will contain the times the loop detect some movement o change in the original frame
df=pandas.DataFrame(columns=['start','end']) #Creation of the dataframe, this will contain the information of the time the motion was detected

while True: 

    check, frame = video_obj2.read()

    status=0
    
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# We change the original image of the webcam to a grayscale
    img_gray = cv2.GaussianBlur(img_gray, (21,21),0) #We apply a GaussianBlur so when we compare the images of the 1° frame of the video with the rest it's easier to detect changes

    #El siguiente bloque compara si el primer frame existe, cuando no lo detecta lo asigna como el primer array img_gray, cuando existe simplemente continua el código
    #The next block of code compare if the 1° frame exist, when doesn't detect it creates the first image based of the first array of "img_gray", when exist simply continues with the rest of the code
    if first_frame is None:
        first_frame=img_gray
        continue

    delta_frame = cv2.absdiff(first_frame,img_gray) #Delta frame it's the difference within the first frame and the rest of the images created with img_gray
    thresh_frame=cv2.threshold(delta_frame, 75 , 255 , cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 5000:
            continue
        status=1
        (x , y , w , h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)

#The next block of code we use a conditional to detect every change of the status and add that time to our "times" list

    if status_list[-1]==1 and status_list[-2]==0: 
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow('capturing', img_gray)  
    cv2.imshow('delta frame', delta_frame)
    cv2.imshow('threshold', thresh_frame)
    cv2.imshow('Color frame', frame)

    key = cv2.waitKey(3)
    
    if key == ord('q'): 
        if status==1:
            times.append(datetime.now())
        else:
            break
        break

#The next block of code is a loop so we can add every timestamp in the list times to our dataframe
for i in range(0,len(times),2):

    df = pandas.concat([df, pandas.DataFrame.from_records([{ 'start': times[i], 'end': times[i+1] }])], ignore_index=True)

print(status_list)
print(times)
df.to_csv('timestamps.csv')


video_obj2.release()
cv2.destroyAllWindows