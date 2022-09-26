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
from pydantic.networks import EmailStr

import schemas

router = APIRouter()

@router.get('/test-get', response_model=schemas.Msg, status_code=201)
def test_get(
) -> Any:
    return {"msg": "Word received"}