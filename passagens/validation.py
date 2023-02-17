def identicos(parametro_01, parametro_02):
    """Verifica se os valores são iguais"""
    return parametro_01 == parametro_02
  
  

def check_caracter(input):
    """Verifica se existe digitos númericos no input"""
    return any(char.isdigit() for char in input)
       

def maior(parametro_01, paramentro_02):
    """Verifica se o segundo valor é maior que o primeiro"""
    return paramentro_02 < parametro_01

