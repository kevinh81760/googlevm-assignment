from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('welcome.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        message = f"Hello {name}"
    return render_template('page2.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
