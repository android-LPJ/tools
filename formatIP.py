#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 18:42
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
import sys
import re

def formatIp(iplist):
    ip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    newiplist = re.findall(ip, iplist)
    print(newiplist)
    return newiplist

if __name__ == '__main__':
    iplist = sys.argv[1]
    formatIp(iplist)