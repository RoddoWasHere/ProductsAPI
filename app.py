from flask import Flask, request, jsonify, Response

from controllers.productsController import ProductsController
from utilities.setup_database import initialize_database, drop_database

products_controller = ProductsController()

app = Flask(__name__)
	
@app.route('/') 
def index():
	with open('views/index.html','r') as f:
		index_html = f.read()
		return index_html

@app.route('/products', methods=['GET'])
def get_products():
	products = products_controller.get_products()
	return jsonify(products)

@app.route('/products', methods=['POST'])
def add_products():
	products_controller.add_products(request.json)
	return jsonify(request.json)
	
#Setup routes
@app.route('/configure', methods=['GET'])
def configure_route():
	with open('views/configure.html','r') as f:
		index_html = f.read()
		return index_html	
		
@app.route('/initialize_database', methods=['GET'])
def initialize_database_route():
	initialize_database()
	
	products = products_controller.get_products()# test
	return "database created and populated successfully"
	
@app.route('/drop_database', methods=['GET'])
def drop_database_route():
	drop_database()
	return "database dropped successfully";
	
#JavaScript scripts route
@app.route('/js/<filename>.js', methods=['GET'])
def get_angular_lib(filename):
	with open('views/js/%s.js' % filename ,'r') as f:
		content = f.read()	
		return Response(content, headers={'content-type': 'text/javascript'})

#Design Doc		
@app.route('/design', methods=['GET'])
def design_route():
	with open('views/design.html','r') as f:
		index_html = f.read()
		return index_html	
	
	
	