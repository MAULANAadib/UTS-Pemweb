from flask import jsonify, request
from models.CategoryModel import Category
from config import db

###### Category ########
#Get all categories
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

#Get a single category by id
def get_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({'message': 'Category tidak ditemukan'}), 404
    return jsonify(category.to_dict())

#Add a new category (POST)
def add_category():
    new_category_data = request.get_json()
    new_category = Category(
        name = new_category_data['name']
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully!', 'category': new_category.to_dict()}), 201

#Update a category (PUT)
def update_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    
    update_data = request.get_json()
    category.name = update_data.get('name', category.name)

    db.session.commit()
    return jsonify({'message': 'Category updated successfully!', 'category': category.to_dict()})

#Delete a category (DELETE)
def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'})
