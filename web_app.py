from flask import Flask, request, jsonify, render_template
from api_worker import Weather, BadWeatherModel


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('route.html')


@app.route('/', methods=['POST'])
def index_post():
    request_data = request.form
    processed_data = process_data(request_data)
    return jsonify(processed_data), 200


def process_data(data):
    city_start = Weather(data['startpoint'])
    city_end = Weather(data['endpoint'])
    start_weather = city_start.get_one_day_forecast()
    end_weather = city_end.get_one_day_forecast()
    return {'start_weather': start_weather,
            'end_weather': end_weather,
            'is_bad_weather_at_start': BadWeatherModel.is_weather_bad(start_weather),
            'is_bad_weather_at_end': BadWeatherModel.is_weather_bad(end_weather)}


if __name__ == '__main__':
    app.run(debug=True)
