from flask_restful import reqparse, abort, Resource
from endpoints import DBHelper 

parser = reqparse.RequestParser()
parser.add_argument('id',type=str)
parser.add_argument('name',type=str)
parser.add_argument('birthday',type=str)
parser.add_argument('phone_number',type=str)

class NewAllUser(Resource):
    def get(self):
        args = parser.parse_args()
        db=DBHelper.DBHelper()
        if(db.adminControl(args.id) == str(1)):
            result = db.getAllCustomer()
            return result
        else:
            return "Admin değilsiniz erişemezsiniz!!"
    def post(self):
        pass
    def put(self):
        args = parser.parse_args()
        db=DBHelper.DBHelper()
        result = db.customerAdd(args.name,args.birthday,args.phone_number)
        return result
    def delete(self):
        pass
