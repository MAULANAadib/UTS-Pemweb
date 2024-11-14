from config import db

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), nullable=False, unique=True)

    #Relasi dengan Borrower (one-to-many)
    borrower = db.relationship('Borrower', backref='status', lazy=True)

    def to_dict(self):
        return {
            'id': self.id, 
            'status': self.status
            }