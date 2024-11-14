from flask import Blueprint
from controllers.BookController import get_books, get_book, add_book, update_book, patch_book, delete_book

book_bp = Blueprint('Book_bp', __name__)

#Routes for getting all books
book_bp.route('/api/books', methods=['GET'])(get_books)

#Routes for get a single book (GET)
book_bp.route('/api/books/<id>', methods=['GET'])(get_book)

#Routes for a new book (POST)
book_bp.route('/api/books', methods=['POST'])(add_book)

#Routes for Update a book (PUT)
book_bp.route('/api/books/<id>', methods=['PUT'])(update_book)

#Routes for Partially update a book (PATCH)
book_bp.route('/api/books/<id>', methods=['PATCH'])(patch_book)

#Routes fo Delete a book (DELETE)
book_bp.route('/api/books/<id>', methods=['DELETE'])(delete_book)
