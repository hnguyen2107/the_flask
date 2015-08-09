from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run()
