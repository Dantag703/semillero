import cv2
import imutils
from Human_Detection import Detector

img = cv2.imread("t2.jpg")
print (img)
img = imutils.resize(img, width=1000)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()