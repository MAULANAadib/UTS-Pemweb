from config import app, db
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp
from routes.Borrower_bp import borrower_bp
from routes.Status_bp import status_bp

app.register_blueprint(book_bp)
app.register_blueprint(category_bp)
app.register_blueprint(borrower_bp)
app.register_blueprint(status_bp)

@app.route("/")
def home():
    return "API"

db.create_all()


# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)