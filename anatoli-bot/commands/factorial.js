
// recursive factorial calculation.
function factorial(x) {  
    if (x === 0) {
        return 1;
    } else
        return factorial(x - 1) * x;
}

module.exports = {
    name: 'factorial',
    aliases: ['fctrl','fct'],
    description: 'Calculates factorial',
    args: true,
    usage: '<number less than 20>',
    execute(message, args) {

        const temp = parseInt(args[0]);

        // if input is either a non-number value or a number bigger than 20,
        // return a failure response.
        if (isNaN(temp)|| temp>=20) {
             message.channel.send(`That's not a valid number!`);
        }
        else 
        message.channel.send(`The result is ${factorial(temp)}`);
    }

}