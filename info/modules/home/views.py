from info.modules.home import home_blue




@home_blue.route('/')
def index():

    return 'index is show'
