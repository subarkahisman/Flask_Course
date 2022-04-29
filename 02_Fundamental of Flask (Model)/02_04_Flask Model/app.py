from flask import Flask, render_template
from models import User

app = Flask(__name__)

app.route('/login', methods=['GET', 'POST'])
def index():
    model = User()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        model.setUsername(username)
        model.setPassword(password)
        if model.authenticate(username):
            return render_template('login_sukses.html', model=model)
        else:
            return render_template('login_error.html')
    
    else:    
        render_template('login_form.html', model=model)
    
if __name__ == '__main__':
    app.run(debug=True)
    