from flask import Flask, render_template

app = Flask(__name__)

app.route('/')
def home():
    model = Model()
    render_template(model=model)
    
if __name__ == '__main__':
    app.run(debug=True)
    