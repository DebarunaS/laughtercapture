### code to trigger webcam

# import numpy and opencv
import np as numpy
import cv2

# open default camera
cap = cv2.VideoCapture(0)

# run loop for each frame until 'Esc' pressed
while (true):
  #get frame and display
  _, frame = cap.read()
  cv2.imshow('Live', frame)
  
  if cv2.waitKey(1)==27:
    break;

# release camera and destroy display window
cap.release()
cv2.destroyAllWindows()
