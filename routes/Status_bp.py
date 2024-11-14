from flask import Blueprint
from controllers.StatusController import get_statuses, get_status, add_status, update_status, delete_status

status_bp = Blueprint ('status_bp', __name__)

#Routes for Get all status
status_bp.route('/api/status', methods=['GET'])(get_statuses)

#Routes for Get a single status (GET)
status_bp.route('/api/status/<id>', methods=['GET'])(get_status)

#Routes for Add a new status (POST)
status_bp.route('/api/status', methods=['POST'])(add_status)

#Routes for Update a status (PUT)
status_bp.route('/api/status/<id>', methods=['PUT'])(update_status)

#Routes for Delete a status (DELETE)
status_bp.route('/api/status/<id>', methods=['DELETE'])(delete_status)