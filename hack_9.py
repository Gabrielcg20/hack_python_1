"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result_modificado = [] # se crea una nueva lista para la salida
    i = 0 # creamos un indice para indicar donde vamos a comenzar

    while i < len(result):
        result_modificado.append(result[i])
        result_modificado.append('@')
        i += 1

    return result_modificado  

print(fn_hack_9())