#dbs prediction

from flask import Flask, render_template, request

app = Flask(__name__)

## in flask framework, slash is first function to look for 
## run this before running function
## get means send to front end
## post means post to front end 

@app.route("/", methods=["GET", "POST"]) 
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"]) 
def main():
    return(render_template("main.html"))

@app.route("/dbs", methods=["GET", "POST"]) 
def dbs():
    return(render_template("dbs.html"))

if __name__ == "__main__":
    app.run()

