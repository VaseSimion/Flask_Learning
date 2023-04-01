import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    images = []
    for filename in os.listdir('static/Pictures'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(filename)
    return render_template('home.html', photos=images[5:9])

@app.route('/portfolio')
def portfolio():
    images = []
    for filename in os.listdir('static/Pictures'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(filename)
    return render_template('portfolio.html', pictures=images)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
