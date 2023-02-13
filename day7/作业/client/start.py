

#导入配置的主要作用是导入环境变量
from conf import settings
from bin import client


if __name__ == "__main__":
    client.start()