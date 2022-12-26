const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: 'http://localhost:8080/',
  outputDir: '../backend/static/dist',
  indexPath: '../../backend/templates/base-vue.html',

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true,
      }
    }
  },
  transpileDependencies: true
})
