import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread("anh_input3.jpg")

# Tăng độ sáng
value = 50
bright = cv2.convertScaleAbs(img, alpha=1.0, beta=50)

# Giảm độ sáng
dark = cv2.convertScaleAbs(img, alpha=1.0, beta=-30)

# Hiển thị
cv2.imshow("Original", img)
cv2.imshow("Bright", bright)
cv2.imshow("Dark", dark)

cv2.imwrite("anh_sang.png", bright)
cv2.imwrite("anh_toi.png", dark)


cv2.waitKey(0)
cv2.destroyAllWindows()
