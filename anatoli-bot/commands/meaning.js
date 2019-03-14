module.exports = {
    name: 'meaning',
    description: 'Ενημερώνει τη μηχανογράφηση για το νόημα της ζωής.',
    aliases: ['life', 'dontpanic'],
    usage: ' ',
	cooldown: 3,
    execute(message, args) {
        message.channel.send('Το νόημα της ζωής είναι 42.');
    },
}