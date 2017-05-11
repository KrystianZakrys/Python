# LEVEL 01
def very_bad_method0(input):
    result = ""
    char_r = ""
    char_int = ""
    for x in input:
        x_ascii_value = ord(x)
        x_new_char = chr((x_ascii_value + 2)%125)
        if(ord(x_new_char) >= 122):
            x_new_char = 'a'
        result += x_new_char + " "
    return result

def method1(input):
    input = str(input)
    alphabet1 = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "cdefghijklmnopqrstuvwxyzab"
    string = str.maketrans(alphabet1,alphabet2)
    return input.translate(string)

C = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
C = "map"
print(very_bad_method0(C))
print(method1(C))
