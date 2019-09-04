from flask import Flask
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<name>')
def hello_guest(name):
    return "Hello %s as a guest" % name

@app.route('/user/<name>')
def hello_user(name):
    return "Hello %s as a user" % name
#    return "Hello World from {}  to the folks outside there %d time".format(name) %id

'''
@app.route('/hello')

def hello_world1():
    return "Hello World "

#app.add_url_rule('/', 'hello', hello_world)
'''

if __name__ == '__main__':
    app.run(debug = True)