from adapters.database_adapter import DatabaseAdapter

class Product:
	def __init__(self):
		self.db_adapter = DatabaseAdapter()
		
	def get_products(self):
		return self.db_adapter.get_all("SELECT * FROM product;")
		
	def insert_product(self, sku):
		return self.db_adapter.insert("INSERT INTO product (sku) VALUES ('%s');" % sku)
		
	def delete_product(self, sku):
		self.db_adapter.delete("DELETE FROM product WHERE sku = '%s'" % sku)

