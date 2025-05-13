from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user, LoginManager
from .models import db, User

auth_bp = Blueprint('auth', __name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify(success=False, message='E-mail já cadastrado'), 400
    u = User(name=data['name'], email=data['email'])
    u.set_password(data['password'])
    db.session.add(u)
    db.session.commit()
    login_user(u)
    return jsonify(success=True)

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    u = User.query.filter_by(email=data['email']).first()
    if not u or not u.check_password(data['password']):
        return jsonify(success=False, message='Credenciais inválidas'), 401
    login_user(u)
    return jsonify(success=True)

@auth_bp.route('/api/forgot', methods=['POST'])
def forgot():
    data = request.get_json()
    # Aqui, apenas retornamos OK. Num MVP real, envie e-mail com token.
    return jsonify(success=True,
                   message='Se o e-mail existir, você receberá instruções.')
@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify(success=True)