from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # # Configuration
    # app.config.from_pyfile('config.py')
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/api')
    
    return app