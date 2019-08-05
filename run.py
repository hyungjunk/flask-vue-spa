import os
import subprocess

from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={
    r"/api/*": {"origins": "*"},
    r"/hello/*": {"origins": "*"},
})


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


@app.route('/hello')
def hello():
    response = {
        'message': 'hello'
    }
    return jsonify(response)


def is_npm_running():
    url = "http://localhost:%s/" % 8080
    try:
        r1 = requests.get(url, timeout=0.5)
        running = True
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
        running = False
    return running


if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == "__main__":
#     app.config['DEBUG'] = True
#     try:
#         print('debug?')
#         if app.config['DEBUG']:
#             # if not is_npm_running():
#                 # print('running')
#                 # subprocess.Popen(
#                 #     (
#                 #             "cd frontend && npm run dev"
#                 #     ),
#                 #     shell=True
#                 # )
#             app.run(debug=True)
#     finally:
#         print('down')
