#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 18:10
# @Author  : lipeijing
# @Email   : lipeijing@jd.com

import os
import json
from pprint import pprint
# import subprocess
def isNumber(item):
    try:
        float(item)
        return True
    except Exception as e:
        return False


def list_dic(dic):
    for name, value in dic.items():
        if isinstance(value, dict):
            list_dic(value)
        else:
            if isNumber(value):
                print(name + ":", value)
            else:
                print(name + ": \"" + value + "\"")

with open("Json") as file:
    output = file.readlines()[0]
    result = json.loads(output)
    list_dic(result)