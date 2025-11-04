from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "656b6994a3c22287f959b1c18836e655"
NEWS_URL = "https://gnews.io/api/v4/search"

@app.route("/")
def index():
    params = {
        "q": "iklim değişikliği",
        "lang": "tr",
        "token": API_KEY,
        "max": 10
    }
    r = requests.get(NEWS_URL, params=params)
    articles = r.json().get("articles", [])
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)



API_KEY = "656b6994a3c22287f959b1c18836e655"






