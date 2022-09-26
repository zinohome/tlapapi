#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: tlapapi

from typing import Any

from fastapi import APIRouter, Depends

from test.awxrestcall import AWXCall
from utils.log import log as log
import schemas

router = APIRouter()

@router.get('/get-all-hosts', status_code=201)
def test_get(
) -> Any:
    awxcall = AWXCall()
    return awxcall.getallhosts()