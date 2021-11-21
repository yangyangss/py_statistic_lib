import matplotlib.pyplot as plt
import random
from collections import Counter

def test_scatter_plot(x, y):
    plt.scatter(x, y)
    plt.show()

def test_line_plot(x, times):
    plt.plot([i for i in range(times)], x)
    plt.show()

def test_bar_plot(x, y):
    plt.bar(x, y)
    plt.show()

def test_histogram(_x, _rwidth, _bins, _density):
    #print(type(_bins))
    #plt.hist(_x, 0.8, 5, True)
    plt.hist(data, rwidth=_rwidth, bins=_bins, density=_density)
    plt.show()

if __name__ == '__main__':
    # scatter plot
    random.seed(666)
    x = [random.randint(0, 100) for _ in range(100)]
    y = [random.randint(0, 100) for _ in range(100)]
    # test_scatter_plot(x, y)
    #test_line_plot(x, 100)


    #条形图 - 条形图是用来为分类变量服务的
    data = [3, 3, 4, 1, 5, 4, 2, 1, 5, 4, 4, 4, 5, 3, 2, 1, 4, 5, 5]
    counter = Counter(data)
    x = [point[0] for point in counter.most_common()]
    y = [point[1] for point in counter.most_common()]
    #test_bar_plot(x, y)


    # 直方图 是用来对数值变量服务的
    # 在直方图中，我们可以对X轴进行任意区间的分割, 然后得到的柱形的宽度和高度都会被改变。
    # 频率直方图 -
    data = [random.randint(1, 100) for _ in range(1000)]
    test_histogram(data, 0.8, 5, True)

