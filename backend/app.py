from flask import Flask


def create_app():
    app = Flask(__name__)

    # Load the config from object
    app.config.from_object('config.Config')

    # Initialize extensions, routes, and other app configurations here

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()