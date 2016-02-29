from mongoengine import *
import datetime 

class log(Document):
	cid=IntField()
	name=StringField()
	algorithm=StringField()
	result=StringField()
	time=DateTimeField(default=datetime.datetime.now)  
	
class config(Document):
	cid=IntField()
	name=StringField()
	address=StringField()
	algorithm=ListField()
	prefix=StringField()
	suffix=StringField()
	algname=ListField()

class algConfig(Document):
	aid=IntField()
	algorithm=StringField()
	config=DictField()

