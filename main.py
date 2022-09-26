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

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from fastapi_utils.timing import add_timing_middleware
from starlette.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

from api.api_v1.api import api_router
from core.settings import settings
from utils.log import log as log

app = FastAPI(debug=settings.API_DEBUG,
              title=settings.PROJECT_NAME,
              openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.SERVER_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.SERVER_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# fastapi_utils.timing profiling
add_timing_middleware(app, record=log.debug, prefix="app", exclude="untimed")

# include routers
app.include_router(api_router, prefix=settings.API_V1_STR)