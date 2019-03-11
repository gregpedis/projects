module.exports = {
    name: 'welcome',
    description: 'Welcomes new member',
    notExposed: true,
    execute(member,channel) {

        channel.send(`Καλημέρα ${member.user.username}, η Ανατολή είμαι.`);
        channel.send(`Μπορείς να δεις το αίτημα ${Math.floor(Math.random()*1000)+4000}? Σε ευχαριστώ.`);      
    }
}