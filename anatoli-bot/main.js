// require Node's native file system module
const fs = require('fs');

// require the discord.js module
const Discord = require('discord.js');

// create a new Discord client
const client = new Discord.Client();

// create a new discord collection of commands
client.commands = new Discord.Collection();

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

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
    console.log('Ready!');
});

// when the client receives any message, run this code
// this event will trigger after every message sent in the channel
client.on('message', message => {

    // if the message is not prefixed or is sent by a bot, do nothing
    if (!message.content.startsWith(prefix) || message.author.bot) return;

    // remove the prefix and white spaces and get a string array of args
    const args = message.content.slice(prefix.length).split(/ +/);

    // remove the command name from the args string array and cast it to lowercase
    const commandName = args.shift().toLowerCase();

    // try to find a command with the name or aliases supplied
    command = client.commands.get(commandName)
    || client.commands.find(cmd => cmd.aliases && cmd.aliases.includes(commandName));

    // if the command name doesn't exist in our implement commands collection, do nothing
    if(!command) return;

    // if the needed args are empty, reply a failure message
    if (command.args && !args.length) {
        let reply = `You didn't provide any arguments, ${message.author}!`;

        //include a proper usage explanation
        if (command.usage) {
            reply += `\nThe proper usage would be: \`${prefix}${command.name} ${command.usage}\``;
        }
        return message.channel.send(reply);
    }

    try {

        // execute the command's exported execute method
        command.execute(message, args);
    } catch (error) {

        //log the error in console and sent a generic failure message to the channel
        console.error(error);
        message.reply('There was an error trying to execute that command');
    }
});

// login to Discord with your app's token
client.login(token);