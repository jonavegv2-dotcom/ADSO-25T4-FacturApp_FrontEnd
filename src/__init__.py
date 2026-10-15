from flask import Flask

def create_app():

    app = Flask(__name__)

    from controllers.home_controller import home_bp
    from controllers.clients_controller import clients_bp
    from controllers.categories_controller import categories_bp
    from controllers.users_controller import users_bp
    from controllers.products_controller import products

    app.register_blueprint(home_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(products)

    return app
