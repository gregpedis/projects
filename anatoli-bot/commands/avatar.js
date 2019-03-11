module.exports = {
    name: 'avatar',
    description: 'Δείχνει το avatar του χρήστη.',
    aliases: ['icon', 'pfp'],
    usage: ' ',
    execute(message) {
        message.channel.send(message.author.avatarURL);
    },
}