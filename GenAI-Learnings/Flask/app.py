from flask import Flask,render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


# My App

app = Flask(__name__)

# First main Page of application
@app.route("/") # Decorator of flask
def index():
    return render_template("index.html")




if __name__ in "__main__":
    app.run(debug=True)