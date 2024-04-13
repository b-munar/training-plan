from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.exercise_model import ExerciseModel
from src.schemas.exercise_schema import ExerciseSerializeSchema, ExerciseDeserializeSchema
from src.utils.authorization import authorization

class ExerciseController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        excercise_create_schema = ExerciseDeserializeSchema()
        
        errors = excercise_create_schema.validate(request_json)
        if errors:
            return "", 400
        
        excercise_create_dump = excercise_create_schema.dump(request_json)
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_exercie = ExerciseModel(**excercise_create_dump)
        session.add(new_exercie)
        session.commit()

        excercise_created_schema = ExerciseSerializeSchema()
        excercise_created_dump = excercise_created_schema.dump(new_exercie)
        return excercise_created_dump, 201
    
    def get(self, **kwargs):
        excercise_schema = ExerciseSerializeSchema()

        session = Session()
        query = session.query(ExerciseModel)
        session.close()
        
        exercises = [excercise_schema.dump(exercise) for exercise in query]
        return {"exercises":exercises}, 200

