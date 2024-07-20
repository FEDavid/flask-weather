""" from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About' """

from flask import Flask, request, render_template, make_response
import os
from api.weather import get_weather

app = Flask(__name__, static_folder="../static", template_folder="../templates")

location = ""
display = "none"

@app.route('/', methods=["GET", "POST"])
def index():
    greeting = check_greeting()
    return render_template("index.html", greeting=greeting, location=location, display=display)

@app.route('/set_name', methods=["POST"])
def set_name():
    user_name = request.form['user_name']
    greeting = "Hello, " + user_name.capitalize() + "!"
    resp = make_response(render_template("index.html", greeting=greeting, display=display))
    resp.set_cookie('user_name', user_name)
    return resp

@app.route('/get_weather', methods=["POST"])
def get_weather_route():
    greeting = check_greeting()
    location = request.form['location']
    location, temp_out, desc_out = get_weather(location)
    weather_icon = "bi bi-cloud-fill" if "cloud" in desc_out else "bi bi-brightness-high-fill"
    display = "inline"
    return render_template("index.html", greeting=greeting, location=location, weather_icon=weather_icon, temp_out=temp_out, desc_out=desc_out, display=display)

def check_greeting():
    user_name = request.cookies.get('user_name')
    if user_name:
        return "Hi again, " + user_name.capitalize() + "!"
    else:
        return "Hello, guest!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

