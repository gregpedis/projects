from flask import Flask, render_template, request, redirect, jsonify 
import createList
import random

# configuration 
DEBUG = True  

#instantiate the app 
app = Flask(__name__) 
app.config.from_object(__name__)  
Rolls = createList.Effects()

#default route, redirecting to the home route
@app.route('/',methods=['GET']) 
def base_route():     
    return redirect("/home", code=302)

#home route, containing the menu 
@app.route('/home', methods=['GET'])
def main_menu():
    rolls = [6,10,20,100]
    return render_template('home.html',rolls = rolls)   

#roll route, containing the dice roll
@app.route('/roll/<dice>', methods=['GET']) 
def dice_roll(dice):
    roll = random.randint(1,int(dice))
    return render_template('dice.html',dice = dice, roll = roll)   

#d10k route, containing the d10k roll
@app.route('/d10k', methods=['GET']) 
def d10k_roll():
    roll_index = random.randint(0,len(Rolls)-1)
    roll_effect = Rolls[roll_index]
    splitted_roll_effect = roll_effect.split(" ",1)
    return render_template('d10k.html', roll = splitted_roll_effect[0],  effect = splitted_roll_effect[1])   

#entrypoint for the app
if __name__ == '__main__':     
    app.run(host='192.168.1.250',port=2525)