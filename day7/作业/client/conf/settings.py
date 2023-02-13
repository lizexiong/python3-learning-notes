





import os,sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)



# 文件下载保存路径
DOWNLOAD_FILE_PATH = os.path.join(BASE_DIR, "download")


# 日志文件存放路径
LOGS = os.path.join(BASE_DIR, "logs/ftpclient.log")
