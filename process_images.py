import os
from PIL import Image, ImageOps

def process_image(image_path):
    try:
        with Image.open(image_path) as img:
            # Применяем метаданные EXIF для правильной ориентации
            img = ImageOps.exif_transpose(img)
            
            # Определяем наибольшую сторону и масштабируем изображение
            max_side = max(img.width, img.height)
            scale = 1000 / max_side
            new_size = (int(img.width * scale), int(img.height * scale))
            
            img = img.resize(new_size, Image.LANCZOS)
            img.save(image_path)
        print(f"Обработано изображение {image_path}")
    except Exception as e:
        print(f"Не удалось обработать изображение {image_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                image_path = os.path.join(root, file)
                process_image(image_path)

if __name__ == "__main__":
    directory = "static/images/"
    process_directory(directory)
