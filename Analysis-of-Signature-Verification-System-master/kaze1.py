import cv2
import numpy as np
img = cv2.imread("fake.jpg", cv2.IMREAD_GRAYSCALE)
#sift = cv2.xfeatures2d.SIFT_create()
#surf = cv2.xfeatures2d.SURF_create()
orb = cv2.KAZE_create()
keypoints, descriptors = orb.detectAndCompute(img, None)
img = cv2.drawKeypoints(img, keypoints, None)
cv2.imshow("Image", img)
cv2.imwrite("kazekeypoints.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()