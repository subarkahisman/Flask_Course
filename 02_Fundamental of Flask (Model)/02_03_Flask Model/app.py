from flask import Flask, render_template, request
from models import Lingkaran

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        r = float(request.form['radius'])
        model = Lingkaran(r)
      
        return render_template('circle.html', model=model)
    
    else:
        return render_template('form.html')
        
if __name__ == '__main__':
    app.run(debug=True)
