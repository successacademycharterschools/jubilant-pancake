"""Flask app for edit distance

For debugging, run like:

FLASK_APP=main.py flask run

Then access it at:

http://localhost:5000/source/target

"""

from flask import Flask
from editd import edit_distance


def create_app():
    app = Flask("jubilant-pancake")

    @app.route("/<source>/<target>")
    def edit_distance_service(source, target):
        return str(edit_distance(source, target))

    return app


if __name__ == '__main__':
    create_app()
