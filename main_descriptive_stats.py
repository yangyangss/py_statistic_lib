from collections import Counter

from playStats.descriptive_stats import frequency

if __name__ == '__main__':

    data = [2, 2, 2, 2, 1, 1, 1, 3, 3]

    # 测试频数
    # Test Count
    counter = Counter(data)
    print('most common value is {}'.format(counter.most_common()))

    #get the count value of most common number
    print('most common [0][1] value is {}'.format(counter.most_common()[0][1]))


    # 测试频率
    # Test frequency

    freq = frequency(data)
    print('frequency value is : {}'.format(freq))