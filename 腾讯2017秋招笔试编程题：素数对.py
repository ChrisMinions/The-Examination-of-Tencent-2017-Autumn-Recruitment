'''
[编程题] 素数对
时间限制：1秒
空间限制：32768K
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)） 
输入描述:
输入包括一个整数n,(3 ≤ n < 1000)


输出描述:
输出对数

输入例子1:
10

输出例子1:
2
'''

'''
解题思路：简单
  本道题只要你找出所有素数对(也就是两个素数和等于输入值)，没有让你找出所有素数组合，所以难度大大降低。
  具体思路很简单，遍历从2开始到正整数一半的每一个整数，判断该数是否为素数，如果是，
  接着判断正整数减去该整数的差是否仍为素数，如果仍是，则累加器加1，最后输出累加器的值即可。
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

from math import sqrt

def is_pri_num(num):
    temp = int(sqrt(num))
    for j in range(2, temp+1):
        if num % j == 0:
            return False
    return True
n = int(input())
d = n // 2

count = 0
for i in range(2, d+1):
    if is_pri_num(i):
        if is_pri_num(n-i):
            count += 1
print(count)
