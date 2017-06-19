from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/example')
def example():
    return render_template('example.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route("/home", methods=['GET', 'POST'])
def home():
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=\
    10&aggregate=0&e=Kraken'
    url_output = requests.get(url).json()['Data']
    links = ['https://www.google.com', 'https://www.duckduckgo.com', \
    'https://www.github.com']

    return render_template('example.html', links=links, url_output=url_output[0])




if __name__ == "__main__":
    app.run(debug=True)


def test():
    print("er")
