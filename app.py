import requests
from flask import Flask, render_template, request
from datetime import datetime
from matplotlib import pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():

    x_time = [0,1,2,3,4,5,6]
    y_temp = [18,15,13,9,8,8,11]
    plt.plot(x_time, y_temp)
    plt.savefig('test_chart')

    return render_template("home.html")


@app.route('/results', methods=["GET", "POST"])
def results():
    api_key = 'c60099ee6e3cea86e800c7aac370bb6c'
    city = request.form.get('city')
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + api_key
    print(url)
    response = requests.get(url).json()
    location = response.get("name")
    timezone = response.get("timezone") 
    timestamp = response.get("dt")
    date_time = dt_object = datetime.fromtimestamp(timestamp)
    local_timestamp = ""
    temp_k = response.get("main").get("temp")
    temp_c = temp_k - 273.15
    description = response.get("description")
    wind_speed = response.get("wind").get("speed")
    icon = response.get("weather")[0].get("icon")
    icon_url = "http://openweathermap.org/img/w/" + icon + ".png"
    my_list = [location, timezone, timestamp]
    my_dict = {
        "location" : {"lat": 0, "long": 0},
        "timestamp": timestamp
    }
    print(my_dict)
    print(my_dict["timestamp"])
    print(my_dict["location"]["lat"])
    print(my_dict.get("location").get("lat"))

    # x_time = [0, 1,2,3,4,5,6]
    # y_temp = [18,15,13,9,8,8,11]
    # plt.plot(x_time, y_temp)
    # plt.savefig('static/test_plot')





    return render_template('results.html', weather_list=my_list, weather_dict=my_dict)


if __name__ == '__main__':
    app.run(debug=True)
