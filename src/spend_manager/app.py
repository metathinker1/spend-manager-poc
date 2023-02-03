from flask import Flask
from flask import request
import logging

PORT = 6304

app = Flask(__name__)


@app.route('/spendmanager/ping', methods=['GET'])
def ping():
    return 'pong'


if __name__ == '__main__':
    logging.info('Starting Flask')
    app.run(host='0.0.0.0', debug=False, port=PORT, threaded=True)

