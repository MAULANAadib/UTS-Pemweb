from flask import jsonify, request
from models.BorrowerModel import Borrower
from models.BookModel import Book
from models.StatusModel import Status
from config import db

##### borrower #####
#GET all borrower
def get_borrowers():
    borrowers = Borrower.query.all()
    borrowers_with_booksstatus = []

    for borrower in borrowers:
        #Ambil book terkait dari book
        book = Book.query.get(borrower.book_id)
        #Ambil status terkait dari status
        status = Status.query.get(borrower.status_id)

        #
        borrowers_with_booksstatus.append({
            'id': borrower.id,
            'borrower': borrower.borrower,
            'email': borrower.email,
            'phone': borrower.phone,
            'book_borrower': book.title if book else " No Books Borrowed",
            'status_borrower': status.status if status else "No Membership Status"
        })

    response = {
        'status': 'success',
        'data': {
            'borrowers': borrowers_with_booksstatus
        },
        'message': 'borrowers retrieved successfully'
    }
    return jsonify(response), 200

#Get a single borrower by with book borrower(GET)
def get_borrower(id):
    borrower = Borrower.query.get(id)
    if not borrower:
        return jsonify({'message': 'borrower tidak ditemukan'}), 404
    
    #Ambil book terkait dari borrower
    book = Book.query.get(borrower.book_id)
    #Ambil status terkait dari status
    status = Status.query.get(borrower.status_id)
    #Jika book tidak ditemukan, maka book_borrower akan menjadi " No Books Borrowed"
    borrower_data = {
        'id': borrower.id,
        'borrower': borrower.borrower,
        'email': borrower.email,
        'phone': borrower.phone,
        'book_borrower': book.title if book else " No Books Borrowed",
        'status_borrower': status.status if status else "No Membership Status"

    }
    response = {
        'status': 'success',
        'data': {
            'borrower': borrower_data
        },
        'message': 'borrower retrieved successfully'
    }

    return jsonify(response), 200

#Add a new borrower (POST)
def add_borrower():
    new_borrower_data = request.get_json()
    new_borrower = Borrower(
        borrower=new_borrower_data['borrower'],
        email=new_borrower_data['email'],
        phone=new_borrower_data['phone'],
        book_id=new_borrower_data['book_id'],
        status_id=new_borrower_data['status_id']
    )
    db.session.add(new_borrower)
    db.session.commit()
    return jsonify({'message': 'borrower added successfully!', 'borrower': new_borrower.to_dict()}), 201

#Update a borrower(PUT)
def update_borrower(id):
    borrower = Borrower.query.get(id)
    if not borrower:
        return jsonify({'message': 'borrower tidak ditemukan'}), 404
    
    update_borrower = request.get_json()
    borrower.borrower = update_borrower.get('borrower', borrower.borrower)
    borrower.email = update_borrower.get('email', borrower.email)
    borrower.phone = update_borrower.get('phone', borrower.phone)
    borrower.book_id = update_borrower.get('book_id', borrower.book_id)
    borrower.status_id = update_borrower.get('status_id', borrower.status_id)

    db.session.commit()
    return jsonify({'message': 'borrower updated successfully!', 'borrower': borrower.to_dict()})

#Partially update a borrower (PATCH)
def patch_borrower(id):
    borrower = Borrower.query.get(id)
    if not borrower:
        return jsonify({'message': 'borrower tidak ditemukan'}), 404
    
    update_data = request.get_json()

    #Perbarui hanya jika data tersebut diberikan
    if 'borrower' in update_data:
        borrower.borrower = update_data['borrower']
    if 'email' in update_data:
        borrower.email = update_data['email']
    if 'phone' in update_data:
        borrower.phone = update_data['phone']
    if 'book' in update_data:
        #Pastikan book ada sebelum update
        book = Borrower.query.get(update_data['book_id'])
        if book:
            borrower.book_id = update_data['book_id']
        else:
            return jsonify({'message': 'book tidak ditemukan'}), 404
    if 'status' in update_data:
        status = Borrower.query.get(update_data['status_id'])
        if status:
            borrower.status_id = update_data['status_id']
        else:
            return jsonify({'message': 'status tidak ditemukan'}), 404
        
    db.session.commit()
    return jsonify({'message': 'borrower updated successfully!', 'borrower': borrower.to_dict()})

#Delete a borrower(DELETE)
def delete_borrower(id):
    borrower = Borrower.query.get(id)
    if not borrower:
        return jsonify({'message': 'borrower tidak ditemukan'}), 404
    
    db.session.delete(borrower)
    db.session.commit()
    return jsonify({'message': 'borrower deleted successfully!'})
