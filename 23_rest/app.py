from flask import Flask, render_template
import requests, json
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    x = requests.get('https://api.nasa.gov/planetary/apod?api_key=81jOn3vdY3ZELIZ8EaAIdQhS2YzueSCdYm2cOADB').json() # Get request in json form
    return render_template('index.html', l = x["hdurl"], m = x["explanation"])
if __name__ == '__main__':
    app.run()
