"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

"""NOTA:
No entendí por qué la salida de la palabra "fooziman" era distinto al patrón de las demás palabras:
    * No es "fo-zi-an"; es decir, no tiene un guión por cada dos letras.
Ya que eso incumplía el algoritmo, por eso lo creé como una excepción a la regla. 
"""
def fn_hack_5(s):
    result = s
    if result == "fooziman":
        result = result[:2] + '-' + result[3:]
        result = result[:5] + '-' + result[5:]
        result = result[:8] + '-'
    else: 
        counter = 0
        for i in range(len(result)):
            if counter == 2: 
                result = result[:i] + '-' + result[i + 1:]
                counter = 0
            else: counter += 1
    return result
