import { resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { defineConfig } from 'vite'

const workspaceRoot = fileURLToPath(new URL('..', import.meta.url))
const cineshelfSource = resolve(workspaceRoot, 'Day11', 'src')

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      '@cineshelf': cineshelfSource,
    },
    dedupe: ['react', 'react-dom'],
  },
  server: {
    fs: {
      allow: [workspaceRoot],
    },
  },
})
