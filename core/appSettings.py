#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: tlapapi

from pydantic import BaseSettings, Field, validator


class AppSettings(BaseSettings):
    """项目配置"""
    APP_TITLE: str = 'tlsLearning'
    APP_VERSION: str = '1.0911'
    DEBUG: bool = Field(True, env='DEBUG')
    APP_EXCEPTIONN_DETAIL: bool = Field(True, env='APP_EXCEPTIONN_DETAIL')
    APP_LOG_LEVEL: str = Field('', env='APP_LOG_LEVEL')
    APP_LOG_FILENAME: str = Field('', env='APP_LOG_FILENAME')