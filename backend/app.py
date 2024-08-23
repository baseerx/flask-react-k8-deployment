from flask import Flask
from flask_cors import CORS, cross_origin  # Import cross_origin decorator

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers=['Content-Type', 'Authorization'], methods=["GET", "POST", "OPTIONS"])

@app.route('/')
@cross_origin()  # Allow CORS for this route
def home():
    return "Hello, Flask on Ubuntu!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
