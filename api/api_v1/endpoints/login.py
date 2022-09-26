# -*- coding: utf-8 -*-

#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: tlapapi
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

import schemas
from typing import Any
from utils.log import log as log

router = APIRouter()

@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    log.debug('Login with data [username=%s,password=%s]' % (form_data.username, form_data.password))

    return {
        "access_token": f"newaccess_tokenfor_{form_data.username}",
        "token_type": "bearer",
    }