from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    prompt = db.Column(db.String(255))
    scheduled_at = db.Column(db.String(10))  # Time for scheduled email
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="Pending")  # Email status

    def __repr__(self):
        return f'<Email {self.subject}>'






