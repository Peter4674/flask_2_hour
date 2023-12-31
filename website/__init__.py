# INITIALIZING FLASK
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MSK'


# registering blueprints
    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
# done registering blueprints


    return app


#DONE INITIAILIZNG FLASK
