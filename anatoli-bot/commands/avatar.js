module.exports = {
    name: 'avatar',
    description: 'Show user avatar',
	aliases: ['icon', 'pfp'],
    execute(message) {
        message.channel.send(message.author.avatarURL);
    },
}