import fs from 'fs';
import path from 'path';

const pagesDir = 'C:\\Users\\BIURODOM\\Desktop\\JTMeble-Web\\src\\pages';
const compDir = 'C:\\Users\\BIURODOM\\Desktop\\JTMeble-Web\\src\\components';

function replaceFallbacks(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            replaceFallbacks(fullPath);
        } else if (fullPath.endsWith('.tsx')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            // Zastępowanie wszelkich linków Unsplash domyślnymi ulepszonymi obrazami z katalogu JTMeble
            let newContent = content
                .replace(/'https:\/\/images\.unsplash\.com\/photo-1555041469-a586c61ea9bc\?auto=format&fit=crop&q=80'/g, "'/images/hero-bg-1.jpg'")
                .replace(/'https:\/\/images\.unsplash\.com\/photo-1556910103-1c02745a872f\?auto=format&fit=crop&q=80'/g, "'/images/hero-bg-2.jpg'")
                .replace(/'https:\/\/images\.unsplash\.com\/photo-1595526114035-0d45ed16cfbf\?auto=format&fit=crop&q=80'/g, "'/images/hero-bg-3.jpg'")
                .replace(/'https:\/\/images\.unsplash\.com\/photo-1497366216548-37526070297c\?auto=format&fit=crop&q=80'/g, "'/images/product-1.jpg'")
                .replace(/'https:\/\/images\.unsplash\.com\/photo-1581091226825-a6a2a5aee158\?auto=format&fit=crop&q=80'/g, "'/images/hero-bg-6.jpg'")
                .replace(/'https:\/\/images\.unsplash\.com\/photo-1540555700478-4be289fbecef\?auto=format&fit=crop&q=80'/g, "'/images/hero-bg-7.jpg'");
            
            if (content !== newContent) {
                fs.writeFileSync(fullPath, newContent);
                console.log(`Zaktualizowano plik: ${file}`);
            }
        }
    }
}

replaceFallbacks(pagesDir);
replaceFallbacks(compDir);

// Zastąpienie fallbacków w katalogu JSON (jesli wystepuja)
const catalogPath = 'C:\\Users\\BIURODOM\\Desktop\\JTMeble-Web\\src\\data\\catalog.json';
let catalogContent = fs.readFileSync(catalogPath, 'utf8');
let newCatalogContent = catalogContent.replace(/"image": "\/images\/hero-bg-2.jpg"/g, '"image": "/images/logo-1641375366.jpg"');
if(catalogContent !== newCatalogContent) {
    fs.writeFileSync(catalogPath, newCatalogContent);
    console.log("Zaktualizowano domyslne obrazki w bazie produktów JSON.");
}
