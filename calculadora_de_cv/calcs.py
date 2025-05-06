
def calcular_valor_critico(dano_critico: float, taxa_critica: float) -> float:
    """
    Calcula o valor crítico com base no dano crítico e na taxa crítica.

    :param dano_critico: Dano crítico do artefato.
    :param taxa_critica: Taxa crítica do artefato.
    :return: Valor crítico calculado.
    """
    return dano_critico + (taxa_critica * 2)
