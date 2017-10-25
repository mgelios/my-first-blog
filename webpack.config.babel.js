import path from 'path'
import 'webpack'
import autoprefixer from 'autoprefixer'

export default {
    entry: './article_web_client/app.js',
    output: {
        path: `${__dirname}/articles_front/static`,
        filename: 'app.js'
    },
    resolve: {
        extensions: ['', '.js', '.jsx', '.scss'],
        modulesDirectories: [
            'node_modules'
        ]
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                loader: ['babel'],
                include: [
                    path.resolve(__dirname, "web_client")
                ],
                query: {
                    plugins: ['transform-runtime'],
                    presets: ['es2015', 'stage-0', 'react']
                }
            },
            {
                test: /\.s[a|c]ss$/,
                loader: 'style-loader!css-loader!sass-loader'
            }
        ]
    },
    sassLoader: {
        includePaths: [
            path.resolve(__dirname, "./article_web_client"),
            path.resolve(__dirname, "./node_modules/bootstrap/scss")
        ]
    }
}