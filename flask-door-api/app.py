#!flask/bin/python
from flask import Flask  

app = Flask(__name__)  

@app.route('/') 
def index():     
    return "Hello, World!"  

if __name__ == '__main__':
    app.debug = True
    app.run(host = '192.168.1.250' , port = 6969)
