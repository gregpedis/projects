from functools import wraps
from flask import Flask, request, Response

app = Flask(__name__) 

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def default_route():
    return '<a href="/secret-page-2">Click this</a>'

@app.route('/secret-page-2')
@requires_auth
def secret_page():
    return 'this is the secret page'

#entrypoint for the app
if __name__ == '__main__':     
    app.run(host='192.168.1.240',port=5000)