from app import create_app
from db import db

app = create_app()

with app.app_context():
    db.create_all()  # ✅ This will now create tables properly
    print("✅ Database tables created successfully!")
