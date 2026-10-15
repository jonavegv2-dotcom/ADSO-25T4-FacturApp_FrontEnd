from flask import Flask

def create_app():
<<<<<<< HEAD

    app = Flask(__name__)

    from controllers.home_controller import home_bp
    from controllers.clients_controller import clients_bp
    from controllers.categories_controller import categories_bp
    from controllers.users_controller import users_bp
    from controllers.products_controller import products
=======
    app = Flask(__name__)

    from src.controllers.home_controller import home_bp
    from src.controllers.clients_controller import clients_bp
    from src.controllers.categories_controller import categories_bp
>>>>>>> 4b6a7ad8b2ccd3b7a7c6ec443f8eb5911a3f63cd

    app.register_blueprint(home_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(categories_bp)
<<<<<<< HEAD
    app.register_blueprint(users_bp)
    app.register_blueprint(products)

    return app
=======

    return app



>>>>>>> 4b6a7ad8b2ccd3b7a7c6ec443f8eb5911a3f63cd
