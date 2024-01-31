from flask import Flask, render_template
import source.server.user
import source.server.otp as otp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello")




@app.route("/user/new")
def new_user(user_name="newbi"):
    secret_key, provisioning_uri, qr_encoded = otp.provision_otp(user_name=user_name)

    return render_template("new_user.html",
                           title="register",
                           secret_key=secret_key,
                           provisioning_uri=provisioning_uri,
                           qr_encoded=qr_encoded)




userApi = source.server.user.user_api("Hello from the API!")
@app.route("/api/v1/user")
def api_index():
    return userApi.get_hello_api()
