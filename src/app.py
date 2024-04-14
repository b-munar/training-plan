from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.controllers.ping_controller import Ping
from src.controllers.exercise_controller import ExerciseController
from src.controllers.training_plan_controller import TrainingPlanController


def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    api.add_resource(Ping, '/training-plan/ping')
    api.add_resource(ExerciseController, '/training-plan/exercise')
    api.add_resource(TrainingPlanController, '/training-plan')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')
else:
    gunicorn_app = create_app()