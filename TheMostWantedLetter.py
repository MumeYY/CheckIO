# -*- coding: utf-8 -*- 
# 给你一个其中包含不同的英文字母和标点符号的文本，你要找到其中出现最多的字母，返回的字母必须是小写形式，
# 当检查最想要的字母时，不区分大小写，所以在你的搜索中 "A" == "a"。 请确保你不计算标点符号，数字和空格，只计算字母。
# 如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母。 例如 -- “one”包含“o”，“n”，“e”每个字母一次，因此我们选择“e”。
# 输入: 用于分析的文本.
# 输出: 最常见的字母的小写形式。
# 前提::
# 密码只包含ASCII码符号
# 0 < len(text) ≤ 105


# BestSolutions
import string
def checkio_best(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    # text.count为函数，返回指定char的数量
    return max(string.ascii_lowercase, key=text.count)


def checkio(text):
    d = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha() == True:
            if letter in d:
                d[letter] = d[letter] + 1
            else:
                d[letter] = 1
    result = 'a'
    maxCount = 0
    for i in range(0, 26):
        char = chr(i+ord('a'))
        # print(char + str(d.get(char, 0)))
        if d.get(char, 0) > maxCount:
            result = char
            maxCount = d.get(char, 0)
    return result

print(checkio_best('AAaooo!!!!'))