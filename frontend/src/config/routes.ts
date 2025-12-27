export const ROUTES = {
  HOME: '/',
  MENU: '/menu',
  CUSTOM_ORDER: '/custom-order',
  PIZZA_BUILDER: '/custom-order/pizza',
  CAKE_DESIGNER: '/custom-order/cake',
  CART: '/cart',
  CHECKOUT: '/checkout',
  PAYMENT: '/checkout/payment',
  ORDER_CONFIRMATION: '/order/confirmation/:orderId',
  TRACK_ORDER: '/track/:orderId',
  SUBSCRIPTIONS: '/subscriptions',
  LOYALTY: '/loyalty',
  ABOUT: '/about',
  CONTACT: '/contact',
  GALLERY: '/gallery',
  ADMIN: '/admin',
  ADMIN_DASHBOARD: '/admin/dashboard',
  ADMIN_ORDERS: '/admin/orders',
  ADMIN_INVENTORY: '/admin/inventory',
} as const;

export type RouteKey = keyof typeof ROUTES;
export type RoutePath = (typeof ROUTES)[RouteKey];