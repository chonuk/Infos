from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Test OOK"

if __name__ == '__main__':
    app.run(debug = True, port = 8080 , host = '0.0.0.0', threaded = True)