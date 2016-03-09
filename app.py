"""Simple flask app to present & calculate the edit distance."""
import os

from flask import Flask, jsonify, abort, render_template, request

from wfdistance import distance

app = Flask(__name__)
app.debug = True


@app.errorhandler(400)
def handle_bad_request(error):
    """We provide json error payload for bad requests."""
    response = jsonify(error=error.description, status_code=400)
    return response, 400


@app.route("/")
def index():
    """Load our SPA."""
    return render_template("index.html")


@app.route("/api/v1/distance", methods=["POST"])
def calc_distance():
    """Calculate the edit distance and return distance.

    Both input & output are JSON
    """
    if not request.json:
        abort(400, "your request must be in JSON")

    try:
        data = request.get_json()
        payload = {
            "distance": distance(data["first"], data["second"])
        }
        return jsonify(**payload)
    except KeyError, e:
        abort(400, "missing value for %s" % e)
    except Exception, e:
        abort(400, "Unknown Error %s" % e)

if __name__ == "__main__":
    # Bind to PORT if defined, else default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
