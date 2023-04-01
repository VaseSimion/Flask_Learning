from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    pictures_dir = os.path.join(app.static_folder, 'Pictures')
    picture_files = [filename for filename in os.listdir(pictures_dir) if filename.endswith('.jpg')]
    return render_template('home.html', picture_files=picture_files[:3])
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    pictures_dir = os.path.join(app.static_folder, 'Pictures')
    picture_files = [filename for filename in os.listdir(pictures_dir) if filename.endswith('.jpg')]
    return render_template('portfolio.html', picture_files=picture_files)

if __name__ == '__main__':
    app.run(debug=True)
