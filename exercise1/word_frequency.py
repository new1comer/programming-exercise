import string
import re


def word_frequency(text):
    
    
    # 文本预处理 去掉可能存在的所有标点符号
    pattern = r'[^\w\s]'    # 正则匹配标点符号
    clean_text = re.sub(pattern, '', text)
    
    # 大小写统一
    lowercased_text = clean_text.lower()
    
    # 分词
    words = lowercased_text.split()
    
    # 创建词表 dict keys: 词语 value: 出现的次数
    frequency = {}
    
    # 计数
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

if __name__ == '__main__':
    text = "this is a test, this is only a test"
    print(word_frequency(text))
    