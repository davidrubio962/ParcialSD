from flask import request, Flask
import json


app5 = Flask(__name__)


@app5.route('/')
def hello_world():
    return 'Salam alikom, this is App3 :) '


if __name__ == '__main__':
   app5.run(debug=True, host='0.0.0.0')
