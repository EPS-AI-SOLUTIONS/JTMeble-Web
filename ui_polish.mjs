import fs from 'fs';
import path from 'path';

const srcDir = 'C:\\Users\\BIURODOM\\Desktop\\JTMeble-Web\\src';

// 1. Zmiana głównych stylów (index.css) - dodanie gradientowego, nowoczesnego tła
let cssPath = path.join(srcDir, 'index.css');
let cssContent = fs.readFileSync(cssPath, 'utf8');
cssContent = cssContent.replace(
  '@apply bg-gray-50 dark:bg-gray-950 text-gray-900 dark:text-gray-100 transition-colors duration-300;',
  '@apply bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-blue-50 via-gray-50 to-white dark:from-gray-900 dark:via-gray-950 dark:to-black text-gray-900 dark:text-gray-100 transition-colors duration-500 min-h-screen;'
);
fs.writeFileSync(cssPath, cssContent);

// 2. Wygładzenie Home.tsx (bardziej miękkie karty, efekt szkła w hero)
let homePath = path.join(srcDir, 'pages', 'Home.tsx');
let homeContent = fs.readFileSync(homePath, 'utf8');

// Poprawki na styl kart
homeContent = homeContent.replace(/rounded-2xl/g, 'rounded-[2rem]');
homeContent = homeContent.replace(/shadow-sm/g, 'shadow-xl shadow-blue-900\/5');
homeContent = homeContent.replace(/shadow-lg/g, 'shadow-2xl shadow-blue-900\/10');

// Lepsze Hero
homeContent = homeContent.replace(
  'bg-black/50',
  'bg-gradient-to-b from-black/60 via-black/40 to-black/80 backdrop-blur-[2px]'
);

// Bardziej nowoczesne przyciski
homeContent = homeContent.replace(
  'rounded-full font-medium text-lg',
  'rounded-full font-bold text-lg shadow-lg shadow-blue-500/30'
);

fs.writeFileSync(homePath, homeContent);

// 3. Wygładzenie Navbar.tsx (zwiększenie efektu rozmycia i paddingu)
let navPath = path.join(srcDir, 'components', 'Navbar.tsx');
let navContent = fs.readFileSync(navPath, 'utf8');
navContent = navContent.replace('bg-white/80 dark:bg-gray-900/80 backdrop-blur-md', 'bg-white/70 dark:bg-gray-950/70 backdrop-blur-xl supports-[backdrop-filter]:bg-white/60');
fs.writeFileSync(navPath, navContent);

console.log("Super-nowoczesny UI Polish (Glassmorphism, Gradients) zakonczony!");
