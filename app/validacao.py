import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF (Cadastro de Pessoas Físicas) brasileiro.
    
    :param cpf: CPF como string (somente números ou no formato xxx.xxx.xxx-xx).
    :return: True se o CPF for válido, False caso contrário.
    """
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos e não é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
       
    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    
    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])