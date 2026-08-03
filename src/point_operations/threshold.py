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

# Chuyen sang anh xam vi Threshold thuong ap dung tren anh 1 kenh
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 2. Ham phan nguong
def apply_threshold(image_gray, thresh_value=127, max_value=255, method=cv2.THRESH_BINARY):
    """
    Phan nguong anh xam.

    Tham so:
        image_gray : anh xam (1 kenh mau)
        thresh_value: gia tri nguong
        max_value   : gia tri gan cho pixel vuot nguong
        method      : kieu phan nguong (cv2.THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC, ...)
    """
    _, ket_qua = cv2.threshold(image_gray, thresh_value, max_value, method)
    return ket_qua


# 3. Ap dung cac kieu phan nguong
img_binary = apply_threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
img_binary_inv = apply_threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
img_trunc = apply_threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)

# 4. Luu ket qua ra file
cv2.imwrite('anh_xam.jpg', img_gray)
cv2.imwrite('anh_threshold_binary.jpg', img_binary)
cv2.imwrite('anh_threshold_binary_inv.jpg', img_binary_inv)
cv2.imwrite('anh_threshold_trunc.jpg', img_trunc)
print("Da luu xong cac anh ket qua!")

# 5. Hien thi ket qua so sanh
cv2.namedWindow('Anh goc', cv2.WINDOW_NORMAL)
cv2.namedWindow('Anh xam', cv2.WINDOW_NORMAL)
cv2.namedWindow('Threshold Binary', cv2.WINDOW_NORMAL)
cv2.namedWindow('Threshold Binary Inv', cv2.WINDOW_NORMAL)
cv2.namedWindow('Threshold Trunc', cv2.WINDOW_NORMAL)

for ten_cua_so in ['Anh goc', 'Anh xam', 'Threshold Binary', 'Threshold Binary Inv', 'Threshold Trunc']:
    cv2.resizeWindow(ten_cua_so, 900, 700)

cv2.imshow('Anh goc', img)
cv2.imshow('Anh xam', img_gray)
cv2.imshow('Threshold Binary', img_binary)
cv2.imshow('Threshold Binary Inv', img_binary_inv)
cv2.imshow('Threshold Trunc', img_trunc)

cv2.waitKey(0)
cv2.destroyAllWindows()
