from flask import Flask

pp = Flask(__name__)

@app.route('/')
def my_function():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)