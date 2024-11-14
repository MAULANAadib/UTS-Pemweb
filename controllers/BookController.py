from flask import jsonify, request
from models.BookModel import Book
from models.CategoryModel import Category
from config import db

###### BOOKS ######
#Get all books
def get_books():
    books = Book.query.all()
    books_with_categories = []

    for book in books:
        #Ambil category terkait dari book
        category = Category.query.get(book.category_id)

        #Tambahkan detail buku beserta nama category
        books_with_categories.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'category_name': category.name if category else "No Category"
        })

    response = {
        'status': 'success',
        'data':{
            'books': books_with_categories
        },
        'message': 'Books retrieved successfully'
    }
    return jsonify(response), 200

#Get a single book by with category name (GET)
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'status': 'error', 'message': 'Book not found'}), 404
    #Ambil category terkait dari book
    category = Category.query.get(book.category_id)

    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'category_name': category.name if category else "No Category"
    }
    # response = {
    #     'status': 'success',
    #     'data':{
    #         'book': book_data
    #     },
    #     'message': 'Book retrieved successfully'
    # }

    return jsonify(book_data), 200

#Add a new book (POST)
def add_book():
    new_book_data = request.get_json()
    new_book = Book(
        title=new_book_data['title'], 
        author=new_book_data['author'], 
        year=new_book_data['year'], ##
        category_id=new_book_data['category_id']    #Menghubungkan books dengan category
        )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added succesfully!', 'book': new_book.to_dict()}), 201

#Update a book (PUT)
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    update_data = request.get_json()
    book.title = update_data.get('title', book.title)
    book.author = update_data.get('author', book.author)
    book.year = update_data.get('year', book.year)
    book.category_id = update_data.get('category_id', book.category_id)

    db.session.commit()
    return jsonify({'message': 'Book updated succesfully!', 'book': book.to_dict()})

#Partially pdate a book (PATCH)
def patch_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    update_data = request.get_json()

    #Perbarui hanya jika data tersebut diberikan
    if 'title' in update_data:
        book.title = update_data['title']
    if 'author' in update_data:
        book.author = update_data['author']
    if 'year' in update_data:
        book.year = update_data['year']
    if 'category' in update_data:
        #Pastikan kategori ada sebelum meng-update
        category = Category.query.get(update_data['category_id'])
        if category:
            book.category_id = update_data['category_id']
        else:
            return jsonify({'error': 'Category not found'}), 404

    db.session.commit()    
    return jsonify({'message': 'Book update successfully!', 'book': book.to_dict()})

#Delete a book
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'})
