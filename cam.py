first download libraries
import cv2
s = cv2.videoCapture(0)
ret,image = s.read()
cv2.imwrite("c:\\users\\taha\\desktop\\tsha.png",image)
del(s)
