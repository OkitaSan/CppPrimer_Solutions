import xlrd as rd


def to_format(string: str):
    string.strip()
    to_remove = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"," ","计","软","一","二","三","四","五","六","七","八","九","十","-","——","—"]
    for _i in to_remove:
        string.replace(_i,'')
    return string

while True:
    open_file_index = input("请输入对应的文件路径:")
    rd_xlsx_1 = rd.open_workbook(open_file_index.replace("\\", "//"))
    table = rd_xlsx_1.sheet_by_index(0)
    stu_list = []
    row_num = table.nrows
    for i in range(1, row_num):
        __temp__ = table.cell_value(i, 1)
        stu_list.append(to_format(__temp__.strip()))
    rd_file_index = input("请输入已经加群的学生的名单的路径:")
    rd_xlsx_2 = rd.open_workbook(rd_file_index.replace("\\", "//"))
    table_2 = rd_xlsx_2.sheet_by_index(0)
    stu_is_in = []
    i = 0
    row_num_2 = table_2.nrows
    for i in range(0, row_num_2):
        __temp__ = table_2.cell_value(i, 0)
        __temp__ = to_format(__temp__.strip())
        stu_is_in.append(__temp__)
    stu_not_in = []
    for stu in stu_list:
        if stu not in stu_is_in:
            stu_not_in.append(stu)
    for stu in stu_not_in:
        print(stu)
    is_quit = input("如果要推出的话请按q，否则按任意键继续:")
    if is_quit == "q":
        break
    else:
        continue
