from flask import Flask
from .modules.price.controller import api as priceNameSpace

from flask_restx import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='House Price Predict',
    version='1.0',
    description='Flask RESTApi for House Price Predict',
)

api.add_namespace(priceNameSpace, path='/price')

def createApp(config_name: str) -> Flask:
    app = Flask(__name__)
    return app