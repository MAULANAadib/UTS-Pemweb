from flask import Blueprint
from controllers.CategoryController import get_categories, get_category, add_category, update_category, delete_category

category_bp = Blueprint('Category_bp', __name__)

#Routes for Get all categories
category_bp.route('/api/category', methods=['GET'])(get_categories)

#Routes for Get a single category by id (GET)
category_bp.route('/api/category/<id>', methods=['GET'])(get_category)

#Routes for a new category (POST)
category_bp.route('/api/category', methods=['POST'])(add_category)

#Routes for Update a category (PUT)
category_bp.route('/api/category/<id>', methods=['PUT'])(update_category)

#Routes for Delete a category (DELETE)
category_bp.route('/api/category/<id>', methods=['DELETE'])(delete_category)
