from flask import Flask

# Create a Flask app
app = Flask(__name__)

# you connect the URL route "/" to the home() function by decorating it with @app.route("/").
# This tells 
@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)