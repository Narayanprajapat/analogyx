from flask import Flask
from flask_cors import CORS
import os


app = Flask(__name__)
app.config['CORS-HEADERS'] = 'Content-Type'
app.config['MONGO_URL'] = os.getenv('DATABASE_URL')
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
