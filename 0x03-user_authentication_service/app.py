#!/usr/bin/env python3
""" App module """

from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run()