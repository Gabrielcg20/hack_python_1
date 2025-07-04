"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    
    result = result.replace('o', '0') # se puede usar de esta forma para reemplazar cada letra de forma individual
    result = result.replace('i', '1')
    result = result.replace('a', '@')

    # result = result.replace('0', '0').replace('i', '1').replace('o', '0').replace('a', '@') // tambien esta una forma mas directa, pero podria ser mas confusa

    return result

print(fn_hack_5())
