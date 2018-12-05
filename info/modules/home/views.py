from flask import current_app

from info.modules.home import home_blue




@home_blue.route('/')
def index():
    current_app.logger.error("出现的错误")

    return 'index is show'
