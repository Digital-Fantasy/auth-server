import blueprints
from flask import Flask
from utils import get_env_var

app = Flask(__name__)

app.config["SECRET_KEY"] = get_env_var("FLASKKEY")
app.register_blueprint(blueprints.root_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Don't forget about 0.0.0.0 if you actually want things to connect
