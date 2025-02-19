from db import db
from datetime import datetime, timedelta

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    issue_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    due_date = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(days=14), nullable=False)
    returned = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
