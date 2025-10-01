import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  // Load env file based on current mode
  const env = loadEnv(mode, process.cwd(), '')
  
  const apiBaseUrl = env.VITE_API_BASE_URL || 'http://localhost:8000'
  const isProd = mode === 'production'
  
  return {
    plugins: [react(), tailwindcss()],
    build: {
      outDir: 'dist',
      sourcemap: !isProd,
      rollupOptions: {
        output: {
          manualChunks: (id) => {
            if (id.includes('node_modules')) {
              if (id.includes('react') || id.includes('react-dom')) {
                return 'vendor';
              }
              if (id.includes('lucide-react') || id.includes('react-icons')) {
                return 'ui';
              }
              return 'vendor';
            }
          }
        }
      }
    },
    server: {
      proxy: {
        '/api': {
          target: apiBaseUrl,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '')
        }
      }
    },
    define: {
      // Make env variables available to client code
      __APP_TITLE__: JSON.stringify(env.VITE_APP_TITLE || 'Sports Committee AI'),
      __APP_DESCRIPTION__: JSON.stringify(env.VITE_APP_DESCRIPTION || 'AI-powered sports committee assistant'),
      __API_BASE_URL__: JSON.stringify(env.VITE_API_BASE_URL || 'http://localhost:8000')
    }
  }
})