from flask import Flask, render_template, request, jsonify 
from flask_cors import CORS   


# configuration 
DEBUG = True  

#instantiate the app 
app = Flask(__name__) 
app.config.from_object(__name__)  

# enable CORS CORS
#(app, resources={r'/*': {'origins': '*'}})


door_status='Closed'

# sanity check route 
@app.route('/', methods=['GET']) 
def remote_door():
    return render_template('door.html',door_status=door_status)   



@app.route('/open',methods=['GET'])
def open_door():
    if door_status =='Open':
        door_status='Closed'
    else:
        door_status='Open'


if __name__ == '__main__':     
    app.run(host='192.168.1.250',port=5000)
