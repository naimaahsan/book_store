from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ThumbnailItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Store the filename (e.g., "sunset.jpg") or a full URL
    image_filename = db.Column(db.String(255), nullable=False, default='default.jpg')