from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return "<h1> Hello </h1>"


@app.route('/page')
def page():
    return "<h1> Page 2 </h1>"


if __name__ == '__main__':
    app.run()
