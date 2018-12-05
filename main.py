
from flask_migrate import MigrateCommand
from flask_script import Manager

from info import create_app

app = create_app("dev")

# 创建脚本启动管理器
mgr = Manager(app)
# 生成迁移命令
mgr.add_command("mc",MigrateCommand)


if __name__ == '__main__':
    mgr.run()