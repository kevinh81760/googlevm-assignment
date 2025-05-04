from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Welcome to Justin's Web Page"

@app.route("/page1")
def page1():
    return '''
        <h1>Page 1</h1>
        <a href="/home"><button>Home</button></a>
        <a href="/page2"><button>Page 2</button></a>
    '''

@app.route("/page2", methods=["GET", "POST"])
def page2():
    from flask import request
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        message = f"<h2>Hello {name}</h2>"
    return f'''
        <form method="POST">
            <input name="name" placeholder="Enter name">
            <button type="submit">Submit</button>
        </form>
        {message}
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
