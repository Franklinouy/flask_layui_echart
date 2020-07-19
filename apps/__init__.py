from flask import Flask, render_template
from flask_cors import CORS

from apps.modules.auth import auth_bp

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(auth_bp)


@app.route('/')
def login():
    # return 'hello world'
    print('render_template')
    return render_template('index.html')
