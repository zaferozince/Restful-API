from flask_restful import reqparse, abort, Resource
from endpoints import DBHelper 

parser = reqparse.RequestParser()
parser.add_argument('id',type=str)
parser.add_argument('name',type=str)
parser.add_argument('customer_id',type=str)
parser.add_argument('park_lot',type=str)


class Registration(Resource):
    def get(self):
        args = parser.parse_args()
        db=DBHelper.DBHelper()
        result2 = db.customerLogin(args.name)
        type(args.customer_id)
        if str(result2) == args.customer_id :
            result = db.registrationSelect(args.customer_id)
            return result 
        else:
            return "Bu id size ait değildir!!"
   
    def post(self):
        pass
    def put(self):
        args = parser.parse_args()
        db=DBHelper.DBHelper()
        result = db.park_parkinglot(args.customer_id,args.park_lot)
        return result
    def delete(self):
        args = parser.parse_args()
        db=DBHelper.DBHelper()
        result = db.park_exit(args.customer_id)
        return result