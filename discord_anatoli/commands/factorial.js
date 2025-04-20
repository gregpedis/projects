// recursive factorial calculation.
function factorial(x) {
    if (x === 0) {
        return 1;
    } else
        return factorial(x - 1) * x;
}

module.exports = {
    name: 'factorial',
    aliases: ['fctrl', 'fct'],
    description: 'Υπολογίζει παραγοντικό.',
    args: true,
    usage: '<number less than 20>',
    execute(message, args) {

        const temp = parseInt(args[0]);

        // if input is either a non-number value or a number bigger than 20,
        // return a failure response.
        if (isNaN(temp) || temp >= 20) {
            message.channel.send(`Αυτός δεν είναι σωστός αριθμός`);
        } else {
            message.channel.send(`Το αποτέλεσμα είναι ${factorial(temp)}`);
            if (factorial(temp) >= 1000)
                message.channel.send(`Κώστα μου μπορούμε να βάλουμε τελείες στα νούμερα γιατι μπερδεύομαι?`);
        }
    }
};
