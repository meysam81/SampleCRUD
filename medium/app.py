from flask import Flask
from http import HTTPStatus


from medium.database import db
from medium.config import Config
from medium.books import app as books_app


def create_app(config: Config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(books_app, url_prefix="/api/v1")

    @app.route("/", provide_automatic_options=False)
    def index():
        return "Welcome, I'm ready when you are", HTTPStatus.OK

    return app
