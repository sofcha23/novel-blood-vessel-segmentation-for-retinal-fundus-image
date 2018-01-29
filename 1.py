import cv2
import glob
import numpy as np
kernel = np.ones((2,2), np.uint8)
for img in glob.glob("DRIVE/training/images/*.tif"):
    g = cv2.imread(img)
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    img_grey = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)
    img_grey=(255-img_grey)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img_grey)
    erosion = cv2.erode(cl1,kernel,iterations = 1)
    erosion=cv2.GaussianBlur(erosion,(5,5),0)
    opening = cv2.morphologyEx(cl1, cv2.MORPH_OPEN, kernel)
    cv2.imshow("op2",erosion)
    x=cv2.subtract(cl1,erosion)
    cv2.imshow("op1",x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
