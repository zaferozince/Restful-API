from flask_restful import reqparse, abort, Resource
from endpoints import DBHelper 

parser = reqparse.RequestParser()
parser.add_argument('id',type=str)
parser.add_argument('name',type=str)
parser.add_argument('birthday',type=str)
parser.add_argument('phone_number',type=str)

class User(Resource):
    def get(self):
        args = parser.parse_args()
        db=DBHelper.DBHelper() 
        user_dict = db.customerSelect(args.id)
        return user_dict
        
    def post(self):
        args = parser.parse_args()
        db = DBHelper.DBHelper()
        if(args.name != None):
            user_dict = db.customerUpdateName(args.id,args.name)
        if(args.birthday != None):
            user_dict2 = db.customerUpdateBirthday(args.id,args.birthday)
        if(args.phone_number != None):
            user_dict3 = db.customerUpdatePhonenumber(args.id,args.phone_number)
        if(user_dict != False or user_dict2 != False or user_dict3 != False):
            return "Update edilmiştir"
        else:
            return "Yanlış Update işlemi yaptınız"

    def put(self):
        pass
    def delete(self):
        args = parser.parse_args()
        db = DBHelper.DBHelper()
        delete_result = db.customerDelete(args.id)
        return delete_result
