import os
from PIL import Image, ImageEnhance

images_dir = r"C:\Users\BIURODOM\Desktop\JTMeble-Web\public\images"

def enhance_image(image_path):
    try:
        with Image.open(image_path) as img:
            # Konwersja na RGB zeby uniknac problemow z przezroczystoscia JPG
            if img.mode != 'RGB':
                img = img.convert('RGB')
                
            # Zwiekszanie nasycenia
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.1)
            
            # Zwiekszanie kontrastu
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.1)
            
            # Wyostrzanie (Sharpness)
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.2)
            
            # Nadpisywanie z wysoka jakoscia
            img.save(image_path, quality=95)
            return True
    except Exception as e:
        print(f"Blad przy obrobce {image_path}: {e}")
        return False

success_count = 0
for file_name in os.listdir(images_dir):
    if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
        file_path = os.path.join(images_dir, file_name)
        if enhance_image(file_path):
            success_count += 1

print(f"Pomyslnie ulepszono {success_count} zdjec (Ostrość, Kontrast, Nasycenie).")
