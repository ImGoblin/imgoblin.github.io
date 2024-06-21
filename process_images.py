import os
from PIL import Image

def process_image(image_path, size):
    try:
        with Image.open(image_path) as img:
            img = img.resize(size, Image.LANCZOS)
            img.save(image_path)
        print(f"Обработано изображение {image_path}")
    except Exception as e:
        print(f"Не удалось обработать изображение {image_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        # Определяем размеры для горизонтальных и вертикальных изображений
                        if img.width > img.height:
                            size = (760, 590)
                        else:
                            size = (442, 590)
                    
                    # Обрабатываем изображение
                    process_image(image_path, size)
                    
                except Exception as e:
                    print(f"Не удалось обработать изображение {image_path}: {e}")

if __name__ == "__main__":
    directory = "static/images/"
    process_directory(directory)
