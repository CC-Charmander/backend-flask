from . import main
#from .services import create_user_service, get_user_service
from ..service.test import test
from ..service.getSnacks import getSnacks

@main.route('/test')
def hello():
    aaa = test()
    return aaa

@main.route('/getSnacks')
def good():
    text = getSnacks()
    return text