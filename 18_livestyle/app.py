# Yinwei Zhang, Jackie, Wen
# Made in China Plus 1
# SoftDev
# K18 Styled; Served Live
# 2024-10-17
# Time Spent : 0.1 Hours

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
