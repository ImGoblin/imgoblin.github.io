import os
from PIL import Image

def process_image(file_path):
    try:
        img = Image.open(file_path)
        width, height = img.size
        if width > height:
            new_width, new_height = 760, 590
        else:
            new_width, new_height = 442.5, 590

        img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        img.save(file_path)
        print(f"Processed and resized image: {file_path}")
    except Exception as e:
        print(f"Failed to process image {file_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                process_image(os.path.join(root, file))

if __name__ == "__main__":
    process_directory("images")  # Замените на путь к вашему каталогу изображений
