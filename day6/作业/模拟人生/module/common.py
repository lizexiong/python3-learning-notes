


from conf import setting


###根据等级分颜色显示###
def show_message(msg, msgtype):
    """
    对print函数进行封装，根据不同类型显示不同颜色
    :param msg:  显示的消息体
    :param msgtype:  消息类型
    :return: 返回格式化过的内容
    """

    if msgtype == "INFO":
        show_msg = "\033[1;34m{0}\033[0m\n".format(msg)
    elif msgtype == "INFORMATION":
        show_msg = "\033[1;32m{0}\033[0m\n".format(msg)
    elif msgtype == "NOTICE":
        show_msg = "\033[1;33m{0}\033[0m\n".format(msg)
    elif msgtype == "ERROR":
        show_msg = "\033[1;31m{0}\033[0m\n".format(msg)
    else:
        show_msg = "{0}\n".format(msg)
    print(show_msg)


def write_file(content,levelname,file_name):
    """
    将程序执行过程上中的异常信息记录到指定日志文件
    :param content: 日志信息
    :param levelname:日志级别
    :return: 无返回，写入文件 game.log
    """
    import logging
    ###自定义日志的格式和等级###
    logging.basicConfig(level=logging.INFO,
                encoding = "UTF-8",
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                filename = file_name,
                filemode='a+')
    if levelname == 'debug':
        logging.debug(content)
    elif levelname == 'info':
        logging.info(content)
    elif levelname == 'warning':
        logging.warning(content)
    elif levelname == 'error':
        logging.error(content)
    elif levelname == 'critical':
        logging.critical(content)
    else:
        show_message('输入错误',"ERROR")