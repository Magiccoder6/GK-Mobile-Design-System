import os

from flask import Flask, render_template, send_from_directory


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,  static_folder='static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template("index.html")
    
    @app.route('/style_guide')
    def style_guide():
        return send_from_directory(app.static_folder, 'flutter_output/index.html')

    return app