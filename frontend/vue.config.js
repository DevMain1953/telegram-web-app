const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    https: true,
    client: {
      webSocketURL: {
        protocol: 'wss',
        hostname: 'url-to-ngrok',
        port: 443
      }
    },
  }
});
