# code to trigger webcam
import np as numpy
import cv2

cap = cv2.VideoCapture(0)

while (true):
  _, frame = cap.read()
  cv2.imshow('Live', frame)
  
  if cv2.waitKey(1)==0:
    break;
    
cap.release()
cv2.destroyAllWindows()
  
