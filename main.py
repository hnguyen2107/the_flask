from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return "Hello world from PythonAnywhere!"


@app.route('/airbnb')
def airbnb():
    return render_template('airbnb.html')


@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')


if __name__ == '__main__':
    app.run()
