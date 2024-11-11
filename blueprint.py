from flask import blueprints, request

from services import register_email, check_inventory

action_bp  = blueprints.Blueprint('action_bp', __name__)

@action_bp.route('/sing_up', methods=['POST'])
def sing_up():
    email = request.json.get('email')
    if not email:
        return {'error': 'Missing email'}, 400

    result = register_email(email)
    if result[0]:
        return {'status': result[1]}, 201
    else:
        return {'error': result[1]}, 400


@action_bp.route('/buy', methods=['POST'])
def buy():
    data = request.get_json()
    if not data:
        return {'error': 'Missing data'}, 400

    result = check_inventory(data)
    if result[0]:
        return {'status': result[1]}, 200
    else:
        return {'error': result[1]}, 400