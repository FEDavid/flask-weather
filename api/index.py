from flask import Flask, request, render_template, make_response
from os import path
import sys, weather
print (sys.version)

app = Flask(__name__, static_folder="static")
location = ""
img = path.join('static', 'images')
display = "none"

# FLASK ----------------------------------------------------------------

@app.route('/',methods=["GET","POST"])
def index():
    greeting = check_greeting()
    return render_template("index.html", greeting = greeting, location = location, display=display)

@app.route('/set_name', methods=["POST"])
def set_name():
    # get the user's name from the form
    user_name = request.form['user_name']
    greeting = "Hello, " + user_name.capitalize() + "!"
    
    # create a response object
    resp = make_response(render_template("index.html", greeting = greeting, display=display))
    
    # set a cookie with the user's name
    resp.set_cookie('user_name', user_name)
    return resp

@app.route('/get_weather', methods=["POST"])
def get_weather():
    greeting = check_greeting()
    # get the user's name from the form
    location = request.form['location']
    location, temp_out, desc_out = weather.get_weather(location)
    if "cloud" in desc_out:
        weather_icon = "bi bi-cloud-fill"
    else:
        weather_icon = "bi bi-brightness-high-fill"
    print(desc_out)

    # create a response object
    display = "inline"
    return render_template("index.html", greeting = greeting, location = location, weather_icon = weather_icon, temp_out = temp_out, desc_out = desc_out, display = display)

# END OF FLASK ----------------------------------------------------------------

def check_greeting():
    user_name = request.cookies.get('user_name')
    if user_name:
        greeting = "Hi again, " + user_name.capitalize() + "!"
    else:
        greeting = "Hello, guest!"
    return greeting

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')