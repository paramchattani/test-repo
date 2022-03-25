
from flask_restful import   Resource  , reqparse 
from flask import Flask ,request
from   flask_jwt import jwt_required 
import sqlite3
from models.Item import ItemModel

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=str,required=True,help='mf this  canot be  blank')
    parser.add_argument('store_id',type=int,required=True,help='fill it mf')
    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name) # as.  it  is clas s method  t will return object  
        #return {'item': {'name': row[0],'price': row[1]}}
        if item: 
            return item.json()# to get the  dictionary  ;  
        return {'message':'Item not  found'} ,404
                #return{'message':f'there is  no item with {name} '}
    

    


    def  post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'item  already exists you fool'}
        
        data=Item.parser.parse_args()
        
        item=ItemModel(name,data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message':'exception occured'}, 500
        return {'name':name,'price':data['price']},201


    def  delete(self,name):
        item=ItemModel.find_by_name(name)
        if  item: 
            item.delete_from_db()
        return{'message': 'item deleted'}


        #error as  local variable given priority and  hence  it  is  wrong 

    def  put(self ,name):
       
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)
        if  item is None:
            item=ItemModel(name,data['price'],data['store_id'])
        else:
            item.price=data['price']
        item.save_to_db()
        return item.json()






class ItemList(Resource):
    def  get(self):
        return {'items': [item.json() for item  in ItemModel.query.all()]}

        


