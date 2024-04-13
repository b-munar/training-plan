from flask import Flask
from flask_restful import Api
from src.controllers.ping_controller import Ping
from src.controllers.exercise_controller import ExerciseController

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Ping, '/exercise/ping')
    api.add_resource(ExerciseController, '/exercise')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')
else:
    gunicorn_app = create_app()