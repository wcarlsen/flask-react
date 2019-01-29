import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import cross_origin

app = Flask(__name__, static_folder="../client/build")


# Serve React App
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists("../client/build/" + path):
        return send_from_directory("../client/build", path)
    else:
        return send_from_directory("../client/build", "index.html")


@app.route("/test", methods=["GET"])
@cross_origin()
def test():
    return jsonify("TEST!")


if __name__ == "__main__":
    app.run(use_reloader=True, port=5000, threaded=True)
