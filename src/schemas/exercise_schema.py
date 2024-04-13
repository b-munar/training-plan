from marshmallow import Schema, fields

class ExerciseDeserializeSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    description = fields.String()
    timing_minutes = fields.Float()
    image_url= fields.String()
    muscular_group = fields.String()

class ExerciseSerializeSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    description = fields.String()
    timing_minutes = fields.Float()
    image_url= fields.String()
    muscular_group = fields.String()
    