# Flask_Assignment

## This is the folder structure :

``` bash 
flask_library/
│── app.py               # Main Flask app entry point
│── config.py            # Configurations (DB, Secret Key, etc.)
│── venv/                # Virtual environment
│── db/
│   ├── __init__.py      # Database initialization
│── models/
│   ├── __init__.py      # Model initialization
│   ├── user.py          # User Model
│   ├── book.py          # Book Model
│   ├── borrow.py        # Borrow Model
│── routes/
│   ├── __init__.py      # Route initialization
│   ├── auth_routes.py   # Authentication routes
│   ├── admin_dashboard.py  # For user, book and adding and removal of books
│   ├── member_dashboard.py # for availabale books and to borrow and return books
│── templates/           # Jinja2 HTML templates
│── static/              # CSS, JS, images
│── requirements.txt     # Dependencies list
│── .env                 # (DB credentials)
```

remember to include the credentials in .env
requirements.txt
screenshots
gitignore
how to setup env file here# Flask_Assignment
