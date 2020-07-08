# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:41
# @Desc:
# ----------------------------------
import logging

from flask import Flask

from common.log import stream_handler


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

    # 设置debug
    app.debug = True

    # 设置日志
    if not app.debug:
        app.logger.root.addHandler(stream_handler)
        app.logger.root.setLevel(logging.INFO)


    # 注册蓝图
    register_bp(app)

    return app


# 创建获取app对象
app = create_app()

# @app.errorhandler(BaseError)
# def custom_error_handler(e):
#     if e.level in [BaseError.LEVEL_WARN, BaseError.LEVEL_ERROR]:
#         if isinstance(e, OrmError):
#             app.logger.exception("%s %s" % (e.parent_error, e))
#         else:
#             app.logger.exception("错误信息: %s %s" % (e.extras, e))
#     response = jsonify(e.to_dict())
#     response.status_code = e.status_code
#     return response


if __name__ == "__main__":
    # load_dotenv
    app.run(host="0.0.0.0", port=9000)
