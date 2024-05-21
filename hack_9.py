"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    if "foo" in result:
        result["foo"] = "Fooziman"
        result["Foo"] = result.pop("foo")
        result.pop("bar")
    return result