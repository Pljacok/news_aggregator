import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/news')
def get_news():
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=your-newsapi-key")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
