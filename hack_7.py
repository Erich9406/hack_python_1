"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i = 5
    while i >= 0:
        result.append(i)
        i = i - 1
    return result  

resultado = fn_hack_7()
print(resultado)