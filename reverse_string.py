def reverse_string(value):
    rev = ""
    for char in value:
        rev  =  char + rev
    return rev