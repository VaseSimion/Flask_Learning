import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message
import re
import random

app = Flask(__name__)
app.secret_key = 'development key'
app.config['MAIL_SERVER']='smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'slrvasile@yahoo.com'
app.config['MAIL_PASSWORD'] = 'TBD'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def validate_form_data(data):
    error_messages = []

    # Check if name is empty
    if not data['name']:
        error_messages.append('Name is required')

    # Check if email is empty or invalid
    if not data['email']:
        error_messages.append('Email is required')
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        error_messages.append('Email is invalid')

    # Check if message is empty
    if not data['message']:
        error_messages.append('Message is required')

    return error_messages


@app.route('/')
def home():
    images = []
    for filename in os.listdir('static/Pictures'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(filename)
    return render_template('home.html', photos=images[-4:])


@app.route('/portfolio')
def portfolio():
    images = []
    for filename in os.listdir("/home/VaseBotty/mysite/static/Pictures"):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(filename)
    return render_template('portfolio.html', pictures=images)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        form_data = request.form.to_dict()
        errors = validate_form_data(form_data)

        if errors:
            return render_template('contact.html', errors=errors, form_data=form_data)

        msg = Message(subject=subject,
                      sender='slrvasile@yahoo.com',
                      recipients=['sularea.vasile@yahoo.com'])
        msg.body = f"Name: {name}\nEmail: {email}\n\n{message}"
        mail.send(msg)

        return render_template('contact.html', success=True)

    return render_template('contact.html', success=False)

@app.route('/local_bots.html')
def local_bots():
    return render_template('local_bots.html')

@app.route('/generated_images.html')
def generated_images():
    images = []
    for filename in os.listdir("/home/VaseBotty/mysite/static/Pictures"):
        if filename.endswith('.png'):
            images.append(filename)
    return render_template('generated_images.html', pictures=images)

@app.route('/photography.html')
def photography():
    images = []
    for filename in os.listdir("/home/VaseBotty/mysite/static/Pictures"):
        if filename.endswith('.jpg'):
            images.append(filename)
    return render_template('photography.html', pictures=images)

@app.route('/ai_tools.html')
def ai_tools():
    return render_template('ai_tools.html')

if __name__ == '__main__':
    app.run(debug=False)