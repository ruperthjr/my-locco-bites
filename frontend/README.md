# Locco Bites Frontend

Modern, AI-powered bakery e-commerce platform built with React, TypeScript, and Vite.

## Features

- AI-powered product recommendations and chat
- Voice ordering capabilities
- Real-time order tracking with live maps
- Custom cake designer with 3D preview
- Interactive product builders (pizza, sandwich, coffee)
- Loyalty rewards program
- Subscription management
- Multi-language support (EN, ES, FR)
- Real-time notifications via WebSocket
- Admin dashboard with analytics

## Tech Stack

- **Framework**: React 19 + TypeScript
- **Build Tool**: Vite
- **Routing**: React Router v6
- **State Management**: Zustand + TanStack Query
- **Styling**: Tailwind CSS
- **UI Components**: Radix UI
- **Animations**: Framer Motion
- **3D Graphics**: Three.js + React Three Fiber
- **Forms**: React Hook Form + Zod
- **Charts**: Recharts
- **Real-time**: Socket.IO Client

## Getting Started

### Prerequisites

- Node.js 18+ 
- pnpm 8+

### Installation

```bash
# Install dependencies
pnpm install

# Create environment file
cp .env.example .env.local

# Start development server
pnpm dev
```

### Available Scripts

- `pnpm dev` - Start development server
- `pnpm build` - Build for production
- `pnpm preview` - Preview production build
- `pnpm lint` - Run ESLint
- `pnpm type-check` - Run TypeScript type checking

## Project Structure

```
src/
├── components/     # Reusable UI components
├── pages/          # Page components
├── hooks/          # Custom React hooks
├── contexts/       # React contexts
├── store/          # Zustand stores
├── services/       # API services
├── utils/          # Utility functions
├── types/          # TypeScript types
├── styles/         # Global styles and theme
└── assets/         # Static assets
```

## Environment Variables

See `.env.example` for required environment variables.

## Development

The app runs on `http://localhost:5173` by default.

API requests are proxied to `http://localhost:8000` in development.

## Building for Production

```bash
pnpm build
```

The build output will be in the `dist/` directory.