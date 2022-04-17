from flask import Flask, request

apps = Flask(__name__)

@apps.route('/')
def index():
    # get header from request object
    headers = request.headers
    response = ['%s : %s' % (key, value) for key, value in sorted(headers.items())]
    response = '<br />'.join(response)
    return response
    
if __name__ == '__main__':
    apps.run(debug=True)