from db import db
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
import enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    MEMBER = "member"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.MEMBER, nullable=False)

    def __init__(self, username, email, password, role=UserRole.MEMBER):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password).decode("utf-8")
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
