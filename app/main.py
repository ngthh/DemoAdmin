from flask import render_template

from app import app, login
from app.models import *

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
