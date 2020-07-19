import requests
from flask import jsonify, request

from . import auth_bp


@auth_bp.route('/')
def test():
    return 'Hello, auth!'


@auth_bp.route('/data/')
def get_data():
    page = request.args.get('page')
    limit = request.args.get('limit')

    data = requests.get(f'https://www.layui.com/demo/table/user/?page={page}&limit={limit}')
    # print(data)
    data = data.json()['data']
    data = {"code": 0, "msg": "请求成功", "count": 800, "data": data}
    print(data)
    return jsonify(data)
    # return jsonify(errno=200, errmsg="查询新闻列表数据成功", data=data)
