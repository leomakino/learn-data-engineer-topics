def foo(x):
    x[0] = 99
    # return x optional here


def bar(x):
    return x+90


def store_lower(_dict, _string):
    """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

    Args:
      _dict (dict): The dictionary to update.
      _string (str): The string to add.
    """
    orig_string = _string  # orig_string = Hello
    _string = _string.lower()  # _string = hello
    _dict[orig_string] = _string  # {'Hello' :  'hello'}


mylist = [*range(3)]
print("mylist: ", mylist)
foo(mylist)
print("Foo:", mylist)


my_var = 3
result = bar(my_var)
print("bar:", result)


d = {}
s = 'Hello'

store_lower(d, s)
print("Dic: {}, string: {}".format(d, s))
