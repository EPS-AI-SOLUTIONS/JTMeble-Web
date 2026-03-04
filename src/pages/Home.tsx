import { motion } from 'motion/react';
import { ChevronRight } from 'lucide-react';

export default function Home() {
  return (
    <>
      <section className="relative h-screen flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img
            src="/images/hero-bg-1.jpg"
            alt="Nowoczesne meble"
            className="w-full h-full object-cover"
            onError={(e) => {
              e.currentTarget.src =
                'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&q=80';
            }}
          />
          <div className="absolute inset-0 bg-black/50" />
        </div>

        <div className="relative z-10 text-center px-4 max-w-5xl mx-auto mt-16">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-4xl sm:text-6xl lg:text-7xl font-bold text-white tracking-tight"
          >
            Tworzymy{' '}
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-amber-300">
              przestrzeń
            </span>{' '}
            Twoich marzeń
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="mt-6 text-xl sm:text-2xl text-gray-200 max-w-3xl mx-auto font-light"
          >
            Meble na wymiar najwyższej jakości. Od projektu po montaż. Zadbamy o każdy detal w Twoim
            domu i biurze.
          </motion.p>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="mt-10 flex flex-col sm:flex-row gap-4 justify-center"
          >
            <button className="px-8 py-4 bg-orange-500 hover:bg-orange-600 text-white rounded-full font-medium text-lg transition-colors flex items-center justify-center group">
              Zobacz ofertę
              <ChevronRight className="ml-2 group-hover:translate-x-1 transition-transform" />
            </button>
          </motion.div>
        </div>
      </section>

      <section className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900">Nasze Specjalizacje</h2>
            <div className="mt-4 w-24 h-1 bg-orange-500 mx-auto rounded-full"></div>
            <p className="mt-6 text-lg text-gray-600 max-w-2xl mx-auto">
              Projektujemy i wykonujemy meble dostosowane do Twoich potrzeb.
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                title: 'Kuchnie na wymiar',
                img: '/images/hero-bg-2.jpg',
                fallback:
                  'https://images.unsplash.com/photo-1556910103-1c02745a872f?auto=format&fit=crop&q=80',
              },
              {
                title: 'Szafy i Garderoby',
                img: '/images/hero-bg-3.jpg',
                fallback:
                  'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&q=80',
              },
              {
                title: 'Meble Biurowe',
                img: '/images/product-1.jpg',
                fallback:
                  'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80',
              },
            ].map((item, idx) => (
              <motion.div
                key={idx}
                whileHover={{ y: -10 }}
                className="group relative rounded-2xl overflow-hidden shadow-lg cursor-pointer h-96"
              >
                <img
                  src={item.img}
                  alt={item.title}
                  className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                  onError={(e) => {
                    e.currentTarget.src = item.fallback;
                  }}
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-8">
                  <h3 className="text-2xl font-bold text-white mb-2">{item.title}</h3>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-20 bg-gray-900 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
            {[
              { number: '15+', label: 'Lat doświadczenia' },
              { number: '2000+', label: 'Zrealizowanych projektów' },
              { number: '100%', label: 'Gwarancja jakości' },
              { number: 'Zadowoleni', label: 'Klienci w całej Polsce' },
            ].map((stat, idx) => (
              <div key={idx} className="p-6">
                <div className="text-4xl md:text-5xl font-bold text-orange-500 mb-2">
                  {stat.number}
                </div>
                <div className="text-gray-400 font-medium uppercase tracking-wider text-sm">
                  {stat.label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
