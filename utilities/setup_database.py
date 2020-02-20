from adapters.database_adapter import DatabaseAdapter
from models.product import Product
from models.attribute import Attribute
from models.product_attribute import ProductAttribute

db_adapter = DatabaseAdapter()

#init DB
drop_db = "DROP DATABASE IF EXISTS ProductsRoderichDB;"
create_db = "CREATE DATABASE IF NOT EXISTS ProductsRoderichDB;"
select_db = "USE ProductsRoderichDB;"

drop_product_attribute_table = "DROP TABLE IF EXISTS product_attribute;"
drop_product_table = "DROP TABLE IF EXISTS product;"
drop_attribute_table = "DROP TABLE IF EXISTS attribute;"

#create tables
create_products_table = """
CREATE TABLE IF NOT EXISTS product(
	sku varchar(255) NOT NULL UNIQUE, -- non-standardized (vendor specific),
	PRIMARY KEY (sku)
);"""
create_attribute_table = """
CREATE TABLE IF NOT EXISTS attribute (
	name varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (name)
);"""
create_product_attribute_table = """
CREATE TABLE IF NOT EXISTS product_attribute(
	product_sku varchar(255) NOT NULL, -- rename to product_sku
	attribute_name varchar(255) NOT NULL,
	value varchar(255),
	PRIMARY KEY (product_sku, attribute_name)
);"""



def clear_database():
	db_adapter.execute(drop_db);
	db_adapter.execute(create_db);
	db_adapter.execute(select_db);
	
	db_adapter.execute(drop_product_attribute_table);
	db_adapter.execute(drop_product_table);
	db_adapter.execute(drop_attribute_table);

	
def create_tables():
	db_adapter.execute(create_products_table);
	db_adapter.execute(create_attribute_table);
	db_adapter.execute(create_product_attribute_table);
	
def populate_tables():
	product_model = Product()
	attribute_model = Attribute()
	product_attribute_model = ProductAttribute()
	
	product_model.insert_product('abc')
	
	attribute_model.insert_attribute('size')
	attribute_model.insert_attribute('grams')
	attribute_model.insert_attribute('foo')
	
	product_attribute_model.insert_product_attribute('abc','size','small')
	product_attribute_model.insert_product_attribute('abc','grams','100')
	product_attribute_model.insert_product_attribute('abc','foo','bar')
	
	product_model.insert_product('xyz')
	
	attribute_model.insert_attribute('color')
	attribute_model.insert_attribute('kg')
	attribute_model.insert_attribute('ml')
	
	product_attribute_model.insert_product_attribute('xyz','color','orange')
	product_attribute_model.insert_product_attribute('xyz','kg','2')
	product_attribute_model.insert_product_attribute('xyz','ml','200')

	
def initialize_database():
	clear_database()
	create_tables()
	populate_tables()
	
def drop_database():
	db_adapter.execute(drop_db);
	
	
	