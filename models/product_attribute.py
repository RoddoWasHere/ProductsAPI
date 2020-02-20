from adapters.database_adapter import DatabaseAdapter

class ProductAttribute:
	def __init__(self):
		self.db_adapter = DatabaseAdapter()
		
	def get_product_attributes(self, sku):
		return self.db_adapter.get_all("SELECT attribute_name, value FROM product_attribute WHERE product_sku = '%s';" % sku)
		
	def insert_product_attribute(self, sku, attribute_name, value):
		return self.db_adapter.insert("INSERT INTO product_attribute (product_sku, attribute_name, value) VALUES ('%s', '%s', '%s');" % (sku, attribute_name, value))

	def update_product_attribute(self, sku, attribute_name, value):
		self.db_adapter.update("UPDATE product_attribute SET value = '%s' WHERE product_sku = '%s' AND attribute_name = '%s';" % (value, sku, attribute_name))
	
	def delete_product_attribute(self, sku, attribute_name):
		self.db_adapter.delete("DELETE FROM product_attribute WHERE product_sku = '%s' AND attribute_name = '%s';" % (sku, attribute_name))
		
	def delete_all_product_attributes(self, sku):
		self.db_adapter.delete("DELETE FROM product_attribute WHERE product_sku = '%s';" % (sku))
		
