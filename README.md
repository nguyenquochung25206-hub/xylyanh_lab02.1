# Image Processing - Chapter 2

## Giới thiệu

Đây là bài thực hành Chương 2 môn **Xử lý ảnh và Thị giác máy tính**.

Project được xây dựng bằng **Python** và **OpenCV**, thực hiện các thuật toán xử lý ảnh cơ bản bao gồm:

- Toán tử điểm ảnh
- Lọc tuyến tính
- Phát hiện cạnh
- Bộ lọc phi tuyến
- Kernel tùy chỉnh

---

## Thành viên nhóm

| STT | Họ và tên | Công việc |
|-----|-----------|-----------|
| 1 | Nguyễn Thị Xuân Mai | Brightness |
| 2 | Lê Gia Huy  | Contrast, Negative, Threshold |
| 3 | Lương Hoàng Phúc | Mean Filter |
| 4 | Hoàng Đỗ Gia Huy | Gaussian Filter, Sharpen |
| 5 | Lê Thị Lan My    | Sobel, Prewitt |
| 6 | ................ | Median, Bilateral, Custom Kernel |
| 7 | ................ | Main Program, Testing, Integration |

---

## Cấu trúc Project

```
ImageProcessing_Chapter2/
│
├── README.md
├── requirements.txt
├── main.py
│
├── images/
│   ├── input/
│   └── output/
│
└── src/
    ├── point_operations/
    ├── linear_filters/
    ├── edge_detection/
    ├── nonlinear_filters/
    ├── custom_kernel/
    └── utils/
```

---

## Chức năng

### I. Toán tử điểm ảnh

- Điều chỉnh độ sáng (Brightness)
- Điều chỉnh độ tương phản (Contrast)
- Ảnh âm bản (Negative)
- Phân ngưỡng (Threshold)

---

### II. Lọc tuyến tính

- Mean Filter
- Gaussian Filter
- Sharpen Filter

---

### III. Bài tập nâng cao

- Sobel Edge Detection
- Prewitt Edge Detection
- Median Filter
- Bilateral Filter
- Custom Kernel

---

## Công nghệ sử dụng

- Python 3.x
- OpenCV
- NumPy
- Pillow
- Matplotlib

---

## Cài đặt

Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

---

## Chạy chương trình

```bash
python main.py
```

Sau khi chạy chương trình sẽ hiển thị menu để lựa chọn thuật toán xử lý ảnh.

---

## Thư mục ảnh

### Ảnh đầu vào

```
images/input/
```

Chứa các ảnh gốc dùng để xử lý.

### Ảnh đầu ra

```
images/output/
```

Chứa kết quả sau khi xử lý bằng từng thuật toán.

---

## Yêu cầu hệ thống

- Python 3.10 trở lên
- Windows 10/11
- OpenCV 4.x

---

## Ghi chú

- Mỗi thuật toán được cài đặt trong một file Python riêng.
- Các thuật toán có thể chạy độc lập hoặc thông qua `main.py`.
- Kết quả xử lý sẽ được lưu vào thư mục `images/output`.

---

## Giấy phép

Project được thực hiện phục vụ mục đích học tập tại trường đại học.
