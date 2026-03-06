import json
import os
import glob

# Load the scraped products
json_path = r"C:\Users\BIURODOM\Desktop\JTMeble-Web\src\data\scraped_products.json"
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find placeholder-like images
# e.g., default images like "https://jtmebel.pl/img/p/pl-default-home_default.jpg"
# We also notice that many items have "default_md" or "home_default" in their URL, but those might be actual images.
# Let's print out what we have.
placeholders = []
for p in data['products']:
    # identify if it looks like a generic placeholder
    img = p.get('image', '')
    if 'pl-default' in img or not img:
        placeholders.append(p)
    elif 'logo' in img:
        placeholders.append(p)

print(f"Products with generic placeholders: {len(placeholders)}")
for p in placeholders:
    print(f"{p['name']}: {p['image']}")

# Let's also check if the images listed in the JSON actually exist in the downloaded folder
download_dir = r"C:\Users\BIURODOM\Desktop\jtmebel_wget\jtmebel.pl"
missing_images = []
for p in data['products']:
    img_url = p.get('image', '')
    if img_url:
        # e.g. "https://jtmebel.pl/11321-default_md/tablica.jpg" -> "11321-default_md/tablica.jpg"
        rel_path = img_url.replace("https://jtmebel.pl/", "")
        local_path = os.path.join(download_dir, rel_path.replace('/', '\\'))
        if not os.path.exists(local_path):
            missing_images.append((p['name'], img_url, local_path))

print(f"\nImages from JSON not found in the downloaded folder: {len(missing_images)}")
for item in missing_images[:10]:
    print(item)
