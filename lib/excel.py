#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by aaron at 4/2/17

# System level
import imp
import sys

import xlrd
import xlwt
from xlutils.copy import copy

imp.reload(sys)


# Private

class Excel():
    def create_excel(self, path, filename):
        """Create excel"""
        if not path.endswith('/'):
            file = path + '/' + filename + '.xls'
        else:
            file = path + filename + '.xls'

        excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
        excel.add_sheet('Tmall', cell_overwrite_ok=False)
        excel.save(file)

    def write_excel(self, path, filename, contents):
        """Write excel"""
        if not path.endswith('/'):
            file = path + '/' + filename + '.xls'
        else:
            file = path + filename + '.xls'

        try:
            rd = xlrd.open_workbook(file)
            sheet = rd.sheets()[0]
            row = sheet.nrows
            wb = copy(rd)
            sheet = wb.get_sheet(0)
            col = 0
            for content in contents:
                sheet.write(row, col, content)
                col = col + 1
                wb.save(file)

        except IOError:
            self.create_excel(path, filename)
            self.write_excel(path, filename, contents)

    def write_info(self, infos, path, filename):
        if len(infos) >= 3:
            name = infos[0]
            comment = infos[1]
            url = infos[2]
            contents = (name, comment, url)
            self.write_excel(path, filename, contents)
        else:
            print('Write infos failed')