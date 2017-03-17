from django.db import connection
class UserAuth(object):
	__auth =  0
	__member = 0
	l = [1,2,3,4,65,69]
	uid = 99999999
		
	def __init__(self,uid)	:
		self.uid=uid

	def is_auth(self):
		cursor = connection.cursor()
		num=cursor.execute("select gid from power where uid=%s" % self.uid)
		for gid in cursor.fetchmany(num):
			if gid[0]==71:
				self.__auth= 1
				break
		return self.__auth
	def is_member(self):
		cursor = connection.cursor()
		num=cursor.execute("select gid from power where uid=%s" % self.uid)
		for gid in cursor.fetchmany(num):
			if gid[0] in  self.l:	
				self.__member= 1
				break
		return self.__member
			
