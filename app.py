import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from Routes.routes import bp

app = Flask(__name__)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug='True', port=5000)