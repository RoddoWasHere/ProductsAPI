from adapters.database_adapter import DatabaseAdapter

class Attribute:
	def __init__(self):
		self.db_adapter = DatabaseAdapter()
	
	def get_attributes(self):
		return self.db_adapter.get_all("SELECT * FROM attribute;")
		
	def insert_attribute(self, name):
		return self.db_adapter.insert("INSERT INTO attribute (name) VALUES ('%s');" % name)

