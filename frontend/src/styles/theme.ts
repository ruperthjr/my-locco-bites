export const theme = {
  colors: {
    // Primary - Bakery warmth inspired by design
    primary: '#FDC500',
    primaryLight: '#FFD633',
    primaryDark: '#E5B200',
    
    // Secondary - Bold accent
    secondary: '#E31837',
    secondaryLight: '#FF3D5C',
    secondaryDark: '#B31229',
    
    // Background
    background: '#150F0F',
    backgroundLight: '#1F1A1A',
    backgroundCard: '#2A2424',
    
    // Text
    text: '#FFFFFF',
    textSecondary: '#B8B8B8',
    textMuted: '#8A8A8A',
    
    // Grayscale
    black: '#000000',
    white: '#FFFFFF',
    gray: {
      50: '#F9F9F9',
      100: '#F0F0F0',
      200: '#E0E0E0',
      300: '#C4C4C4',
      400: '#A0A0A0',
      500: '#7A7A7A',
      600: '#5A5A5A',
      700: '#3A3A3A',
      800: '#2A2A2A',
      900: '#1A1A1A',
    },
    
    // Semantic colors
    success: '#10B981',
    warning: '#F59E0B',
    error: '#EF4444',
    info: '#3B82F6',
    
    // UI elements
    border: '#3A3A3A',
    divider: '#2A2A2A',
    overlay: 'rgba(0, 0, 0, 0.7)',
    shadow: 'rgba(0, 0, 0, 0.5)',
  },

  fonts: {
    primary: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    heading: "'Poppins', 'Inter', sans-serif",
    mono: "'Fira Code', 'Courier New', monospace",
  },

  fontSizes: {
    xs: '0.75rem',     // 12px
    sm: '0.875rem',    // 14px
    base: '1rem',      // 16px
    lg: '1.125rem',    // 18px
    xl: '1.25rem',     // 20px
    '2xl': '1.5rem',   // 24px
    '3xl': '1.875rem', // 30px
    '4xl': '2.25rem',  // 36px
    '5xl': '3rem',     // 48px
    '6xl': '3.75rem',  // 60px
  },

  fontWeights: {
    light: 300,
    regular: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
    extrabold: 800,
  },

  spacing: {
    xs: '0.25rem',   // 4px
    sm: '0.5rem',    // 8px
    md: '1rem',      // 16px
    lg: '1.5rem',    // 24px
    xl: '2rem',      // 32px
    '2xl': '3rem',   // 48px
    '3xl': '4rem',   // 64px
    '4xl': '6rem',   // 96px
    '5xl': '8rem',   // 128px
  },

  borderRadius: {
    none: '0',
    sm: '0.25rem',   // 4px
    base: '0.5rem',  // 8px
    md: '0.75rem',   // 12px
    lg: '1rem',      // 16px
    xl: '1.5rem',    // 24px
    '2xl': '2rem',   // 32px
    full: '9999px',
  },

  shadows: {
    sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
    base: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
    md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
    lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
    xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
    '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
    inner: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
    product: '8px 8px #FDC500', // Inspired by design
  },

  breakpoints: {
    xs: '320px',
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px',
    '2xl': '1536px',
  },

  transitions: {
    fast: '150ms ease-in-out',
    base: '200ms ease-in-out',
    slow: '300ms ease-in-out',
    slower: '500ms ease-in-out',
  },

  zIndex: {
    dropdown: 1000,
    sticky: 1020,
    fixed: 1030,
    modalBackdrop: 1040,
    modal: 1050,
    popover: 1060,
    tooltip: 1070,
  },
};

export type Theme = typeof theme;