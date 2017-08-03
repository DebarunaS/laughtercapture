### code to trigger webcam

# import numpy and opencv
import np as numpy
import cv2

# open default camera
cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)
cap.VideoCapture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH , 1024)

# prepare VideoWriter
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20.0, (640,480))


# run loop for each frame until 'Esc' pressed
while (cap.isOpened()):
  #get frame, save and display
  _, frame = cap.read()
  out.write(frame)
  cv2.imshow('Live', frame)
  
  if cv2.waitKey(1)==27:
    break;

# release camera and destroy display window
cap.release()
out.release()
cv2.destroyAllWindows()
