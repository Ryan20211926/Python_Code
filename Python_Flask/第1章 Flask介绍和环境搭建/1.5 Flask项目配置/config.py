# coding:utf-8
# @Time    : 2025/5/7 13:38
# @Author  : Ryan
# @FileName: config.py
"""
"""
# config.py
class Config:
    """基本配置类"""
    DEBUG = False
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'