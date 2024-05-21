"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vocals = ['a', 'e', 'i', 'o', 'u']
    txt = ''
    for letter in result:
        if letter not in vocals: txt += letter
    return txt