from db import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100))
    available = db.Column(db.Boolean, default=True)

    def __init__(self, title, author, category, available=True):
        self.title = title
        self.author = author
        self.category = category
        self.available = available