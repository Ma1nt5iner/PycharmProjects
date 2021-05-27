import os
import xlrd

# 对比所需文件夹路径
file_path = '------'
# 对比所需excel路径
excel_path = '------'

# 把文件夹内包含的文件的文件名返回一个列表
myList1 = os.listdir(file_path)
result_dir1_name = []
# for循环文件夹内的文件到file
for file in myList1:
    # 把文件后缀去掉在进行对比
    file_name = file.split(".")[0]
    # 去掉后缀后的文件名放入列表
    result_dir1_name.append(file_name)

# 读取表格里的内容
xls = xlrd.open_workbook(excel_path)
# 获取表格第二个索引的内容
sheet = xls.sheet_by_index(1)
# 返回表格第二列从第二行开始到最后的内容（返回列表）
excel_name = sheet.col_values(1)[1:]

result = []
# for循环表格内容到excel
for excel in excel_name:
    # if判断表格里的内容(excel)是否和文件名(result_dir1_name)不同(not in)
    if excel not in result_dir1_name:
        # 符合条件的放入result列表里
        result.append(excel)

print(result)