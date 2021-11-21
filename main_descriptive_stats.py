from collections import Counter

from playStats.descriptive_stats import frequency, mode, median, mean, rng, quartile, variance, std


# 测试众数
def test_mode(data):
    mode_elements, mode_count = mode(data)
    if mode_elements:
        print('mode elements is : {}'.format(mode_elements))
        print('mode count is : {}'.format(mode_count))
    else:
        print('Mode does not exist')

def test_frequency(data):
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

def test_median(data):
    print('median value is: {}'.format(median(data)))

def test_mean(data):
    print('mean value is: {}'.format(mean(data)))

def test_rng(data):
    print('range value is: {}'.format(rng(data)))

def test_quartile(data):
    print('quartile value is: {}'.format(quartile(data)))

def test_variance(data):
    print('variance value is: {}'.format(variance(data)))

def test_std(data):
    print('sqt value is: {}'.format(std(data)))


if __name__ == '__main__':
    # data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    # test_mode(data)

    data = [1,4,2,3]
    test_std(data)


    data = [1,4,2,3, 5]
    test_std(data)


    data = [1,4,2,3, 5, 99]
    test_std(data)