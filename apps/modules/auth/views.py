import os

import requests
from flask import jsonify, request

from config import BASE_DIR
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


@auth_bp.route('/upload_img/', methods=['POST'])
def upload_img():
    # 获得图片(images:<FileStorage: 'wa.jpg' ('image/jpeg')>)
    print(request.files)
    images = request.files.get('file')
    # house_id = request.form.get('house_id')
    # 得到upload的路径
    upload_dir = os.path.join(os.path.join(BASE_DIR, 'apps/static'), 'upload')
    # 得到上传图片要保存的路径
    # 'D:\\project\\houseproject\\static\\upload\\wa.jpg'
    url = os.path.join(upload_dir, images.filename)
    # 保存图片
    images.save(url)
    return jsonify({
        "code": 0
        , "msg": ""
        , "data": {
            "src": "http://cdn.layui.com/123.jpg"
        }
    })
