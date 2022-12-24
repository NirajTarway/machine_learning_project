from flask import Flask
from Housing.logger import logging
from Housing.exception import HousingException
import sys
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception('Custom exception raised in index file')
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)

    logging.info('main index file running')

    return 'machine learning with ci-cd_11'


if __name__ == '__main__':
    app.run(debug=True)
