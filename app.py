
from flask import Flask ,request
from flask_restful import  Resource ,Api,reqparse  
from flask_jwt import JWT , jwt_required
from security import authenticate , identity
from resources.user import UserRegister
from resources.Item import Item 
from  resources.Item import ItemList
from db   import   db ;  
from resources.store import Store,StoreList
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] =  False
app.secret_key='param'

api=Api(app)

@app.before_first_request
def create_tables(): 
    db.create_all()

jwt=JWT(app,authenticate,identity)
#auth   end point  
# it  gets  password  and  username  and send  it  for authentication   
# it  gives  username and  password  to authenticate functio n 
#then goes  to identt=ity and return user    


#request to api is in request variabe hence  import request  




    


        

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/stores')
api.add_resource(Store,'/store/<string:name>')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)
    



