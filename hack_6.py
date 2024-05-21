"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    result = s
    txt = []
    if len(result) > 0: 
        for i in range(1, len(result) + 1):
            if i % 2 == 0: txt.append("-")
            else: txt.append(str(i))
    else: txt.append("0")
    return txt