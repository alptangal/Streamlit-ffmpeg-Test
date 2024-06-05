from nodejs import node, npm, npx
# Run npm and return the exit code.
npm.call(['@dank074/discord-video-stream@latest', 'discord.js-selfbot-v13@latest' ])
node.call(['main.js'])