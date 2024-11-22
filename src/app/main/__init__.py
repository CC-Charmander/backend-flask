from flask import Blueprint

# ルーティングを登録するためのインスタンス「bp」を作成
main = Blueprint('main', __name__)

from . import routes