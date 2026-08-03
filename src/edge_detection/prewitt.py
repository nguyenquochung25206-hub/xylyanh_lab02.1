import cv2
import numpy as np


img1 = cv2.imread("anh_input1.jpg", 0)
img2 = cv2.imread("anh_input2.jpg", 0)
img3 = cv2.imread("anh_input3.jpg", 0)
kernelx = np.array(
      [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1],
      ]
)

kernely = np.array(
      [
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1],
      ]
)
prewittx = cv2.filter2D(img1, -1, kernelx)
prewitty = cv2.filter2D(img1, -1, kernely)

prewitt = cv2.addWeighted(prewittx, 0.5, prewitty, 0.5, 0)

cv2.imshow("Anh goc", img1)
cv2.imshow("Anh da xly", prewitt)

cv2.waitKey(0)
cv2.destroyAllows()
