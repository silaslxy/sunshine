# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:41
# @Desc:
# ----------------------------------

from flask import Flask


def register_bp(app: Flask):
    """
    注册蓝图
    """
    from src.model_a import model_a_bp
    app.register_blueprint(model_a_bp, url_prefix="/model_a")


def create_app():
    app = Flask(__name__)
    # 注册蓝图
    register_bp(app)
    return app


# 创建获取app对象
app = create_app()

if __name__ == '__main__':
    app.run()
