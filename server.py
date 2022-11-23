from distutils.log import debug

from flask import Flask

app= Flask(__name__)

# Homepage Route
@app.route("/")
def home():
    return "Hello World!"

# Healthcheck Route
@app.route("/healthcheck")
def healthcheck():
    return "OK!"

if __name__=="__main__":
    app.run(debug==True)