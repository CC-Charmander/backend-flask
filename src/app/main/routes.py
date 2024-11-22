from . import main
#from .services import create_user_service, get_user_service
from ..service.getSnacks import getSnacks

@main.route('/test')
def hello():
    return "<h1>Hello World!!</h1>"

@main.route('/snack', methods=["GET"])
def getSnack():
    return getSnacks()