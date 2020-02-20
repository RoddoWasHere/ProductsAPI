#from models.products import Product, Attribute, ProductAttribute
from models.product import Product
from models.attribute import Attribute
from models.product_attribute import ProductAttribute


#Improve: 

#ignore updates with no changes (caching)
	
	
class ProductsController():

	def __init__(self):
		self.product_model = Product()
		self.attribute_model = Attribute();
		self.product_attribute_model = ProductAttribute();
	
	def get_products(self):
		results = []
		products = self.product_model.get_products().list
		for product in products:
			product_dict = {"sku": product["sku"] }
			attributes = self.product_attribute_model.get_product_attributes(product["sku"]).list;
			
			attributes_dict = {}
			for attribute in attributes:
				attributes_dict[attribute["attribute_name"]] = attribute["value"]
			
			product_dict["attributes"] = attributes_dict
			results.append(product_dict)
		return results
	
	def add_products(self, products):
		existing_products_lookup = self.product_model.get_products().lookup
		all_attributes_lookup = self.attribute_model.get_attributes().lookup
		
		for product in products:
			#check if product exists
			if(existing_products_lookup.get(product["sku"]) == None): # no such product -> add it
				self.product_model.insert_product(product["sku"])
		
			if(product.get("attributes") == None): # delete product
				self.product_model.delete_product(product["sku"])
				self.product_attribute_model.delete_all_product_attributes(product["sku"])
				return
				
			attributes_dict =  self.product_attribute_model.get_product_attributes(product["sku"]).lookup

			for attribute_key, attribute_value in product["attributes"].items():
				# check attribute exists
				if(all_attributes_lookup.get(attribute_key) == None): # attribute doesn't exist -> add it
					self.attribute_model.insert_attribute(attribute_key);
					self.product_attribute_model.insert_product_attribute(
						sku = product["sku"],
						attribute_name = attribute_key,
						value = attribute_value
					)
				else: # attribute exists -> check if product has it
					if(attributes_dict.get(attribute_key) == None): # product attribute doesn't exist
						if(attribute_value != None):
							self.product_attribute_model.insert_product_attribute(
								sku = product["sku"],
								attribute_name = attribute_key,
								value = attribute_value
							)
					else: # product attribute does exist
						if(attribute_value != None): # update product attribute
							self.product_attribute_model.update_product_attribute(
								sku = product["sku"],
								attribute_name = attribute_key,
								value = attribute_value
							)
						else: # delete product attribute
							print("deleting: " + attribute_key)
							self.product_attribute_model.delete_product_attribute(
								sku = product["sku"],
								attribute_name = attribute_key,
							)
	
	def clean_up_attributes(self):
		pass
		