"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    
    return result[1:4]  # debemos indicar cuales son los valores a los que queremos llegar

print(fn_hack_8())