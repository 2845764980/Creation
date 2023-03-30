from pyecharts import Bar
from wordcloud_generater import *
# from PIL import ImageFont
bar = Bar("First Graph")
req = []
freq = []
# 调函数获取字典
temp_dict = frequence_generater("../datas/example.txt", "../datas/stopwords.txt")
# 得到两个列表画图
for key, val in temp_dict:
    req.append(key)
    freq.append(val)
req.remove(req[0])
freq.remove(freq[0])
bar.add("要求", req, freq)
# 生成HTML文件
bar.render()

