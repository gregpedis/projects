// require Node's native file system module
const fs = require('fs');

// require the discord.js module
const Discord = require('discord.js');

// create a new Discord client
const client = new Discord.Client();

// create a new discord collection of commands
client.commands = new Discord.Collection();

// rquire the welcome.js module
const welcome = require('./welcome.js');

// create variables according to the configuration file
const {
    prefix,
    meaning_of_life,
    token
} = require('./config.json');

// create an array of the command file names.
const commandFiles = fs.readdirSync('./commands')
    .filter(file => file.endsWith('.js'));

for (const file of commandFiles) {

    // requite each command's exported module
    const command = require(`./commands/${file}`);

    // set a new item in the Collection
    // with the key as the command name and the value as the exported module
    client.commands.set(command.name, command);
}

// set a counter which procs a random request message after a set amount of messages in the client
let counter = 0;

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
    console.log('Ready!');
});

// when a new member joins, run this code
// this event welcomes new members
client.on('guildMemberAdd', member => {

    const channel = client.channels.get('channelID');
    welcome.execute(member, channel);
});

// when the client receives any message, run this code
// this event will trigger after every message sent in the channel
client.on('message', message => {

    // increase the random request counter on every message
    // apart from bot commands and bot messages
    if (!message.author.bot && !message.content.startsWith(prefix)) counter++;

    // execute the request command's exported execute method 
    // every set amount of messages in any channel.
    if (counter >= 50) {
        client.commands.get("request").execute(message, []);
        counter = 0;
    }

    // if the message is not prefixed or is sent by a bot, do nothing
    if (!message.content.startsWith(prefix) || message.author.bot) return;

    // remove the prefix and white spaces and get a string array of args
    const args = message.content.slice(prefix.length).split(/ +/);

    // remove the command name from the args string array and cast it to lowercase
    const commandName = args.shift().toLowerCase();

    // try to find a command with the name or aliases supplied
    command = client.commands.get(commandName) ||
        client.commands.find(cmd => cmd.aliases && cmd.aliases.includes(commandName));

    // if the command name doesn't exist in our implement commands collection, do nothing
    if (!command || command.notExposed) return;

    message.channel.send(`Καλημέρα ${message.author}, η Ανατολή είμαι.`);

    // if the needed args are empty, reply a failure message
    if (command.args && !args.length) {
        let reply = `Δε μου έδωσες τις παραμέτρους που χρειάζομαι.`;

        //include a proper usage explanation
        if (command.usage) {
            reply += `\nΗ σωστή χρήση θα ήταν: \`${prefix}${command.name} ${command.usage}\``;
        }
        return message.channel.send(reply);
    }

    try {
        // execute the command's exported execute method
        command.execute(message, args);
    } catch (error) {
        //log the error in console and sent a generic failure message to the channel
        console.error(error);
        message.channel.send('Υπήρχε κάποιο πρόβλημα με την εκτέλεση αυτής της εντολής.');
        message.channel.send(`Να βάλω αίτημα στην υποστήριξη?`);
    }
});

// login to Discord with your app's token
client.login(token);