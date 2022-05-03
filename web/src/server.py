from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
import mysql.connector as mysql
from dotenv import load_dotenv
import os

def home_page(req):
    return FileResponse("./templates/home.html")

def product_page(req):
    return FileResponse("./templates/product.html")

def KVP_page(req):
    return FileResponse("./templates/KVP.html")

if __name__ == '__main__':
    with Configurator() as config:
         #create route called home
        config.add_route('home','/')

        #bind the view (defined bu index_page) to route named 'home'
        config.add_view(home_page, route_name='home')

        config.add_route('product','/')

        config.add_view(product_page, route_name='product')

        config.add_route('KVP','/')

        config.add_view(KVP_page,route_name='KVP')


        config.add_static_view(name='/',path='./public', cache_max_age=3600)

        config.add_static_view(name='/product',path='./templates', cache_max_age=3600)
        
        app = config.make_wsgi_app()
    
    server = make_server('0.0.0.0', 6000, app)
    print("server started!")
    server.serve_forever()