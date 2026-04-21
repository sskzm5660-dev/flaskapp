from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/convert",methods=["POST"] )
def convert():
    celsius = request.form["celsius"]

    response = requests.post(
        "http://127.0.0.1:5001/convert",
        json={"celsius": celsius}
    )

    result = response.json()["fahrenheit"]

    return f"Fahrenheit value: {result}"
    

if __name__ == "__main__":
    app.run(debug=True)