def transforma_base(questoes):
    base_agrupada = {}
    for questao in questoes:
        nivel = questao['nivel']
        if nivel not in base_agrupada:
            base_agrupada[nivel] = []
        base_agrupada[nivel].append(questao)
    return base_agrupada