import pandas as pd

def excel_detail(path):
    # 读取Excel表格
    df = pd.read_excel(path)
    # 获取detail列的所有数据，将其转换成字符串列表
    details = df['detail'].tolist()
    details = [str(detail) for detail in details]

    # 使用join()函数将所有detail列的数据拼接成一个字符串
    details_str = ''.join(details)

    # 输出拼接后的字符串
    print(details_str)
    return details_str

def excel_area(path):
    df = pd.read_excel(path)
    areas = df['area'].tolist()
    areas = [str(area) for area in areas]
    # print("区有:", areas)
    return areas

def excel_salary(path):
    df = pd.read_excel(path)
    salaries = df['avg_salary'].tolist()
    salaries = [int(salary) for salary in salaries]
    # print("工资有:", salaries)
    return salaries
