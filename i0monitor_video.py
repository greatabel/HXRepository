import cv2
from imutils.object_detection import non_max_suppression
from imutils import paths
from imutils.video import FileVideoStream
import numpy as np
import os,imutils


cap = FileVideoStream('demo_scene/video_red0.mp4').start()
hog = cv2.HOGDescriptor()  
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
frame_index = 0
while True:
    frame = cap.read()
    frame = imutils.resize(frame, width=min(800, frame.shape[1]))
    (rects, weights) = hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.15)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
 
    for (x, y, w, h) in pick:
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
        newpath = os.path.join('myimages/' , str(frame_index) + ".jpg")
        cv2.imwrite(newpath,frame[y:h,x:w])
        frame_index = frame_index + 1
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == 27:
        break