import os
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    # / -> renders your merged dashboard page
    return render_template("index.html")

@app.route("/Smog_Circular_Dashboard.html")
def smog_circular():
    # keeps your existing iframe/link working if it points to this filename
    return render_template("Smog_Circular_Dashboard.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
