import cv2
import os

# 1. Doc anh
base_dir = os.path.abspath(os.path.dirname(__file__))
img_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'images', 'inputs', 'anh_input3.jpg'))
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Khong tim thay anh: {img_path}")

img = cv2.imread(img_path)
if img is None:
    raise ValueError(f"Khong the doc anh: {img_path}")


# 2. Ham tao anh am ban
def negative_image(image):
    """
    Tao anh am ban bang cach dao nguoc gia tri tung diem anh: 255 - pixel.
    """
    return 255 - image


# 3. Ap dung
img_negative = negative_image(img)

# 4. Luu ket qua ra file
cv2.imwrite('anh_am_ban.jpg', img_negative)
print("Da luu xong anh am ban!")

# 5. Hien thi ket qua so sanh
cv2.namedWindow('Anh goc', cv2.WINDOW_NORMAL)
cv2.namedWindow('Anh am ban', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Anh goc', 900, 700)
cv2.resizeWindow('Anh am ban', 900, 700)

cv2.imshow('Anh goc', img)
cv2.imshow('Anh am ban', img_negative)

cv2.waitKey(0)
cv2.destroyAllWindows()
