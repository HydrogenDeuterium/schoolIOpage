from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('navigate.html')


@app.route('/leave')
def leave():  # put
    return render_template('lixiao.html')


@app.route('/into')
def into():
    return render_template('ruxiao.html')


if __name__ == '__main__':
    app.run()
