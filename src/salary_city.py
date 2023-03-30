from excel_reader import *
from collections import Counter
import pandas as pd
import operator


def counter(array):
    return Counter(array)


path = "../datas/人力专员.xlsx"
# 获取地区列表
area = excel_area(path)
# 获取工资表
salary = excel_salary(path)
# 去重后区数据
unique_area_list = list(set(area))
sum_salary = []
# 初始换salary
for i in range(len(unique_area_list)):
    sum_salary.append(0)
# 合并为字典
unique_area_dict = dict(zip(unique_area_list, sum_salary))
count_dict = counter(area)
# 求取各个区工资总数
for i in range(len(area)):
    unique_area_dict[area[i]] += salary[i]

sort_unique_area_dict = dict(sorted(unique_area_dict.items(), key=operator.itemgetter(0)))
sort_count_dict = dict(sorted(count_dict.items(), key=operator.itemgetter(0)))

temp_sort_unique_area_dict_key = list(sort_unique_area_dict.keys())
temp_sort_unique_area_dict_val = list(sort_unique_area_dict.values())
temp_sort_count_dict = list(sort_count_dict.values())

for i in range(len(temp_sort_unique_area_dict_val)):
    temp_sort_unique_area_dict_val[i] = round(temp_sort_unique_area_dict_val[i] / temp_sort_count_dict[i], 2)

final_dict = dict(zip(temp_sort_unique_area_dict_key, temp_sort_unique_area_dict_val))
final_dict.pop('nan')
sort_final_dict = dict(sorted
                       (final_dict.items(), key=operator.itemgetter(1))
                       )
key = list(sort_final_dict.keys())
value = list(sort_final_dict.values())
# 利用pandas模块建立DataFrame类型，然后存入两个list
output_excel = pd.DataFrame()
output_excel["区"] = key
output_excel["工资"] = value
# 写入excel
output_excel.to_excel(excel_writer='salary_city.xlsx', sheet_name='sheet_1')
