#!/usr/bin/env python
# -*- coding:utf8 -*-
import pymysql


class SQLUtils(object):
    def __init__(self):
        print("init=====sql=")
        dataBases = pymysql.connect("39.108.177.124", "wangtao", "PPYY0264", "ocr_data", charset='utf8')
        self.cursor = dataBases.cursor()
        self.tbl_file = "tbl_file"
        self.tbl_ocr = "tbl_ocr"

    def exeSelect(self, tbl, where):
        sql = "select * from " + tbl + " where " + where
        self.cursor.execute(where)

    def addTableFile(self, fileBean):
        sql = "inster into " + self.tbl_file + "(" + fileBean.__getParaStr__() + ") values(" + fileBean.__str__() + ")";
        print(sql)

    def closedAll(self):
        print("close-====")
        self.cursor.close()
