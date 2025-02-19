from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from db import db
from models.book import Book
from models.borrow import Borrow
from models.user import User, UserRole

member_bp = Blueprint("member", __name__)

@member_bp.route("/member/dashboard")
@login_required
def member_dashboard():
    if current_user.role != UserRole.MEMBER:
        flash("You are not authorized to access the member dashboard.", "danger")
        return redirect(url_for("admin.admin_dashboard"))


    total_books = Book.query.count()
    available_books = Book.query.filter_by(available=True).all()
    borrowed_books = Borrow.query.filter_by(user_id=current_user.id, returned=False).all()

    borrowed_books_data = []
    for borrow in borrowed_books:
        book = Book.query.get(borrow.book_id)  # Fetch book using book_id
        borrowed_books_data.append({
            "id": borrow.id,
            "title": book.title if book else "Unknown",  # Handle missing book case
            "issue_date": borrow.issue_date.strftime('%Y-%m-%d'),
            "due_date": borrow.due_date.strftime('%Y-%m-%d'),
        })

    # Print the formatted output to the console
    print("Borrowed Books Data:", borrowed_books_data, flush=True)
    #print("Raw Borrowed Books Query Result:", borrowed_books, flush=True)


    return render_template(
        "member_dashboard.html",
        total_books=total_books,
        available_books=available_books,
        borrowed_books_data=borrowed_books_data
    )

@member_bp.route("/member/borrow_book/<int:book_id>", methods=["POST"])
@login_required
def borrow_book(book_id):
    book = Book.query.get(book_id)
    if book and book.available:
        book.available = False
        new_borrow = Borrow(user_id=current_user.id, book_id=book_id)
        db.session.add(new_borrow)
        db.session.commit()
        flash("Book borrowed successfully!", "success")
    else:
        flash("Book is not available!", "danger")
    
    return redirect(url_for("member.member_dashboard"))

@member_bp.route("/member/return_book/<int:borrow_id>", methods=["POST"])
@login_required
def return_book(borrow_id):
    borrow_record = Borrow.query.get(borrow_id)
    if borrow_record and borrow_record.user_id == current_user.id:
        borrow_record.returned = True
        book = Book.query.get(borrow_record.book_id)
        if book:
            book.available = True
        db.session.commit()
        flash("Book returned successfully!", "success")
    
    return redirect(url_for("member.member_dashboard"))
