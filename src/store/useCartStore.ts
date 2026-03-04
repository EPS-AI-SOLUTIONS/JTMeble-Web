import { create } from 'zustand';

export interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
}

interface CartStore {
  items: Product[];
  isOpen: boolean;
  addItem: (product: Product) => void;
  removeItem: (id: number) => void;
  toggleCart: () => void;
  clearCart: () => void;
}

export const useCartStore = create<CartStore>((set) => ({
  items: [],
  isOpen: false,
  addItem: (product) => set((state) => ({ items: [...state.items, product] })),
  removeItem: (id) => set((state) => ({ items: state.items.filter((item) => item.id !== id) })),
  toggleCart: () => set((state) => ({ isOpen: !state.isOpen })),
  clearCart: () => set({ items: [] }),
}));
