# 导入需要的库
import operator
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud_generater(txt1, txt2):
    # 读取文本文件并过滤停用词
    with open(txt1, 'r', encoding='utf-8') as f:
        text = f.read()
    with open(txt2, 'r', encoding='utf-8') as f:
        stopwords = set([line.strip() for line in f])  # 从文本文件中读取停用词
    words = [word for word in jieba.cut(text) if word not in stopwords]
    filtered_text = ' '.join(words)  # 拼接过滤后的文本
    # 生成词云图
    wc = WordCloud(background_color='white', font_path='msyh.ttc', width=800, height=600).generate(filtered_text)
    plt.imshow(wc)
    plt.axis('off')
    # plt.show()
    return filtered_text


def frequence_generater(txt1, txt2):
    words = []
    words = wordcloud_generater(txt1, txt2).split(" ")
    print("去重前的个数:" + str(len(words)))
    # 去重
    word_set = set(words)
    # 去重后的列表
    word_list = list(word_set)
    print("去重后的个数:" + str(len(word_list)))

    # 初始化频率表
    freq = []
    for i in range(len(word_list)):
        freq.append(0)

    # 计算词频
    for word in words:
        temp = word_list.index(word)
        freq[temp] += 1
    print("求和:" + str(sum(freq)))

    # 求取字典
    word_dict = dict(zip(word_list, freq))
    # print(word_dict)
    if "\n" in word_dict:
        word_dict.pop("\n", None)
    elif '' in word_dict:
        word_dict.pop('', None)
    elif "◆" in word_dict:
        word_dict.pop("◆", None)

    word_dict_sort = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    # print("字典如下:", word_dict_sort)
    # print(word_dict_sort[])
    return word_dict_sort


if __name__ == "__main__":
    frequence_generater("datas/example.txt", "datas/stopwords.txt")
