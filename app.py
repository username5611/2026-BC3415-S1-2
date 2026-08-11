#dbs prediction

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
## in flask framework, slash is first function to look for 
## run this before running function
## get means send to front end
## post means post to front end 
def index():
    return("hi")

if __name__ == "__main__":
    app.run()
