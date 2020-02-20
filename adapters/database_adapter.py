import mysql.connector

class Utils:
	@classmethod
	def DictListToLookupDict(cls, dict_list, index_field=None):
		lookup = {}
		
		if(len(dict_list)>0 and index_field==None):# default to first field
			index_field = list(dict_list[0].keys())[0]
		
		for dict in dict_list:
			key = dict[index_field]
			lookup[key] = dict
		
		return lookup

class QueryResult:
	def __init__(self, list, lookup):
		self.list = list
		self.lookup = lookup
		
class DatabaseAdapter: # Singleton
	class __DatabaseAdapterConfig:
		def __init__(self):
			self.mydb = mysql.connector.connect(
				host="localhost",
				user="root",
				passwd="",
			)
			self.cursor = self.mydb.cursor(dictionary=True)
			try:
				self.cursor.execute("USE ProductsRoderichDB;");
			except:
				pass
	
	instance = None

	def __init__(self):
		DatabaseAdapter.__initialize()
		
	@classmethod
	def __initialize(cls):
		if(cls.instance == None):# instantiate
			cls.instance = DatabaseAdapter.__DatabaseAdapterConfig()
	
	def get_all(self, query):
		inst = DatabaseAdapter.instance
		
		results = []
		inst.cursor.execute(query)
		dict_list = inst.cursor.fetchall()
		lookup_dict = Utils.DictListToLookupDict(dict_list)
		return QueryResult(dict_list, lookup_dict)
	
	def execute(self, query):
		inst = DatabaseAdapter.instance
		
		inst.cursor.execute(query)
	
	def insert(self, query):
		inst = DatabaseAdapter.instance
		
		inst.cursor.execute(query)
		inst.mydb.commit()
		return inst.cursor.lastrowid
	
	def update(self, query):
		inst = DatabaseAdapter.instance
		
		inst.cursor.execute(query)
		inst.mydb.commit()
		
	def delete(self, query):
		inst = DatabaseAdapter.instance
		
		inst.cursor.execute(query)
		inst.mydb.commit()
		
		
