from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def test2():
    return "TEST 2"


if __name__ == '__main__':
    app.run(debug=True)
