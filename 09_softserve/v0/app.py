# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # Serving Flask app 'app' with Debug mode: off

@app.route("/")                # This is the root file directory.
def hello_world():
    print(__name__)            # __main__ is printed in the console once I access the local server.
    return "No hablo queso!"   # This is the content of the website in HTML.

app.run()                      # Running on http://127.0.0.1:5000
