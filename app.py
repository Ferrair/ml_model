import logging
from flask import Flask, jsonify, request

from config import Environment
from model.hs import reset_test, reset_prod

app = Flask(__name__)


@app.route('/api/healthz')
def healthz_api():
    # 探针
    return jsonify('OK')


@app.route('/api/hs/reset', methods=["POST"])
def manual_reset_api():
    data = request.get_json()
    T1 = data.get('T1', 135)
    T2 = data.get('T2', 120)
    environment = data.get('environment', Environment.TEST)
    logging.info('HS RESET-------------------------')
    logging.info(data)
    logging.info('HS RESET-------------------------')
    if environment == Environment.TEST:
        res = reset_test([str(T1), str(T2)])
        logging.info(res)
        return jsonify(res)
    elif environment == Environment.PROD:
        res = reset_prod([str(T1), str(T2)])
        logging.info(res)
        return jsonify(res)
    else:
        return jsonify("environment params error")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
