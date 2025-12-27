export const APP_CONFIG = {
  name: import.meta.env.VITE_APP_NAME || 'Locco Bites',
  description: import.meta.env.VITE_APP_DESCRIPTION || 'Artisan Bakery & Custom Confections',
  locale: import.meta.env.VITE_DEFAULT_LOCALE || 'en-US',
  currency: import.meta.env.VITE_CURRENCY || 'KES',
} as const;

export const API_CONFIG = {
  baseUrl: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1',
  wsUrl: import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws',
  timeout: 30000,
} as const;

export const FEATURE_FLAGS = {
  aiChat: import.meta.env.VITE_ENABLE_AI_CHAT === 'true',
  voiceOrder: import.meta.env.VITE_ENABLE_VOICE_ORDER === 'true',
  subscriptions: import.meta.env.VITE_ENABLE_SUBSCRIPTIONS === 'true',
  loyalty: import.meta.env.VITE_ENABLE_LOYALTY === 'true',
  realTime: import.meta.env.VITE_ENABLE_REAL_TIME === 'true',
} as const;

export const ORDER_STATUS = {
  PENDING: 'pending',
  CONFIRMED: 'confirmed',
  PREPARING: 'preparing',
  READY: 'ready',
  OUT_FOR_DELIVERY: 'out_for_delivery',
  DELIVERED: 'delivered',
  CANCELLED: 'cancelled',
} as const;

export const PAYMENT_STATUS = {
  PENDING: 'pending',
  PROCESSING: 'processing',
  COMPLETED: 'completed',
  FAILED: 'failed',
  REFUNDED: 'refunded',
} as const;

export const DIETARY_OPTIONS = [
  { value: 'vegetarian', label: 'Vegetarian', emoji: '🥗' },
  { value: 'vegan', label: 'Vegan', emoji: '🌱' },
  { value: 'gluten-free', label: 'Gluten Free', emoji: '🌾' },
  { value: 'dairy-free', label: 'Dairy Free', emoji: '🥛' },
  { value: 'nut-free', label: 'Nut Free', emoji: '🥜' },
  { value: 'keto', label: 'Keto', emoji: '🥑' },
] as const;

export const PRODUCT_CATEGORIES = [
  { id: 'breads', name: 'Breads', emoji: '🍞' },
  { id: 'pastries', name: 'Pastries', emoji: '🥐' },
  { id: 'cakes', name: 'Cakes', emoji: '🎂' },
  { id: 'cookies', name: 'Cookies', emoji: '🍪' },
  { id: 'pizzas', name: 'Pizzas', emoji: '🍕' },
  { id: 'custom', name: 'Custom Orders', emoji: '✨' },
] as const;

export const DELIVERY_OPTIONS = [
  { id: 'pickup', name: 'Pickup', icon: '🏪', estimatedTime: '15-30 mins' },
  { id: 'delivery', name: 'Delivery', icon: '🚚', estimatedTime: '45-60 mins' },
] as const;

export const PAGINATION = {
  defaultPageSize: 12,
  pageSizeOptions: [12, 24, 36, 48],
} as const;

export const LOCAL_STORAGE_KEYS = {
  cart: 'locco-bites-cart',
  user: 'locco-bites-user',
  preferences: 'locco-bites-preferences',
  recentOrders: 'locco-bites-recent-orders',
} as const;

export const ANIMATION_DURATION = {
  fast: 150,
  normal: 300,
  slow: 500,
} as const;

export const TOAST_DURATION = {
  short: 2000,
  medium: 4000,
  long: 6000,
} as const;