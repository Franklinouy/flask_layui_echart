from flask import Blueprint

#1.创建蓝图对象
auth_bp = Blueprint("auth", __name__, url_prefix='/auth')

#3.导入views文件
from .views import *