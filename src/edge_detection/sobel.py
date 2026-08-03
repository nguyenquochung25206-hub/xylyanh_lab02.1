import cv2

img1 = cv2.imread("anh_input1.jpg", 0)
img2 = cv2.imread("anh_input2.jpg", 0)
img3 = cv2.imread("anh_input3.jpg", 0)

sobelx = cv2.Sobel(img1, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img1, cv2.CV_64F, 0, 1)

sobel1 = cv2.addWeighted(
    cv2.convertScaleAbs(sobelx),
    0.5,
    cv2.convertScaleAbs(sobely),
    0.5,
    0
)

cv2.imshow("Original", img1)
cv2.imshow("Sobel", sobel1)
cv2.waitKey(0)
