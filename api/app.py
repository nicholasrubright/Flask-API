from flask import Flask, redirect, url_for
from src.routes import api_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    
    app.register_blueprint(api_bp, url_prefix='/api')
    
    
    @app.route('/')
    def index():
        return redirect(url_for('api_bp.index'))
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080)