from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()



from models.user import User
from models.book import Book
from models.borrow import Borrow

