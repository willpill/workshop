# Yinwei Zhang
# Made in China + 1
# K08 <Flask & venv - Using flask to output HTML>
# 2024-9-23
# Time Spent: 0.1 hours

"""
DISCO:
We ran this program and the return value is shown in our local server webpage.

QCC:
0. Strangely it printed no hablo queso, which means nothing.
1. I can make it output proper HTML and so it displays a pretty website.
2. It needs not HTML doctype, HTMl or body or head tag (quirks mode!)
3. Print statements are printed in the shell.

INVESTIGATIVE APPROACH:
We used our existing knowledge of the terminal and HTML to understand the basics flask.
I learned that you can use flask to output and HTMl page from returning things in python.
"""


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?
                                         # This appears in many languages with variable assignment, such as Swift, Java, etc.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
                                         # File directory root.
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print? To the console of the site. Prints the name of the app.
    return "<h1>No hablo queso!</h1><p>woah</p>"           
                                         # Q4: Will this appear anywhere? How u know? Appears as HTML. Adding HTML tags make them respond accordingly.

app.run()                                # Q5: Where have you seen similar constructs in other languages? In swift and Java.



