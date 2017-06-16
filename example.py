from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Me!</h1>"


@app.route("/home", methods=['GET', 'POST'])
def home():
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=\
    10&aggregate=0&e=Kraken'
    url_output = requests.get(url).json()['Data']
    return render_template('example.html')


if __name__ == "__main__":
    app.run(debug=True)


def test():
    print("er")
