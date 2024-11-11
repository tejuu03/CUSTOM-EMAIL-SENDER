from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)
# Define the Email model
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    prompt = db.Column(db.String(255))
    send_time = db.Column(db.String(10))  # Store time as string (HH:MM format)
    created_at = db.Column(db.DateTime, default=db.func.now())  # Store creation timestamp
    status = db.Column(db.String(20), default="Pending")  # Email status

    def __repr__(self):
        return f'<Email {self.subject}>'

# Initialize the database (to be done once, use flask db commands)
with app.app_context():
    db.create_all()

# Define the index route for rendering the form
@app.route('/')
def index():
    return render_template('index.html')

# Define the /upload route to handle form submission
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    subject = request.form['subject']
    prompt = request.form['prompt']
    send_time = request.form['send_time']

    # Save the form data to the database
    new_email = Email(subject=subject, prompt=prompt, send_time=send_time)
    db.session.add(new_email)
    db.session.commit()

    # Print the data for debugging
    print(f"File: {file.filename}, Subject: {subject}, Prompt: {prompt}, Send Time: {send_time}")

    # Redirect to the dashboard or a success message page
    return redirect(url_for('dashboard'))

# Define the dashboard route
@app.route('/dashboard')
def dashboard():
    # Fetch all emails from the database to display in the dashboard
    emails = Email.query.all()
    return render_template('dashboard.html', emails=emails)

# WebSocket connection handler to emit email data upon connection
@socketio.on('connect')
def handle_connect():
    emails = Email.query.all()
    # Collect the data to send as part of the WebSocket update
    email_data = [{"subject": email.subject, "status": email.status} for email in emails]
    # Emit email data to update the dashboard in real-time
    socketio.emit('update_dashboard', email_data)
# Define the route to view scheduled emails
@app.route('/view_emails')
def view_emails():
    # Fetch all emails from the database
    emails = Email.query.all()
    return render_template('view_emails.html', emails=emails)


# Start the application with SocketIO support
if __name__ == "__main__":
    socketio.run(app, debug=True)











