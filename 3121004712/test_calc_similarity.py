import unittest
import gensim

# 传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text1, text2):
    texts = [text1, text2]
    # 形成词典
    dictionary = gensim.corpora.Dictionary(texts)
    # 形成向量
    corpus = [dictionary.doc2bow(text) for text in texts]
    # print(corpus)
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

class TestStringMethods(unittest.TestCase):
    # 获取指定路径的文件内容
    def test_get_file_contents(self):
        similarity1 = calc_similarity(['今天', '是', '星期天', '天气', '晴', '今天', '晚上', '我要', '看', '电影'],
                                     ['今天', '是', '星期天', '天气', '晴', '今天', '晚上', '我要', '看', '电影'])
        self.assertEqual(similarity1, 0.9999999)

if __name__ == '__main__':
    unittest.main()