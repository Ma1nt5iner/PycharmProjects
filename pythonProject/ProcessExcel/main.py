import xlrd

table = xlrd.open_workbook("计算机2002名单.xlsx")

sheet = table.sheet_by_name("全班名单")

data = sheet.col_values(1)[1:]

user_data = sheet.col_values(2)

for i in data:
    if i not in user_data:
        print(f"{i}")
