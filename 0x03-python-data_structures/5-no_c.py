def no_c(my_string):
    str = ""
    for ch in my_string:
        if ch != "c" and ch != "C":
            str = str + ch
    return str
