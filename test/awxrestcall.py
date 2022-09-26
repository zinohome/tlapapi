#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: tlapapi
from utils.awxclient.awxclientapi import AWXClientApi
from utils.log import log as log


class AWXCall(object):
    def __init__(self):
        self._USERNAME = "admin"
        self._PASSWORD = "CEJ4xaOcUxKXIbnBlevMHDcBnTHmfdja"
        self._API_URL = "http://192.168.32.1:30080/api/v2"

    def getallhosts(self):
        client = AWXClientApi(api_url=self._API_URL, username=self._USERNAME, password=self._PASSWORD)
        return client.get_all_hosts()



if __name__ == '__main__':
    awxcall = AWXCall()
    log.debug(awxcall.getallhosts())

