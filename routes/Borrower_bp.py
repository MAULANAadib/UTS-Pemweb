from flask import Blueprint
from controllers.BorrowerController import get_borrowers, get_borrower, add_borrower, patch_borrower, delete_borrower, update_borrower

borrower_bp = Blueprint('borrower_bp', __name__)

#Routes for Get all borrower
borrower_bp.route('/api/borrowers', methods=['GET'])(get_borrowers)

#Routes for Get a single borrower (GET)
borrower_bp.route('/api/borrowers/<id>', methods=['GET'])(get_borrower)

#Routes for Add a new borrower (POST)
borrower_bp.route('/api/borrowers', methods=['POST'])(add_borrower)

#Routes for Update a borrower(PUT)
borrower_bp.route('/api/borrowers/<id>', methods=['PUT'])(update_borrower)

#Routes for partially update a borrower (PATCH)
borrower_bp.route('/api/borrowers/<id>', methods=['PATCH'])(patch_borrower)

#ROutes for Delete a borrower (DELETE)
borrower_bp.route('/api/borrowers/<id>', methods=['DELETE'])(delete_borrower)
