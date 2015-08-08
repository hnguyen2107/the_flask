from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world from PythonAnywhere!"


@app.route('/airbnb')
def airbnb():
    return render_template('airbnb.html')

if __name__ == '__main__':
    app.run()
