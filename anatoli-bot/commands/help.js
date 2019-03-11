const { prefix } = require('../config.json');

module.exports = {
	name: 'help',
	description: 'Δείχνει σε λίστα όλες τις διαθέσιμες εντολές ή τις λεπτομέρειες συγκεκριμένης εντολής.',
	aliases: ['commands'],
	usage: '[command name]',
	cooldown: 3,
	execute(message, args) {
		const data = [];
		const { commands } = message.client;

		if (!args.length) {
			data.push('Επισυνάπτω τη λίστα με τις εντολές μου:\n');
			data.push(commands.map(command => command.name).join('\n'));
			data.push(`\nΜπορείς να στείλεις \`${prefix}help [command name]\` για να σου επισυνάψω βοήθεια με κάποια εντολή!`);

			return message.channel.send(data, { split: true })
				.catch(error => {
					console.error(`Could not send help to ${message.channel.name}.\n`, error);
					message.channel.send(`Για κάποιο λόγο δε μπόρεσα να στείλω τη λίστα με τις εντολές.`);
					message.channel.send(`Να βάλω αίτημα στην υποστήριξη?`);
				});
		}

		const name = args[0].toLowerCase();
		const command = commands.get(name) || commands.find(c => c.aliases && c.aliases.includes(name));

		if (!command) {
			message.reply('Αυτή η εντολή δεν υπάρχει.');
			message.channel.send('Βάζω αίτημα στην υποστήριξη.');
			return;
		}

		data.push(`**Όνομα:** ${command.name}`);

		if (command.aliases) data.push(`**Aliases:** ${command.aliases.join(', ')}`);
		if (command.description) data.push(`**Περιγραφή:** ${command.description}`);
		if (command.usage) data.push(`**Χρήση:** ${prefix}${command.name} ${command.usage}`);

		data.push(`**Χρόνος μεταξύ χρήσεων:** ${command.cooldown || 3} δευτερόλεπτα`);

		message.channel.send(data, { split: true });
	},
};