import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from .config import Config
from .models import db, User
from .auth import auth_bp, login_manager

def create_app():
    app = Flask(__name__, static_folder='../static', static_url_path='/')
    app.config.from_object(Config)
    CORS(app, supports_credentials=True)
    
    # Inicializa DB e Login
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Registra blueprints
    app.register_blueprint(auth_bp)
    
    # Cria tabelas se não existirem
    with app.app_context():
        db.create_all()

    # Rota para servir index.html e demais arquivos estáticos
    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.errorhandler(404)
    def not_found(e):
        # Qualquer rota desconhecida retorna index (SPA)
        return send_from_directory(app.static_folder, 'index.html')
    
    return app

""" 
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    # Para rodar o app diretamente, descomente a linha abaixo 
"""
# Para rodar o app diretamente, descomente a linha abaixo
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080)
    # app.run(debug=True)