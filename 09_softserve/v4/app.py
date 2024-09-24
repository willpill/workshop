# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo qssueso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change. When i change the code, it automatically updates in the site and the change is visible when I refresh the site.
    app.run()

#Prints the following in the console:
#the __name__ of this module is...
#__main__