from flask_restful import reqparse, abort, Resource
from endpoints import DBHelper 

class GetAll(Resource):
    def get(self):
        db=DBHelper.DBHelper()
        result =db.getAllPark()
        return result
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass