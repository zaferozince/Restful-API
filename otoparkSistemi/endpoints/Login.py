from flask_restful import reqparse, abort, Resource
from endpoints import DBHelper 

parser = reqparse.RequestParser()
parser.add_argument('name',type=str)

class Login(Resource):
    def get(self):
        args = parser.parse_args()
        db = DBHelper.DBHelper()
        result=db.customerLogin(args.name)
        return result
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass