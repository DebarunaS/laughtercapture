### code to trigger webcam

# import numpy and opencv
import numpy as np
import cv2

# open default camera
cap = cv2.VideoCapture(0)

# prepare VideoWriter
out = cv2.VideoWriter('../output.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20.0, (640,480))


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
