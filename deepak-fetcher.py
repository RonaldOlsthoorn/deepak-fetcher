from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
import urllib.request

app = Flask(__name__)
CORS(app)


@app.route('/deepak.json')
def deepak_qutote():

    with urllib.request.urlopen('http://wisdomofchopra.com/iframe.php') as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        full_td = soup.find(id="quote").header.h2.string

    return jsonify(quote=full_td)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)