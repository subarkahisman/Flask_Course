from flask import Flask, render_template
from models import Circle

app = Flask(__name__)

@app.route('/')
def index():
    model = Circle()
    model.setRadius(5.0)
    return render_template('circle.html', model=model)
    
if __name__ == '__main__':
    app.run(debug=True)
    