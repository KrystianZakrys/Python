# LEVEL 02
import re
# def method0(): need much work
#     result = ""
#     DATA = open("LEVEL02").read()
#     DATA = re.findall("<!--(.*?)-->", DATA, re.DOTALL)[-1]
#     numbers = {}
#     for x in DATA:
#         numbers[x] = numbers.get(x,0)+1
#     print(result)

def method1():
    DATA = open("LEVEL02").read()
    data = re.findall("<!--(.*?)-->", DATA, re.DOTALL)[-1]
    print("".join(re.findall("[A-Za-z]", data)))


method1()