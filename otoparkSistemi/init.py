from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from endpoints import NewAllUser
from endpoints import User
from endpoints import Park
from endpoints import GetAll
from endpoints import Registration
from endpoints import Login
app = Flask(__name__)
api = Api(app)

api.add_resource(NewAllUser.NewAllUser, '/user')
api.add_resource(User.User,'/users')
api.add_resource(Park.Park,'/park')
api.add_resource(GetAll.GetAll,'/all')
api.add_resource(Registration.Registration,'/regs')
api.add_resource(Login.Login,'/login')

if __name__ == '__main__':
    app.run(debug = True , host="0.0.0.0", port=9696)
