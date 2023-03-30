// semantic release js configuration
// we delegate the github tag work to python semantic release
module.exports = {
    plugins: [
        '@semantic-release/commit-analyzer',
        '@semantic-release/release-notes-generator',
        '@semantic-release/npm'
    ]
}
