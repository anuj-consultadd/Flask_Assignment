from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from db import db
from models.book import Book
from models.borrow import Borrow
from models.user import User, UserRole

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/dashboard")
@login_required
def admin_dashboard():
    if current_user.role != UserRole.ADMIN:
        flash("You are not authorized to access the admin dashboard.", "danger")
        return redirect(url_for("member.member_dashboard"))

    total_books = Book.query.count()
    total_members = User.query.filter_by(role=UserRole.MEMBER).count()
    
    books = Book.query.all()
    book_data = []
    
    for book in books:
        borrow_info = Borrow.query.filter_by(book_id=book.id, returned=False).first()

        # Debugging
        print(f"Book ID: {book.id}, Borrow Info: {borrow_info}")

        borrower_name = "N/A"
        if borrow_info:
            user = User.query.get(borrow_info.user_id)
            if user:
                borrower_name = user.username
            print(f"Book: {book.title}, Borrower ID: {borrow_info.user_id}, Borrower Name: {borrower_name}")

    
        book_data.append({
            "id": book.id,  
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "available": book.available,
            "borrower": borrower_name,
            "due_date": borrow_info.due_date.strftime('%Y-%m-%d') if borrow_info else "N/A"
    })

    
    return render_template(
        "admin_dashboard.html",
        total_books=total_books,
        total_members=total_members,
        book_data=book_data
    )

@admin_bp.route("/admin/add_book", methods=["POST"])
@login_required
def add_book():
    if current_user.role != UserRole.ADMIN:
        return redirect(url_for("member.member_dashboard"))

    title = request.form.get("title")
    author = request.form.get("author")
    category = request.form.get("category")

    if not title or not author:
        flash("Title and Author are required!", "danger")
        return redirect(url_for("admin.admin_dashboard"))

    new_book = Book(title=title, author=author, category=category)
    db.session.add(new_book)
    db.session.commit()
    
    flash("Book added successfully!", "success")
    return redirect(url_for("admin.admin_dashboard"))

@admin_bp.route("/admin/remove_book/<int:book_id>", methods=["POST"])
@login_required
def remove_book(book_id):
    if current_user.role != UserRole.ADMIN:
        flash("You are not authorized to remove books.", "danger")
        return redirect(url_for("member.member_dashboard"))

    book = Book.query.get(book_id)

    if not book:
        flash("Book not found!", "danger")
    else:
        db.session.delete(book)
        db.session.commit()
        flash("Book removed successfully!", "success")

    return redirect(url_for("admin.admin_dashboard"))
