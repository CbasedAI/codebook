const path = require('path');

const config = {
    mode: 'production',
    entry: './app/index.js',
    output: {
        filename: 'bundle.js'
    },
    module: { 
        rules: [
            {
              test: /\.js$/,
              exclude: /(node_modules|bower_components)/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: ['@babel/preset-env']
                }
              }
            },
            {
                test: /\.css$/,
                loader: "style-loader!css-loader",
            },
            {
                test: /\.less$/,
                loader: 'style-loader!css-loader!less-loader',
            },
          ]
        }
    };

module.exports = config;