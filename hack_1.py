"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""

def fn_hack_1(s):
    result = s
    txt = ''
    i = 1
    for letter in result:
        if i == 3: 
            middle_letter = txt[-1].upper()
            txt = txt[:-1] + middle_letter
            i = 1
        else: i += 1
        txt += letter
    return txt