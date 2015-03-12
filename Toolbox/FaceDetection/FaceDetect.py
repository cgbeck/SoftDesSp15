import numpy as np
import cv2
import sys

# import sys.path.append('/home/cbeck/opencv/data/haarcascades')
# import haarcascade_frontalface_alt.xml

kernel = np.ones((21,21),'uint8')
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('./FinalVideo.wlmp')
face_cascade = cv2.CascadeClassifier('/home/cbeck/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')

while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
	    frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
	    cv2.ellipse(frame,(x,y/4),((x+w)/2,(y+h)/3),0, 0, 180,(255,0,0))
	    cv2.circle(frame, (x/4,3*y/4), x/4, (0,0,0))
	    cv2.circle(frame, (3*x/4,3*y/4), x/4, (0,0,0))
	    # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
	 # Display the resulting frame
	print frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()