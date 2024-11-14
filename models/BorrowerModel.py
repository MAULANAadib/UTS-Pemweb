from config import db

class Borrower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False)

    #Foreign key ke tabel Book
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    #Foreign key ke tabel Status
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'borrower': self.borrower,
            'email': self.email,
            'phone': self.phone,
            'book_id': self.book_id,
            'status_id': self.status_id
        }