import cv2
import numpy as np
import os

# 1. Đọc ảnh
base_dir = os.path.abspath(os.path.dirname(__file__))
img_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'images', 'inputs', 'anh_input1.jpg'))
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Không tìm thấy ảnh: {img_path}")

img = cv2.imread(img_path)
if img is None:
    raise ValueError(f"Không thể đọc ảnh: {img_path}")

# 2. Thêm nhiễu
def add_salt_pepper_noise(image, prob=0.02):
    """
    prob: xác suất một pixel bị nhiễu (0.02 = 2% số điểm ảnh bị nhiễu)
    """
    noisy_img = image.copy()
    h, w = image.shape[:2]

    # Số lượng điểm ảnh bị nhiễu
    num_noise_pixels = int(prob * h * w)

    # Nhiễu "muối" (điểm trắng)
    for _ in range(num_noise_pixels // 2):
        y = np.random.randint(0, h)
        x = np.random.randint(0, w)
        noisy_img[y, x] = 255

    # Nhiễu "tiêu" (điểm đen)
    for _ in range(num_noise_pixels // 2):
        y = np.random.randint(0, h)
        x = np.random.randint(0, w)
        noisy_img[y, x] = 0

    return noisy_img

img_noisy = add_salt_pepper_noise(img, prob=0.02)

# 3. LỌC TRUNG BÌNH
# Định nghĩa hàm mean_filter đơn giản

def mean_filter(image, kernel_size=3):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be an odd integer.")
    return cv2.blur(image, (kernel_size, kernel_size))

mean_filtered = mean_filter(img_noisy, kernel_size=5)

# 4. LƯU ẢNH KẾT QUẢ RA FILE
cv2.imwrite('anh_bi_nhieu.jpg', img_noisy)
cv2.imwrite('ket_qua_mean_filter.jpg', mean_filtered)
print("Đã lưu xong các ảnh kết quả!")

# 5. HIỂN THỊ KẾT QUẢ SO SÁNH
cv2.namedWindow('Anh goc', cv2.WINDOW_NORMAL)
cv2.namedWindow('Anh bi nhieu (Salt & Pepper)', cv2.WINDOW_NORMAL)
cv2.namedWindow('Loc trung binh', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Anh goc', 900, 700)
cv2.resizeWindow('Anh bi nhieu (Salt & Pepper)', 900, 700)
cv2.resizeWindow('Loc trung binh', 900, 700)

cv2.imshow('Anh goc', img)
cv2.imshow('Anh bi nhieu (Salt & Pepper)', img_noisy)
cv2.imshow('Loc trung binh', mean_filtered)

# Chờ nhấn phím bất kỳ để đóng cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()