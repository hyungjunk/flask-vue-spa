import collections

from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import flask as fl
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


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     if app.debug:
#         return requests.get('http://localhost:8080/{}'.format(path)).text
#     return render_template("index.html")


@app.route('/hello')
def hello():
    response = {
        'message': 'hello'
    }
    return jsonify(response)


@app.route('/data-post', methods=["GET", "POST"])
def data_post():

    import json
    import requests

    if fl.request.method == "GET":
        return fl.render_template('json_poster.html')
    else:

        # todo : FRONT
        # 2. Key Row는 Coloring 할 수 있도록 (Done)
        # 3. 보내는 Data type의 select box
        # 4. 보내는 Row, Col의 제거를 자유롭게.

        # todo : Back
        # 1. 코드 정리
        # 3.

        raw_result = json.loads(fl.request.form['data'])
        class POSTData:

            def __init__(self, raw_result):
                self.result = raw_result['data']
                self.url_to_send = raw_result['url']
                self.key_col_idx = int(raw_result['key_col'])

            def parse_data(self):
                self.DataRow = collections.namedtuple('DataRow', self.result.pop(0))

            def save_data(self):
                for row in self.result:
                    url_prefix = self.url_to_send
                    data = self.DataRow(*row)
                    if not all([True if el else False for el in [*row]]) is None:
                        break
                    url = url_prefix  + "/" + row[self.key_col_idx - 1]
                    if not url.startswith("http://"):
                        url = "http://" + url
                    wrapped_result = dict()
                    wrapped_result['rows'] = '[' + json.dumps(data._asdict()) + ']'
                    requests.post(
                        url,
                        data=wrapped_result,
                        headers=self.production_h
                    )

        pd = POSTData(raw_result)
        pd.parse_data()
        pd.save_data()

        return fl.jsonify(dict(status=200))


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
