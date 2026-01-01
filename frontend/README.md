# Locco Bites Frontend
[![React](https://img.shields.io/badge/React-19.2.0-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9.3-blue.svg)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-7.2.4-646CFF.svg)](https://vitejs.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](/LICENSE))

## Features

### Core Features
- **E-commerce Platform** - Complete online ordering system
- **AI Recommendations** - Personalized product suggestions
- **Voice Ordering** - Hands-free shopping experience
- **Real-time Order Tracking** - Live delivery tracking with maps
- **Custom Product Designer** - 3D cake customization studio
- **Multiple Payment Options** - Stripe, PayPal, Apple Pay, Google Pay
- **Real-time Notifications** - WebSocket-based updates

### Advanced Features
- **Custom Cake Designer** - Interactive 3D cake builder with live preview
- **Coffee Customizer** - Build your perfect coffee drink
- **Sandwich Builder** - Create custom sandwiches
- **Loyalty Rewards Program** - Points and rewards system
- **Subscription Management** - Recurring orders and subscriptions
- **Multi-language Support** - English, Spanish, French
- **Progressive Web App** - Installable on mobile devices
- **Admin Dashboard** - Comprehensive analytics and management

## Tech Stack

### Frontend Framework
- **React 19.2** - Latest React with concurrent features
- **TypeScript 5.9** - Type-safe development
- **Vite 7.2** - Lightning-fast build tool

### State Management
- **Zustand** - Lightweight state management
- **TanStack Query** - Server state management & caching
- **React Context** - Local state management

### UI & Styling
- **Tailwind CSS** - Utility-first CSS framework
- **Radix UI** - Accessible component primitives
- **Framer Motion** - Smooth animations
- **Lucide Icons** - Beautiful icon library

### Forms & Validation
- **React Hook Form** - Performant form management
- **Zod** - TypeScript-first schema validation

### 3D & Graphics
- **Three.js** - 3D graphics library
- **React Three Fiber** - React renderer for Three.js
- **React Three Drei** - Useful helpers for R3F

### Data Visualization
- **Recharts** - Composable charting library

### Real-time Communication
- **Socket.IO Client** - WebSocket communication

### Utilities
- **Axios** - HTTP client
- **date-fns** - Modern date utility library
- **clsx & tailwind-merge** - Conditional styling

## Prerequisites

- **Node.js**: v18.0.0 or higher
- **pnpm**: v8.0.0 or higher (recommended package manager)
- **Backend API**: FastAPI backend running on port 8000

## Installation

### 1. Install pnpm globally

```bash
npm install -g pnpm
```

### 2. Clone the repository

```bash
git clone https://github.com/ruperthjr/my-locco-bites.git
cd frontend
```

### 3. Install dependencies

Quick install:
```bash
pnpm install
```

### 4. Configure environment

```bash
cp .env.example .env.local
```

Edit `.env.local` with your configuration.

### 5. Start development server

```bash
pnpm dev
```

Visit `http://localhost:5173` in your browser.

## Available Scripts

| Command | Description |
|---------|-------------|
| `pnpm dev` | Start development server on port 5173 |
| `pnpm build` | Build for production |
| `pnpm preview` | Preview production build |
| `pnpm lint` | Run ESLint |
| `pnpm type-check` | Run TypeScript type checking |


## Key Features Detail

### AI-Powered Features
- **Smart Recommendations** - ML-based product suggestions
- **Voice Assistant** - Natural language ordering
- **Image Search** - Find products by uploading images
- **Chat Support** - AI-powered customer service

### Customization Studio
- **3D Cake Designer** - Visual cake builder with real-time preview
- **Coffee Builder** - Customize size, strength, milk, syrups
- **Sandwich Builder** - Layer-by-layer sandwich creation
- **AR Preview** - View products in augmented reality

### E-commerce
- **Product Catalog** - Browse by category with filters
- **Smart Search** - Autocomplete with suggestions
- **Shopping Cart** - Persistent cart with recommendations
- **Wishlist** - Save favorites for later
- **Reviews & Ratings** - Customer feedback system

### Order Management
- **Real-time Tracking** - Live order status updates
- **Order History** - Complete purchase history
- **Reorder** - Quick reorder from history
- **Custom Orders** - Special requests and notes

### Admin Dashboard
- **Analytics** - Sales, customers, products, traffic
- **Product Management** - CRUD operations with bulk actions
- **Order Management** - Process and track orders
- **Customer Management** - User profiles and segments
- **Inventory Management** - Stock levels and alerts
- **Marketing Tools** - Campaigns, coupons, promotions

## Environment Variables

Required variables for `.env.local`:

```bash
VITE_API_BASE_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
```

See `.env.example` for all available configuration options.

## API Integration

The frontend connects to a FastAPI backend. API requests are proxied in development:

```typescript
// vite.config.ts
proxy: {
  '/api': {
    target: 'http://localhost:8000',
    changeOrigin: true,
  },
  '/ws': {
    target: 'ws://localhost:8000',
    ws: true,
  },
}
```

## Testing

```bash
# Run tests (when configured)
pnpm test

# Run tests with coverage
pnpm test:coverage

# Run e2e tests
pnpm test:e2e
```

##  Building for Production

```bash
# Build the application
pnpm build

# Preview the production build
pnpm preview
```

The build output will be in the `dist/` directory.

### Build Optimization
- Code splitting by route and vendor
- Tree shaking for unused code
- Minification and compression
- Asset optimization
- Source maps for debugging

## Deployment

### Vercel
```bash
vercel deploy
```

### Netlify
```bash
netlify deploy --prod
```

### Docker
```bash
docker build -t locco-bites-frontend .
docker run -p 3000:3000 locco-bites-frontend
```

## Code Style

This project uses:
- **ESLint** for code linting
- **Prettier** for code formatting
- **TypeScript** for type safety

Run linting before committing:
```bash
pnpm lint
pnpm type-check
```

##  Troubleshooting

### Common Issues

**Port already in use**
```bash
# Change port in vite.config.ts or use:
PORT=3000 pnpm dev
```

**Module not found**
```bash
# Clear cache and reinstall
pnpm store prune
rm -rf node_modules
pnpm install
```

**TypeScript errors**
```bash
# Rebuild TypeScript
pnpm type-check
```

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.
