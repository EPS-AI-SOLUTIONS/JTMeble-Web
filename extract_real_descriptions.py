import json
import os
import glob
from bs4 import BeautifulSoup
import re

json_path = r"C:\Users\BIURODOM\Desktop\JTMeble-Web\src\data\scraped_products.json"
base_dir = r"C:\Users\BIURODOM\Desktop\jtmebel_wget\jtmebel.pl"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated_count = 0

for product in data.get('products', []):
    name = product.get('name', '')
    
    # Try to find the file by name or similar. 
    # Since we don't have the exact URL of the product page, we can search the directory for HTML files that contain the product name.
    # Alternatively, we can find the image URL and derive the product ID, e.g. "https://jtmebel.pl/9950-home_default/biurko-office-bof12.jpg" -> "9950" is the image ID, but what is the product ID?
    # In Prestashop, the image ID doesn't necessarily match the product ID.
    # Let's search all HTML files in base_dir for the product name in the <title> or h1.
    # To make it faster, we can just search for the filename part of the image, e.g., "biurko-office-bof12.html"
    
    img_url = product.get('image', '')
    slug = ""
    if img_url:
        filename = img_url.split('/')[-1]
        slug = filename.replace('.jpg', '.html')
    
    if slug:
        # find files ending with this slug in any subdirectory
        search_pattern = os.path.join(base_dir, '**', f"*{slug}")
        matches = glob.glob(search_pattern, recursive=True)
        
        found_desc = None
        for match in matches:
            if not match.endswith('.html'):
                continue
                
            try:
                with open(match, 'r', encoding='utf-8', errors='ignore') as html_f:
                    soup = BeautifulSoup(html_f, 'html.parser')
                    desc_div = soup.find('div', class_='product__description')
                    if desc_div:
                        text = desc_div.get_text(separator=' ', strip=True)
                        if text and len(text) > 10:
                            found_desc = text
                            break
            except Exception as e:
                pass
                
        if found_desc:
            # Clean up the description
            found_desc = re.sub(r'\s+', ' ', found_desc)
            product['description'] = found_desc
            updated_count += 1
            print(f"Updated: {name} -> {found_desc[:50]}...")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully found and updated real descriptions for {updated_count} products.")
