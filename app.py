from flask import Flask, render_template
from flask_cors import CORS
import json
import http.client

app = Flask(__name__)
CORS(app)

connection = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

conntectionHeader = {
    'X-RapidAPI-Key': "0c5593f7c3mshaea2f58724d8514p12e7ecjsn1a8037ec618f",
    'X-RapidAPI-Host': "covid-193.p.rapidapi.com"
}

@app.route("/")
def index():
    connection.request("GET", "/countries", headers=conntectionHeader)
    response = connection.getresponse()
    data = response.read()
    return render_template("index.html", countries=json.loads(data.decode("utf-8"))["response"], totalCount=json.loads(data.decode("utf-8"))["results"])


@app.route("/country/<countryName>")
def getCountry(countryName):
    connection.request("GET", "/statistics?country=" + countryName, headers=conntectionHeader)
    res = connection.getresponse()
    data = res.read()
    return render_template("country.html", country=json.loads(data.decode("utf-8"))["response"][0])


if __name__ == "__main__":
    app.run(debug=True)