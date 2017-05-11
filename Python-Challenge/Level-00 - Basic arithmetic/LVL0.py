# http://www.pythonchallenge.com/pc/def/0.html
#
# LEVEL 00  2^38

def method0():
    return 2**38

def method1():
    twoPowerThirtyEight = 1
    for i in range(38):
        twoPowerThirtyEight *= 2
    return twoPowerThirtyEight

def method2():
    return pow(2,38)

# binary shift
def method3():
    return 1<<38

print(method0())
print(method1())
print(method2())
print(method3())
