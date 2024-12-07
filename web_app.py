from flask import Flask, request, jsonify, render_template
from api_worker import Weather, BadWeatherModel


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('route.html')


if __name__ == '__main__':
    app.run(debug=True)
