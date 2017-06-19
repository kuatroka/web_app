from flask import Flask, render_template, request
import requests

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/example')
def example():
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=\
    10&aggregate=0&e=Kraken'
    url_output = requests.get(url).json()['Data']
    return render_template('example.html', url_output=url_output[0] )

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={0}&tsym={1}&limit=\
    10&aggregate=0&e=Kraken'.format(name[:3], name[3:])
    url_output = requests.get(url).json()['Data']

    return render_template('index.html', name=name, comment=comment, url_output=url_output[0])
@app.route("/home", methods=['GET', 'POST'])
def home():

    links = ['https://www.google.com', 'https://www.duckduckgo.com', \
    'https://www.github.com']

    return render_template('example.html', links=links)




if __name__ == "__main__":
    app.run(debug=True)


def test():
    print("er")
