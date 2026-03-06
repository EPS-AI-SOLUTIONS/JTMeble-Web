import json
import os
import glob
import re
import shutil

json_path = r"C:\Users\BIURODOM\Desktop\JTMeble-Web\src\data\scraped_products.json"
base_dir = r"C:\Users\BIURODOM\Desktop\jtmebel_wget\jtmebel.pl"
public_images_dir = r"C:\Users\BIURODOM\Desktop\JTMeble-Web\public\images\products"

# Create public images directory if it doesn't exist
os.makedirs(public_images_dir, exist_ok=True)

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated_count = 0
resolutions = ["product_main_2x", "product_main", "home_default", "default_md", "default_m", "default_xs"]

for product in data.get('products', []):
    img_url = product.get('image', '')
    if not img_url:
        continue
        
    # Example: https://jtmebel.pl/9950-home_default/biurko-office-bof12.jpg
    # Extract ID and filename
    match = re.search(r'/(\d+)-[a-zA-Z_]+/(.+)$', img_url)
    if not match:
        continue
        
    img_id = match.group(1)
    filename = match.group(2)
    
    # Find the highest resolution image locally
    best_local_img = None
    best_res_name = None
    
    for res in resolutions:
        test_path = os.path.join(base_dir, f"{img_id}-{res}", filename)
        if os.path.exists(test_path):
            best_local_img = test_path
            best_res_name = res
            break
            
    if best_local_img and best_res_name != "home_default" and best_res_name != "default_md":
        # We found a better resolution image!
        # Option A: Just update the URL to point to the better resolution on jtmebel.pl
        # Option B: Copy to public/images/products and use local path.
        # Let's just update the URL for now as it's the simplest and keeps the JSON clean.
        # Alternatively, downloading them to public/images/products ensures they don't break if jtmebel.pl changes.
        
        new_url = f"https://jtmebel.pl/{img_id}-{best_res_name}/{filename}"
        
        if product['image'] != new_url:
            print(f"Updated {filename} from {product['image'].split('/')[-2]} to {best_res_name}")
            product['image'] = new_url
            updated_count += 1

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully upgraded image resolutions for {updated_count} products.")
