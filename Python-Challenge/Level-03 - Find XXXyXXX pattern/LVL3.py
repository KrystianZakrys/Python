# LEVEL 03 Find pattern XXXyXXX
import re

def method0():
    DATA = open("LEVEL03").read()
    # [^A-Z]+ atleast one different letter to begin our pattern for example iXXXyXXX same at the end XXXyXXXi
    # [A-Z]{3} 3 UPPERCASE characters
    # ([a-z]){1) "Selecting" only one lowercase letter
    print(re.findall("[^A-Z]+[A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]+",DATA))

method0()