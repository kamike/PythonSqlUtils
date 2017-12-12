#!/usr/bin/env python
# -*- coding:utf8 -*-
from FileBean import FileBean
from SQLUtils import SQLUtils

utils = SQLUtils()
fileBean = FileBean("http://baiodu.com","fileName",'a/dwaw','100',"md5111",'100','300',"baidu")


utils.addTableFile(fileBean)
utils.closedAll()
