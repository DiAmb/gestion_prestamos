from flask import Flask
from flask_cors import CORS

from views.view import app

CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
