from flask import Flask

app = Flask(__name__)

@app.route('/home')
def my_function():
    return render_template('index.html')

@app.route('/about')
def my_function():
    return render_template('about.html')

@app.route('/gallery')
def my_function():
    return render_template('gallery.html')

app.route('/servics')
def my_function():
    return render_template('service.html')


@app.route('/login')
def my_function():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)