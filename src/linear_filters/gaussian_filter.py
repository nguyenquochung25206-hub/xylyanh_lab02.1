import cv2
import numpy as np
from pathlib import Path
try:
    from PIL import Image # type: ignore
except ImportError:
    Image = None


def apply_gaussian_filter(image, kernel_size=5, sigma=0):
    """
    Áp dụng bộ lọc Gaussian lên ảnh đầu vào.
    """
    if kernel_size % 2 == 0:
        raise ValueError("kernel_size phải là số lẻ (3,5,7,...)")
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)


def create_sample_image(input_dir: Path) -> Path:
    """Tạo một ảnh mẫu nếu thư mục đầu vào chưa có ảnh nào."""
    input_dir.mkdir(parents=True, exist_ok=True)
    sample_path = input_dir / "sample_input.png"

    if not sample_path.exists():
        image = np.zeros((400, 600, 3), dtype=np.uint8)
        image[:, :, 0] = 120
        image[:, :, 1] = 160
        image[:, :, 2] = 220
        cv2.putText(image, "Sample Image", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
        cv2.rectangle(image, (80, 90), (520, 310), (255, 255, 255), 3)
        cv2.circle(image, (300, 200), 90, (255, 255, 255), 3)
        cv2.imwrite(str(sample_path), image)
        print(f" Đã tạo ảnh mẫu tại: {sample_path}")

    return sample_path


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    input_dir = project_root / "images" / "inputs"
    output_dir = Path(r"D:\Xử lý ảnh\xylyanh021\images\outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    sample_image_path = create_sample_image(input_dir)

    valid_ext = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif')
    image_files = [p for p in input_dir.iterdir() if p.is_file() and p.suffix.lower() in valid_ext]

    if not image_files:
        print(f" Không tìm thấy ảnh nào trong thư mục '{input_dir}'.")
    else:
        img_path = image_files[0]
        try:
            image_bytes = img_path.read_bytes()
            img_array = np.frombuffer(image_bytes, dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        except Exception as exc:
            print(f" Không thể đọc ảnh '{img_path}'. Lỗi: {exc}")
            img = None

        if img is None:
            print(f" Không thể đọc ảnh '{img_path}'. Kiểm tra lại file.")
        else:
            result = apply_gaussian_filter(img, kernel_size=5, sigma=0)
            out_path = output_dir / f"{img_path.stem}_gaussian.png"
            if Image is not None:
                pil_image = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
                pil_image.save(out_path)
            else:
                cv2.imwrite(str(out_path), result)
            print(f" Đã lưu ảnh Gaussian tại: {out_path}")
