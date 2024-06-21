import os
import subprocess
from PIL import Image

def process_image(image_path, output_path, size):
    try:
        with Image.open(image_path) as img:
            img = img.resize(size, Image.LANCZOS)
            img.save(output_path)
        print(f"Обработано изображение {image_path}")
    except Exception as e:
        print(f"Не удалось обработать изображение {image_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                image_path = os.path.join(root, file)
                # Определяем размер для горизонтальных и вертикальных изображений
                try:
                    with Image.open(image_path) as img:
                        if img.width > img.height:
                            size = (760, 590)
                        else:
                            size = (442, 590)
                    
                    # Создаём новый путь для сохранения изменённого изображения
                    output_path = os.path.join(root, f"resized_{file}")
                    process_image(image_path, output_path, size)
                    
                    # Заменяем исходное изображение изменённым
                    os.remove(image_path)
                    os.rename(output_path, image_path)
                    
                except Exception as e:
                    print(f"Не удалось обработать изображение {image_path}: {e}")

process_directory("static/images/")
