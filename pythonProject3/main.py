from Answer import Answer
from Product import Product
from SuffixExpression import SuffixExpression
import argparse
from BinaryTree import BinaryTree
from line_profiler import LineProfiler

import os


def main():
    parser = argparse.ArgumentParser(description="小学四则运算自动生成器")
    parser.add_argument('-n', '-na', type=int, help='控制生成题目的个数')
    parser.add_argument('-r', '-ra', type=str, help='题目中数值（自然数、真分数和真分数分母）的范围')
    parser.add_argument('-e', '-ea', type=str, default=" ", help='题目文件')
    parser.add_argument('-a', '-aa', type=str, default=" ", help='答案文件')
    args = parser.parse_args()
    n = int(args.n)
    r = int(args.r)
    e = args.e
    e = e.strip()
    a = args.a
    a = a.strip()
    product = Product(r, n)
    questions = product.problemArray
    # 存储生成的表达式，存进 ： “Exercises.txt”
    answer = Answer()
    answer.expression_result(questions)  # 生成题目的答案、

    if os.path.exists(e) and os.path.exists(a):
        print("核对答案")
        answer.check_answer(e, a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 性能测试
    p = LineProfiler()
    p.add_function(Answer.expression_result)
    p.add_function(Answer.check_answer)
    p.add_function(Product.__init__)
    p.add_function(Product.creQuestion)
    p.add_function(Product.generateOperation)
    p.add_function(Product.generateParentheses)
    p.add_function(Product.getOperNum)
    p.add_function(Product.DecToStr)
    p.add_function(Product.getRangeDec)
    p.add_function(Product.stacdardDec)
    p.add_function(Product.getFactorList)
    p.add_function(Product.getRandomNum)
    p.add_function(Product.getOperSymbol)
    p.add_function(Product.normalizeExpression)
    p.add_function(Product.isRepeat)
    p.add_function(Product.calculate)
    p.add_function(BinaryTree.generateBinaryTree)
    p.add_function(BinaryTree.treeIsSame)
    p.add_function(SuffixExpression.toSuffix)
    p.add_function(SuffixExpression.suffixToValue)
    p.add_function(SuffixExpression.cal)
    p_wrap = p(main)
    p_wrap()
    p.print_stats()  # 控制台打印相关信息
    p.dump_stats('saveName.lprof')  # 当前项目根目录下保存文件
