"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    len_result = len(result)
    txt = []
    if len_result % 2 == 0:
        for i in range(1, len_result + 1): txt.append(str(i))
    else:
        i = 1
        for letter in result: 
            txt.append(letter + '-' + str(i))
            i += 1
    txt.reverse()
    return txt