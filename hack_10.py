"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    new_list = []
    counter = 1
    for i in range(len(result)):
        new_list.append({str(counter): str(counter + 1)})
        counter += 2
    return new_list