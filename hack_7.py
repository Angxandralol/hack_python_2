"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    txt = []
    if (len(result) > 0) and (result[0] != 0): 
        for i in range(1, len(result) + 1):
            if i % 2 == 0: txt.append(i)
            else: txt.append(str(i))
    else: txt.append(0)
    return txt