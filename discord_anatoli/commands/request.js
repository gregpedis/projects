module.exports = {
	name: 'request',
	description: 'Επισυνάπτει ένα αίτημα της υποστήριξης.',
	aliases: ['req', 'rqst'],
	usage: '[request number]',
	cooldown: 3,
	execute(message, args) {

		const data = [];
		if (!args.length) {

			const roll = Math.floor(Math.random() * request_indexes.length);
			data.push(`**Αίτημα νο. ${request_indexes[roll]}:** \n`);
			data.push(`${requests[roll]} \n`);

			return message.channel.send(data, {
					split: true
				})
				.catch(error => {
					console.error(`Could not send request to ${message.channel.name}. \n`, error);
					message.channel.send(`Για κάποιο λόγο δε μπόρεσα να στείλω αίτημα υποστήριξης.`);
					message.channel.send(`Να βάλω αίτημα στην υποστήριξη?`);
				});
		}

		const requestNo = parseInt(args[0]);
		const key = request_indexes.indexOf(requestNo);

		if (isNaN(requestNo) || key < 0) {
			data.push('Αυτό το αίτημα δεν υπάρχει. \n');
			data.push('Επισυνάπτω τη λίστα με τα αιτήματα μου: \n');
			data.push(request_indexes.map(index => index).join('\n'));
			data.push(`Μπορείς να στείλεις \`${prefix}request [request number]\` για να σου επισυνάψω κάποιο αίτημα :relaxed: \n`);

			return message.channel.send(data, {
					split: true
				})
				.catch(error => {
					console.error(`Could not send request to ${message.channel.name}. \n`, error);
					message.channel.send(`Για κάποιο λόγο δε μπόρεσα να στείλω αίτημα υποστήριξης.`);
					message.channel.send(`Να βάλω αίτημα στην υποστήριξη?`);
				});
		}

		data.push(`**Αίτημα νο. ${requestNo}:** \n`);
		data.push(`${requests[key]} \n`);

		message.channel.send(data);
	},
};

const {
	prefix
} = require('../config.json');

const request_indexes = [2091, 3581, 4537, 5124, 6969];

const requests = [
	"Η δημιουργία νέας ζημίας στο INFOPAD -> 'Διαχείρηση Φακέλων' δε δουλεύει. Επισυνάπτω screenshot.",
	"Όταν πατάω tab στο MIS των Επανεισπράξεων δε με προχωράει σωστά στα πεδία μίας επανείσπραξης, πράγμα το οποίο δε με αφήνει να δουλέψω. Έχει πραγματοποιηθεί συννενόηση με τη Διεύθυνση και το αίτημα κρίθηκε επείγον.",
	"Στο MIS η προεπιλεγμένη γραμματοσειρά είναι πολύ κουραστική, θα μπορούσαμε να κάνουμε κάτι σε Comic Sans MS?",
	"Δεν μου αρέσει το back button στον Πάπυρο. Θα προτιμούσα όταν το πατάω, να με πηγαίνει μπροστά. Έχω συννενοηθεί με τον κύριο Μπιτσάκο. Ευχαριστώ.",
	"Θα μπορούσατε να ξαναγράψετε όλο το database, το back-end και το front-end layer σε javascript? Θα βόλευε πολύ το δικαστικό εάν δε χρησιμοποιούσαμε managed code."
];
