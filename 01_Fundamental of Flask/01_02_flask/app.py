from flask import Flask
from models import HelloModel

apps = Flask(__name__)

@apps.route('/')
def index():
    # create object from  HelloModel class
    model = HelloModel()
    # return a value taken from model
    return model.getText()
    
if __name__ == '__main__':
    apps.run(debug=True)
    
    