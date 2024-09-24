# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                    #where will this go? This goes in the development terminal.
    return "No hablo queso!"

app.debug = True
app.run() #Debug mode shows some other information

'''
* Restarting with stat
    * Debugger is active!
* Debugger PIN: 276-852-198
'''