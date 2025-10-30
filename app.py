from flask import Flask 
from config import Config
from extensions import db, jwt, ma
import routes 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)


    app.register_blueprint(routes.bp)
    app.register_blueprint(routes.bp_auth)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

