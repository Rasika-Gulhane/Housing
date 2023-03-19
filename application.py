

from flask import Flask

application = Flask(__name__)
app= application

@app.route("/", methods = ['GET','POST'])

def index():
    return "ML - flask new project"

if __name__ == "__main__":
    app.run(debug = True)