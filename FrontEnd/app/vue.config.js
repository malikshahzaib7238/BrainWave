module.exports = {
  
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
    },
  },
    publicPath: process.env.NODE_ENV === 'production'
      ? '/web-edf-viewer/'
      : '/'

  }
 