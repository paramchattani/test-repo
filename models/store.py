#import  sqlite3
from db import db
class StoreModel(db.Model):
    __tablename__='stores'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    items=db.relationship('itemModel')

    def __init__(self,name):
        self.name=name;
        self.items

    def json(self):
        return {'name':self.name,'items':[item.json() for  item in self.items]}


    def save_to_db(self): 
        db.session.add(self)
        db.session.commit()

    @classmethod
    def  find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()# data  is converted  to itme model object
        
    def  delete_from_db(self):
        db.session.delete(self)
        db.session.commit();