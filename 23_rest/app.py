from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    x = requests.get('https://api.nasa.gov/planetary/apod?api_key=keykeykey')
    y = x.json()
    return render_template('index.html', l = y["hdurl"])

if __name__ == '__main__':
    app.debug = True
    app.run()
