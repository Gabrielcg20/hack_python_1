"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result_mayuscula = result.upper() # primer paso fue como el hack_1, pasar todo a mayuscula.
    result_modificado = result_mayuscula.replace('O', '0').replace('I', '1').replace('A', '@') #segundo paso, hacer el reemplazo como el hack_5
    result_final = list(result_modificado) # convertir la cadena en una lista

    return result_final  

print(fn_hack_10())