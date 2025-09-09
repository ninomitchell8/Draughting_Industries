from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import secrets
from flask import send_from_directory
print(secrets.token_hex(16))
app = Flask(__name__)

app.secret_key = "82ce948abe7c5faba5d61c3772b84d64"  # for flash messages

# Configure mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # or your email provider
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'draughting.industries@gmail.com'
app.config['MAIL_PASSWORD'] = 'pspz ciwv xilu ijds'  # use an app-specific password

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send email
        msg = Message(f"New Contact from {name}",
                      sender='draughting.industries@gmail.com',
                      recipients=['draughting.industries@gmail.com'],
                      reply_to = email
        )
        msg.body = f" From : {name}<{email}>\n\n{message}"
        mail.send(msg)

        flash('Message sent successfully!')
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True)
