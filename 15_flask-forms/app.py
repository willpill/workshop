from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])

def greetings_page():
    print("")

if __name__ == '__main__':
    app.run()