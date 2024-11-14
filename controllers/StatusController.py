from flask import jsonify, request
from models.StatusModel import Status
from config import db

##### status #####
# status routes
def get_statuses():
    status = Status.query.all()
    return jsonify([status.to_dict() for status in status])

#Get a single status by id
def get_status(id):
    status = Status.query.get(id)
    if not status:
        return jsonify({'message': 'status tidak ditemukan'}), 404
    return jsonify(status.to_dict())

#Add a new status
def add_status():
    new_status_data = request.get_json() 
    new_status = Status(
        status=new_status_data['status']
    )
    db.session.add(new_status)
    db.session.commit()
    return jsonify({'message': 'status added successfully!', 'status': new_status.to_dict()}), 201

#Update a status (PUT)
def update_status(id):
    status = Status.query.get(id)
    if not status:
        return jsonify({'error': 'status not found'}), 404
    
    update_status = request.get_json()
    status.status = update_status.get('status', status.status)

    db.session.commit()
    return jsonify({'message': 'status updated successfully!', 'status': status.to_dict()})

#Delete a status(DELETE)
def delete_status(id):
    status = Status.query.get(id)
    if not status:
        return jsonify({'message': 'status tidak ditemukan'}), 404
    
    db.session.delete(status)
    db.session.commit()
    return jsonify({'message': 'status deleted successfully!'})
