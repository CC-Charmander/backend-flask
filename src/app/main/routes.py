from . import main
from flask import request
from ..service.getSnacks import getSnacks
from ..service.createPrompt import createSnackPrompt

import os
from dotenv import load_dotenv

load_dotenv()


@main.route('/test')
def test():
    return createSnackPrompt("カシスリキュール")

@main.route('/snack', methods=["GET"])
def getSnack():
    return getSnacks(["ジン"])