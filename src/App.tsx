import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import CartDrawer from './components/CartDrawer';
import Home from './pages/Home';
import About from './pages/About';
import Offer from './pages/Offer';
import Category from './pages/Category';
import Contact from './pages/Contact';
import Laboratoria from './pages/Laboratoria';

export default function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col bg-gray-50 dark:bg-gray-950 text-gray-900 dark:text-gray-100 font-sans transition-colors">
        <Navbar />
        <CartDrawer />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/o-nas" element={<About />} />
            <Route path="/oferta" element={<Offer />} />
            <Route path="/oferta/:slug" element={<Category />} />
            <Route path="/kontakt" element={<Contact />} />
            <Route path="/laboratoria" element={<Laboratoria />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}
