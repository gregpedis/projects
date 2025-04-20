module.exports = {
    name: 'avatar',
    description: 'Δείχνει το avatar του χρήστη.',
    aliases: ['icon', 'pfp'],
    usage: ' ',
    execute(message,args) {
        message.channel.send(`Επισυνάπτω το avatar του χρήστη ${message.author.username} παρακάτω. \n`);
        message.channel.send(message.client.user.avatarURL);
    }
};
