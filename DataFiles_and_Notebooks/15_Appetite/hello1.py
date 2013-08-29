from flask import Flask
app = Flask(__name__)

run_on_public_interface = True

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    if run_on_public_interface:
        app.run(host='0.0.0.0')
    else:
        app.run()
