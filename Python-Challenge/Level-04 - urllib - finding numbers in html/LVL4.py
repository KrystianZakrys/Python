# LEVEL 04 # you must watch console for messages;
from urllib.request import urlopen
import re
def method0():
    uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    num = "12345"
    temp =""
    while(num):
        content = urlopen(uri % num).read().decode()
        temp = num
        num = "".join(re.findall("(\d+)",content))
        if not num:
            num = str(int(temp)/2)
        print(content)
method0()