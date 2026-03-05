import { motion } from 'motion/react';
import { X, ShoppingCart } from 'lucide-react';
import { useCartStore } from '../store/useCartStore';

interface Product {
  name: string;
  price: string;
  image: string;
  category: string;
  description?: string;
}

interface ProductModalProps {
  product: Product;
  onClose: () => void;
  idx: number;
}

export default function ProductModal({ product, onClose, idx }: ProductModalProps) {
  const addItem = useCartStore((state) => state.addItem);

  // Zabezpieczenie przed brakiem obrazka
  const imageUrl = product.image && product.image.trim() !== '' ? product.image : '/images/hero-bg-1.jpg';

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      onClick={onClose}
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
    >
      <motion.div
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.95, y: 20 }}
        onClick={(e) => e.stopPropagation()}
        className="bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-5xl overflow-hidden flex flex-col md:flex-row relative max-h-[90vh]"
      >
        <button
          onClick={onClose}
          className="absolute right-4 top-4 z-10 p-2 bg-white/80 dark:bg-gray-800/80 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full backdrop-blur-sm transition-colors"
        >
          <X size={20} className="text-gray-600 dark:text-gray-300" />
        </button>

        {/* Obraz */}
        <div className="w-full md:w-1/2 bg-white dark:bg-white p-8 flex items-center justify-center min-h-[300px] border-r border-gray-100 dark:border-gray-800">
          <img
            src={imageUrl}
            alt={product.name}
            className="max-w-full max-h-[400px] object-contain drop-shadow-sm"
            onError={(e) => {
              (e.target as HTMLImageElement).src = '/images/hero-bg-1.jpg';
            }}
          />
        </div>

        {/* Szczegóły */}
        <div className="w-full md:w-1/2 p-8 flex flex-col overflow-y-auto">
          <p className="text-sm font-semibold text-blue-600 mb-2 uppercase tracking-wider">{product.category}</p>
          <h2 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-6 leading-tight">{product.name}</h2>
          
          <div className="prose dark:prose-invert max-w-none mb-8 text-gray-600 dark:text-gray-400">
            {product.description ? (
              <p className="leading-relaxed text-base">{product.description}</p>
            ) : (
              <p className="italic">Brak szczegółowego opisu dla tego produktu.</p>
            )}
          </div>

          <div className="mt-auto flex flex-col sm:flex-row items-start sm:items-center justify-between pt-6 border-t border-gray-100 dark:border-gray-800 gap-4">
            <div className="flex flex-col shrink-0">
              <span className="text-sm text-gray-500 dark:text-gray-400 mb-1">Cena netto</span>
              <span className="text-2xl font-bold text-gray-900 dark:text-white">
                {product.price || 'Zapytaj o cenę'}
              </span>
            </div>
            
            <button
              onClick={() => {
                addItem({
                  id: `${product.name}-${idx}`,
                  name: product.name,
                  price: product.price ? parseFloat(product.price.replace(/[^\d,.-]/g, '').replace(',', '.')) : 0,
                  image: imageUrl,
                  category: product.category,
                  quantity: 1
                });
                onClose();
              }}
              className="flex items-center justify-center gap-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-medium transition-colors shadow-lg shadow-blue-600/20 w-full sm:w-auto"
            >
              <ShoppingCart size={20} />
              <span>Dodaj do zapytania</span>
            </button>
          </div>
        </div>
      </motion.div>
    </motion.div>
  );
}
