from flask import Flask, render_template
import source.server.user

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello")

userApi = source.server.user.user_api("Hello from the API!")
@app.route("/api/v1/user")
def api_index():
    return userApi.get_hello_api()
