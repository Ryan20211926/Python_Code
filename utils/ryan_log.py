# coding:utf-8
# @Time    : 2024/11/26 9:37
# @Author  : Ryan
# @FileName: ryan_log.py

from loguru import logger
from datetime import datetime
import os

def getRootPath(project):
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find(project) + len(project)]
    logger.info(f"项目的跟目录{rootPath}")
    return rootPath

class ApiAutoLog():
    '''
    利用loguru封装接口自动化项目日志记录器
    '''
    def __new__(cls, *args, **kwargs):
        log_name = datetime.now().strftime("%Y-%m-%d")    # 以时间命名日志文件，格式为"年-月-日"
        # base_path = os.path.dirname(os.path.dirname(__file__))
        base_path = getRootPath("Python_Code")
        file_path = f"{base_path}\logs\{log_name}.log"
        sink =os.path.join(base_path,file_path)
        # print(sink)
        # "../logs/{}.log".format(log_name) # 日志记录文件路径
        level = "DEBUG"  # 记录的最低日志级别为DEBUG
        encoding = "utf-8"  # 写入日志文件时编码格式为utf-8
        enqueue = True # 多线程多进程时保证线程安全
        rotation = "500MB" # 日志文件最大为500MB，超过则新建文件记录日志
        retention = "1 week"    # 日志保留时长为一星期，超时则清除
        logger.add(
            sink=sink, level=level, encoding=encoding,
            enqueue=enqueue, rotation=rotation, retention=retention
        )
        return logger
if __name__ == '__main__':
    # print(os.path.dirname(os.path.dirname(__file__)))
    log = ApiAutoLog()
    log.debug("这是一条debug日志信息")
    log.info("这是一条info日志信息")
    log.warning("这是一条warning日志信息")
    log.critical("这是一条critical日志信息")