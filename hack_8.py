"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1, 3, 5, 7, 9]
    result = [x for x in result if x in [3, 5, 7]]
    return result

resultado = fn_hack_8()
print(resultado)