from flask import Flask
from markupsafe import escape

# Initialize the application instance
app = Flask(__name__)

# Define the root route and its execution function
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/user")
def user():
    return "User Page!"

@app.route("/user/<user>")
def user_profile(user):
    return f"Hello {escape(user)}!"


if __name__ == "__main__":
    app.run(debug=True)
