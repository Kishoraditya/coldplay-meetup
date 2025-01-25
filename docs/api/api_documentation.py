from flask_restx import Api, Resource, fields

from app.backend.models import User


api = Api(
    title='Coldplay Meetup API',
    version='1.0',
    description='API for managing concert meetups'
)

user_model = api.model('User', {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'seat_section': fields.String,
    'attendance_date': fields.DateTime
})

@api.route('/api/users')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return User.query.all()

