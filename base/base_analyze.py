# coding=utf-8
import os

import yaml
import xlrd
import sys
import datetime
from xlutils.copy import copy
from docxtpl import DocxTemplate

file = "./data/办事通巡检" + datetime.datetime.now().strftime('%Y%m%d') + ".xlsx"
saveFile = "D:\\办事通巡检" + datetime.datetime.now().strftime('%Y%m%d') + ".xlsx"
print(file)
wordTemplate = "./data/办事通巡检日报模板.docx"
print(wordTemplate)
#saveWord = "./data/办事通巡检日报" + datetime.datetime.now().strftime('%Y%m%d') + ".docx"
saveWord = "D:\\办事通巡检日报"+ datetime.datetime.now().strftime('%Y%m%d') + ".docx"
print(saveWord)

def analyze_file(file_name, key):
    with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r", encoding='utf-8') as f:
        case_data = yaml.load(f, Loader=yaml.FullLoader)[key]

        data_list = list()
        for i in case_data.values():
            data_list.append(i)

        return data_list


def read_excel_sheet_row_data():
    li = []
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    print(wb.sheet_names())  # 打印所有表格名字
    for i in range(2):
        if i == 1:
            sheet_data = wb.sheet_by_name("事项类")  # 通过工作表名称获取某张表格
        else:
            sheet_data = wb.sheet_by_name("功能类")  # 通过工作表名称获取某张表格
        # 获取表格内从第三行到最后一行的数据
        for m in range(2, sheet_data.nrows):
            # l.append(sheet1.row_values(i))
            d = []
            for j in range(sheet_data.ncols):
                d = sheet_data.row_values(m)[1]
            li.append(d)
    return li


def save_excel_sheet(index, gongneng_list, gongneng, result, beizhu):
    """
    index:1表示功能类，2表示事项类
    gongneng_list:包含两个表所有功能的数组
    gongneng：功能名称
    result：正常或失败
    beizhu: 备注
    """
    wb = xlrd.open_workbook(filename=file)  # 选择需要复制的Excel
    xlsc = copy(wb)  # 进行Excel的复制
    shtc = xlsc.get_sheet(index - 1)  # 选取在Excel第一张表
    # 2表示第三行
    result_row_num = gongneng_list.index(gongneng) + 2
    print(result_row_num)
    if result_row_num > 42:
        result_row_num = result_row_num - 42
    print(result_row_num)
    # 结果
    shtc.write(result_row_num, 2, result)
    # 备注
    shtc.write(result_row_num, 3, beizhu)
    xlsc.save(saveFile)


def save_docx(content):
    # word模板
    doc = DocxTemplate(wordTemplate)
    # 待替换对象
    context = {'full_date': datetime.datetime.now().strftime('%Y年%m月%d日'), 'realname': "付聪聪", 'username': "15198938874",
               "month_date": datetime.datetime.now().strftime('%m月%d日'), "gongneng_total": "42","shixiang_total": "111"}
    doc.render(context)
    doc.save(saveWord)
