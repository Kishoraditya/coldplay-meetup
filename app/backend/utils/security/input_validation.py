from marshmallow import Schema, fields, validate

class ProfileSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email()
    mobile = fields.Str(validate=validate.Regexp(r'^\+?[1-9]\d{9,14}$'))
    seat_section = fields.Str(required=True)
    attendance_date = fields.DateTime(required=True)
    scam_meter = fields.Int(validate=validate.Range(min=1, max=10))

def validate_profile(data):
    schema = ProfileSchema()
    return schema.load(data)
