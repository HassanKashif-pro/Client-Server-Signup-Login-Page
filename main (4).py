from flask import Flask, request, redirect
from replit import db

app = Flask(__name__, static_url_path='/static')

# Assume that db is properly initialized

# A dictionary hard coded into the program that stores the login details for two db
# db["david"] = {"password": "Baldy1"}
# db["katie"] = {"password": "k8t"}

@app.route('/', methods=["GET"])
def index():
    page = """<p><a href="/login">Log in</a></p>
              <p><a href="/signup">Sign up</a></p>"""
    return page

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        password = form.get("password")
        if username not in db.keys():
            db[username] = {"name": form.get("name"), "password": password}
            return f"Hello {db[username]['name']}"
    return """<form method="post" action="/signup">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
                <br><br>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <br><br>
                <input type="submit" value="Sign Up">
            </form>"""

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        password = form.get("password")
        try:
            if db[username]["password"] == password:
                return f"Hello {db[username]['name']}"
            else:
                return redirect("/nope")
        except KeyError:
            return redirect("/nope")
    else:
        return """<form method="post" action="/login">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <br><br>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <br><br>
                    <input type="submit" value="Login">
                </form>"""

@app.route("/nope")
def nope():
    return """<img src="/static/nerdy.gif" height="100">"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
