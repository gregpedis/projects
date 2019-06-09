from flask import Flask, render_template, request, jsonify 
import createList
import random

# configuration 
DEBUG = True  

#instantiate the app 
app = Flask(__name__) 
app.config.from_object(__name__)  
Rolls = createList.Effects()

# sanity check route 
@app.route('/', methods=['GET']) 
def random_roll_effect():
    
    roll_index = random.randint(0,len(Rolls)-1)
    roll_effect = Rolls[roll_index]
    splitted_roll_effect = roll_effect.split(" ",1)

    return render_template('random-roll-effect.html', roll = splitted_roll_effect[0],  effect = splitted_roll_effect[1])   


if __name__ == '__main__':     
    app.run(host='192.168.1.250',port=2525)
