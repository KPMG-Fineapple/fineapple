module.exports = {
    apps: [
        {
            name: 'server',
            script: 'dist/main.js',
            watch: '.',
            instances: -1
        },
    ],
};