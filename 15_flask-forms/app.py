from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/greet', methods=['GET', 'POST'])
def greetings_page():
    if request.method == 'POST':
        username = request.form['username']
        requesttype = "POST"
    else:
        username = request.args.get('username')
        requesttype = "GET"

    return render_template('response.html', username=username, request=requesttype)

if __name__ == '__main__':
    app.debug = True
    app.run()