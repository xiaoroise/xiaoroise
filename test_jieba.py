import unittest
import jieba
import re

def filter(str):
    # 将读取到的文件内容先进行jieba分词，
    str = jieba.lcut(str)
    result = []
    # 把标点符号、转义符号等特殊符号过滤掉
    for tags in str:
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result

class TestStringMethods(unittest.TestCase):
    # 获取指定路径的文件内容
    def test_get_file_contents(self):
        self.assertEqual(filter("今天是星期天，天气晴，今天晚上我要去看电影"),['今天', '是', '星期天', '天气', '晴', '今天', '晚上', '我要', '去', '看', '电影'])

if __name__ == '__main__':
    unittest.main()