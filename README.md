# Flask Library Management System

## Setup

### Clone the Repository:
```bash
git clone https://github.com/your-repo/flask-library-management.git
cd flask-library-management
```

### Create a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Setup Environment Variables:
Create a `.env` file in the root directory and add the following:
⚠️ ``Important``: Replace your_secret_key, your_password, and your_database_name with actual values before running the application.
```env
SECRET_KEY=your_secret_key
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/your_database_name
```

### Apply Database Migrations:
```bash
flask db init   # Run only for first-time setup
flask db migrate -m "Initial migration"
flask db upgrade
```

### Run the Application:
```bash
python app.py
```

### Access the Application:
Open your browser and go to:
```
http://127.0.0.1:5000/
```

## Project Structure:
```bash
flask_library/
│── app.py               # Main Flask app entry point
│── config.py            # Configuration file (Database, Secret Key, etc.)
│── venv/                # Virtual environment (dependencies)
│── README.md            # Project documentation
│── requirements.txt     # Project dependencies
│── .env                 # Environment variables (DB credentials, secret keys)
│── .gitignore           # Files and directories to be ignored by Git
│
│── db/                  # Database-related files
│   ├── __init__.py      # Database initialization
│
│── models/              # Database models (ORM)
│   ├── __init__.py      # Model initialization
│   ├── user.py          # User model (Admin & Member)
│   ├── book.py          # Book model (Title, Author, ISBN, etc.)
│   ├── borrow.py        # Borrow model (Issue, Return, Renew, Due Dates)
│
│── scripts/             # Utility scripts
│   ├── init_db.py       # Script to initialize the database
│
│── templates/           # Jinja2 HTML templates
│   ├── base.html              # Base template for inheritance
│   ├── login.html             # Login page template
│   ├── register.html          # User registration template
│   ├── logout.html            # Logout page template
│   ├── admin_dashboard.html   # Admin dashboard (Manage Users, Books, etc.)
│   ├── member_dashboard.html  # Member dashboard (Search, Borrow, Return Books)
│
│── routes/              # Flask application routes
│   ├── __init__.py           # Routes package initialization
│   ├── auth_routes.py        # Authentication routes (Login, Register, Logout)
│   ├── admin_dashboard.py    # Admin-specific routes (User & Book Management)
│   ├── member_dashboard.py   # Member-specific routes (Book Borrowing & Return)
│
│── static/              # Static files (CSS, JS, Images)
│
│── migrations/          # Alembic migration scripts for database changes
```

#  Flask Library Management System - Features

## User Roles & Permissions  

The system has **two roles**:  
1. **Admin (Librarian)**  
2. **Member (Library User)**  

Each role has specific permissions and access levels.

---

## Authentication & User Management  

The system uses **``Flask-Login``** for secure user authentication, session management, and role-based access control.  

### **Features:**
- **User Registration**  
  - New users can register and select their role (**Admin or Member**).  
  - Passwords are securely hashed using **``bcrypt``**.  
  ![](static/register.png)

- **Login & Logout**  
  - Users can log in using their email and password.  
  - The system manages sessions using **``Flask-Login``**.  
  - Users are redirected to their respective dashboards after login.  
  - Sessions are cleared upon logout.  
  ![](static/login.png)

- **Access Control**  
  - **``Protected Routes``**: Only logged-in users can access certain features.  
  - Unauthorized users are redirected to the login page.  

---

## 📖 Admin Role (Librarian)  

The **Admin** manages the entire library system, including book inventory and tracking borrowed books.  

### **Admin Features:**
![](static/admin_dashboard.png)
- **Book Management**  
  - Add new books to the library.  
  - Remove books from the library.  

- **View All Books**  
  - See a list of all books in the library.  
  - Check whether a book is available or borrowed.  

- **Borrowing & Availability Tracking**  
  - View details on who has borrowed a book.  
  - Check issue and return dates of borrowed books.  

---

##  Member Role (Library User)  

The **Member** can browse available books, borrow books, and return them.  

###  **Member Features:**
![](static/member_dashboard.png)
- **View Available Books**  
  - See a list of books that are currently available for borrowing.  

- **Borrowing System**  
  - Borrow available books.  
  - View a personal list of borrowed books.  
  - See issue and return dates for borrowed books.  

- **Returning Books**  
  - Return borrowed books before the due date.  

---

##  Database & Storage  

- The system uses **MySQL**, connected via **``MySQL Workbench``**.  
![](static/database_connection_example.png)
- **``Flask-SQLAlchemy``** is used as the ORM for managing database interactions.  
- Migrations are handled using **``Flask-Migrate``** and **Alembic**.  
![](static/MYSQL_table.png)


###  **Database Tables:**
- **`users`** - Stores user authentication details (Admin & Member).  
- **`books`** - Stores book information (title, author, availability).  
- **`borrowed_books`** - Tracks issued books with issue and return dates.  
Extended ER Diagram:
![](static/EERD.png)


---

**This system ensures smooth management of books, borrowing activities, and user authentication in the library!**  






