from flask_restful import reqparse, abort, Resource
from endpoints import DBHelper 

parser = reqparse.RequestParser()
parser.add_argument('id',type=str)
parser.add_argument('customer_id',type=str)
parser.add_argument('repletion',type=str)
parser.add_argument('parkingLot',type=str)

class Park(Resource):
    def get(self):
        args = parser.parse_args()
        db= DBHelper.DBHelper()
        if(db.adminControl(args.customer_id) == 1):
            result = db.parkSelect(args.id)
            return result
        else:
            return "Admin değilsiniz erişemezsiniz!!"
          
    def post(self):
        args = parser.parse_args()
        db = DBHelper.DBHelper()
        if(db.adminControl(args.customer_id) == 1):
            result = db.parkUpdate(args.id,args.repletion,args.parkingLot)
            return result
        else:
            return "Admin değilsiniz erişemezsiniz!!"

    def put(self):
        args = parser.parse_args()
        db=DBHelper.DBHelper() 
        if(db.adminControl(args.customer_id) == 1):
            result = db.parkAdd(args.parkingLot)
            return result
        else:
            return "Admin değilsiniz erişemezsiniz!!"
              
    def delete(self):
        args = parser.parse_args()
        db = DBHelper.DBHelper()
        if(db.adminControl(args.customer_id) == 1):
            result = db.parkDelete(args.id)
            return result
        else:
            return "Admin değilsiniz erişemezsiniz!!"
        
