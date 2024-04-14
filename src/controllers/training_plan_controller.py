from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.training_plan_model import TraningPlanModel, TrainingDayModel, TrainingDayExerciseModel
from src.schemas.training_plan_schema import TrainingPlanDeserializedSchema, TrainingPlanSerializedSchema
from src.utils.authorization import authorization

class TrainingPlanController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        training_plan_create_schema = TrainingPlanDeserializedSchema()
        
        errors = training_plan_create_schema.validate(request_json)
        if errors:
            print(errors)
            return "", 400
        
        training_plan_create_dump = training_plan_create_schema.dump(request_json)
        training_plan_create_dump["trainer"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_training_plan = TraningPlanModel(user=training_plan_create_dump["user"],trainer=training_plan_create_dump["trainer"] )
        session.add(new_training_plan)
        session.flush()
        print(training_plan_create_dump)
        for day in training_plan_create_dump["days"]:
            new_day = TrainingDayModel(day=day["day"], training_plan_id = new_training_plan.id)
            session.add(new_day)
            session.flush()
            for exercises in day["exercises"]:
                new_exercise = TrainingDayExerciseModel(exercise_id=exercises["id"], traning_day_id= new_day.id) 
                session.add(new_exercise)   
        session.commit()

        training_plan_created_schema = TrainingPlanSerializedSchema()
        training_plan_created_dump = training_plan_created_schema.dump(new_training_plan)
        return training_plan_created_dump, 201
    
    def get(self, **kwargs):
        training_plan_schema = TrainingPlanSerializedSchema()
        session = Session()
        if kwargs["user"]["role"] == 2:
            user = TraningPlanModel.trainer==kwargs["user"]["id"]
        else:
            user = TraningPlanModel.user==kwargs["user"]["id"]
        query = session.query(TraningPlanModel).filter(user)
        session.close()
        
        plans = [training_plan_schema.dump(plan) for plan in query]
        return {"plans":plans}, 200

