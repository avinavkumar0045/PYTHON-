from flask import Flask # from module flask we import Flask

app = Flask(__name__)

#URL => endpoint

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if (__name__ == "__main__"):
    app.run(debug=True)

