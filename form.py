from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def display_form():
    return render_template('form.html')


@app.route('/results', methods=['POST'])
def results():
    return "Hello"

if __name__ == '__main__':
    app.run()
