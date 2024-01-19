from flask import Flask
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/lotto')
def make_lotto():
    numbers = range(1, 46)
    # sample 비복원 랜덤 추출 이미 뽑았던 것은 뽑지 않고 추출
    # random.sample(후보, 갯수)
    lotto = random.sample(numbers, 6)
    return sorted(lotto)


if __name__ == '__main__':
    app.run(debug=True)