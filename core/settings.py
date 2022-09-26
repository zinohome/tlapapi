#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: tlapapi

import os
import secrets
from pathlib import Path
from typing import List
from pydantic import AnyHttpUrl, BaseSettings, Field

BASE_DIR = Path(__file__).resolve().parent.parent

class AppSettings(BaseSettings):
    # 项目配置
    PROJECT_NAME: str = 'TLAPAPI'
    PROJECT_VERSION: str = '1.0911'

    #服务器配置
    SERVER_NAME: str = Field('tlapi-server', env='SERVER_NAME')
    SERVER_HOST: str = Field('0.0.0.0', env='SERVER_HOST')
    SERVER_PORT: str = Field('8880', env='SERVER_PORT')
    # SERVER_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    SERVER_CORS_ORIGINS: str = Field('[*]', env='SERVER_CORS_ORIGINS')

    # API配置
    API_V1_STR: str = "/api/v1"
    API_SECRET_KEY: str = secrets.token_urlsafe(32)
    API_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    API_DEBUG: bool = Field(True, env='API_DEBUG')
    API_EXCEPTIONN_DETAIL: bool = Field(True, env='API_EXCEPTIONN_DETAIL')
    API_LOG_LEVEL: str = Field('INFO', env='API_LOG_LEVEL')
    API_LOG_FILENAME: str = Field('logfilename', env='API_LOG_FILENAME')

    # 数据源配置
    MYSQL_SERVER: str = Field('localhost', env='MYSQL_SERVER')
    MYSQL_USER: str = Field('root', env='MYSQL_USER')
    MYSQL_PASSWORD: str = Field('password', env='MYSQL_PASSWORD')
    MYSQL_DB: str = Field('mydb', env='MYSQL_DB')
    SQLALCHEMY_DATABASE_URI: str = Field('mysql+pymysql://root:password@127.0.0.1:3306/mydb?charset=utf8mb4', env='SQLALCHEMY_DATABASE_URI')

    class Config:
        case_sensitive = True


class Settings(AppSettings):
    # 服务器配置
    SERVER_NAME: str = 'tlapi-server'
    SERVER_HOST: str = '0.0.0.0'
    SERVER_PORT: str = '8880'
    SERVER_CORS_ORIGINS: str = '[*]'

    # API配置
    API_V1_STR: str = "/api/v1"
    API_SECRET_KEY: str = secrets.token_urlsafe(32)
    API_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    API_DEBUG: bool = False
    API_EXCEPTIONN_DETAIL: bool = True
    API_LOG_LEVEL: str = 'INFO'
    API_LOG_FILENAME: str = 'tlapapi.log'

    # 数据源配置
    MYSQL_SERVER: str = 'localhost'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = 'passw0rd'
    MYSQL_DB: str = 'mydb'
    SQLALCHEMY_DATABASE_URI: str = 'mysql+pymysql://root:password@127.0.0.1:3306/mydb?charset=utf8mb4'

settings = Settings(_env_file=os.path.join(BASE_DIR, '.env'))


if __name__ == '__main__':
    print(settings.MYSQL_USER)
    print(settings.API_SECRET_KEY)
    print(settings.API_ACCESS_TOKEN_EXPIRE_MINUTES)
    print(settings.API_V1_STR)
    print(settings.SQLALCHEMY_DATABASE_URI)
    print(settings.API_LOG_FILENAME)