from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello Hello'

@app.get('/')
def index():
    return{'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run()