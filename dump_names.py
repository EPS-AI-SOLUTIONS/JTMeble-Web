import json
file_path = r"C:\Users\BIURODOM\Desktop\JTMeble-Web\src\data\scraped_products.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
for i, p in enumerate(data.get('products', [])):
    print(f"{i}|{p.get('name')}|{p.get('category')}")
