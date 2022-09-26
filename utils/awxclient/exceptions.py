#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: tlapapi

class AuthError(Exception):
    """
    Authentication error
    """
    pass

class UnauthorizedError(AuthError):
    """
    Unauthorized error
    """
    pass

class MissingParameterError(Exception):
    """
    Missing parameter error
    """
    pass

class ParameterError(Exception):
    """
    Parameter error
    """
    pass

class LoginRequiredError(Exception):
    """
    Authentication error
    """
    pass