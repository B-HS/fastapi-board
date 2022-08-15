const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy : {
      '/useres':'http://localhost:8081',
      changeOrigin: true
    }
  }
})
