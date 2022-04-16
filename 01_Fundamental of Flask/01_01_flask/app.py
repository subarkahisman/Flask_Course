from flask import Flask
apps = Flask(__name__)

@apps.route('/')
def index():
    return '<h2>Hello World from Flask</h2>'
    
@apps.route('/hello/<name>')
def hello(name):
    return '<h2>Hello %s, it is from Flask</h2>' % name
    
@apps.route('/page/<int:number>')
def page(number):
    return '<h2>Page #%d</h2>' % number

if __name__ == '__main__':
    apps.run(debug=True)