import { sveltekit } from '@sveltejs/kit/vite';
import UnoCSS from 'unocss/vite';
import { Connect, defineConfig, type Plugin } from 'vite';
import extractorSvelte from '@unocss/extractor-svelte';
import tsconfigPaths from 'vite-tsconfig-paths';
import topLevelAwait from 'vite-plugin-top-level-await';
import { nodePolyfills } from 'vite-plugin-node-polyfills';

const crossOriginIsolationMiddleware: Connect.NextHandleFunction = (_, response, next) => {
  response.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
  response.setHeader('Cross-Origin-Embedder-Policy', 'require-corp');
  next();
};

const crossOriginIsolation: Plugin = {
  name: 'cross-origin-isolation',
  configureServer: (server) => {
    server.middlewares.use(crossOriginIsolationMiddleware);
  },
  configurePreviewServer: (server) => {
    server.middlewares.use(crossOriginIsolationMiddleware);
  }
};

export default defineConfig({
  plugins: [
    nodePolyfills(),
    UnoCSS({
      extractors: [extractorSvelte]
    }),
    sveltekit(),
    tsconfigPaths(),
    topLevelAwait(),
    crossOriginIsolation
  ],
  server: {
    cors: true
  },
  resolve: {
    alias: {
      '@cornerstonejs/dicom-image-loader':
        '@cornerstonejs/dicom-image-loader/dist/cornerstoneDICOMImageLoader.bundle.min.js'
    }
  }
});
