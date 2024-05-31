from flask import Flask
from app.controllers import bp as app_bp

app = Flask(__name__)
app.register_blueprint(app_bp)

if __name__ == '__main__':
    app.run(debug=True)
