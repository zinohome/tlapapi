#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: tlapapi

import functools
from utils.awxclient.exceptions import LoginRequiredError

def require_auth(function):
    """
    A decorator that wraps the passed in function and raises exception
    if headers with token is missing
    """
    @functools.wraps(function)
    def wrapper(self, *args, **kwargs):
        if not self.headers:
            raise LoginRequiredError
        return function(self, *args, **kwargs)
    return wrapper