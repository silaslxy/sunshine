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
    from src.ping import ping_bp
    from src.item import model_a_bp
    from src.user import model_b_bp
    app.register_blueprint(ping_bp, url_prefix="/ping")
    app.register_blueprint(model_a_bp, url_prefix="/item")
    app.register_blueprint(model_b_bp, url_prefix="/user")


def create_app():
    app = Flask(__name__)
    # 注册蓝图
    register_bp(app)
    app.debug = True
    return app


# 创建获取app对象
app = create_app()

if __name__ == '__main__':
    # load_dotenv
    app.run(host="0.0.0.0", port=9000)
