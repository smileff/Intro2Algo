import random

def GetRandomIntegers(num = 100, minValue = 0, maxValue = 100):
    return [random.randint(minValue, maxValue) for i in range(num)]


