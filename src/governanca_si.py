def validar_volume_entrada(valor_str):
    """
    Função de Governança de TI (SI)
    Valida e sanitiza os dados de entrada antes de passar para o motor operacional.
    """
    try:
        volume = float(valor_str)
        if volume <= 0:
            return False, 0.0, "Erro: O volume informado deve ser maior que zero."
        return True, volume, "Volume valido."
    except ValueError:
        return False, 0.0, "Erro: Digite apenas valores numericos validos."