def transforma_base(questoes):
    base_agrupada = {}
    for questao in questoes:
        nivel = questao['nivel']
        if nivel not in base_agrupada:
            base_agrupada[nivel] = []
        base_agrupada[nivel].append(questao)
    return base_agrupada

def valida_questao(questao):
    resultado={}
    chaves_esperadas=['titulo', 'nivel', 'opcoes', 'correta']

    for chave in chaves_esperadas:
        if chave not in questao:
            resultado[chave]='nao_encontrado'

    if len(questao)!=4:
        resultado['outro']='numero_chaves_invalido'

    if 'titulo' in questao:
        if not questao['titulo'].strip():
            resultado['titulo']='vazio'

    if 'nivel' in questao:
        if questao['nivel'] not in ['facil', 'medio', 'dificil']:
            resultado['nivel']='valor_errado'

    if 'opcoes' in questao:
        opcoes=questao['opcoes']

        if len(opcoes)!= 4:
            resultado['opcoes']= 'tamanho_invalido'
        else:
            if 'A' not in opcoes or 'B' not in opcoes or 'C' not in opcoes or 'D' not in opcoes:
                resultado['opcoes']= 'chave_invalida_ou_nao_encontrada'
            else:
                vazias = {}
                for letra in ['A', 'B', 'C', 'D']:
                    if not opcoes[letra].strip():
                        vazias[letra] = 'vazia'
                if vazias:
                    resultado['opcoes']= vazias

    
    if 'correta' in questao:
        if questao['correta'] not in ['A', 'B', 'C', 'D']:
            resultado['correta']= 'valor_errado'

    return resultado

def valida_questao(questao):
    resultado={}
    chaves_esperadas=['titulo', 'nivel', 'opcoes', 'correta']

    for chave in chaves_esperadas:
        if chave not in questao:
            resultado[chave]='nao_encontrado'

    if len(questao)!=4:
        resultado['outro']='numero_chaves_invalido'

    if 'titulo' in questao:
        if not questao['titulo'].strip():
            resultado['titulo']='vazio'

    if 'nivel' in questao:
        if questao['nivel'] not in ['facil', 'medio', 'dificil']:
            resultado['nivel']='valor_errado'

    if 'opcoes' in questao:
        opcoes=questao['opcoes']

        if len(opcoes)!= 4:
            resultado['opcoes']= 'tamanho_invalido'
        else:
            if 'A' not in opcoes or 'B' not in opcoes or 'C' not in opcoes or 'D' not in opcoes:
                resultado['opcoes']= 'chave_invalida_ou_nao_encontrada'
            else:
                vazias = {}
                for letra in ['A', 'B', 'C', 'D']:
                    if not opcoes[letra].strip():
                        vazias[letra] = 'vazia'
                if vazias:
                    resultado['opcoes']= vazias

    
    if 'correta' in questao:
        if questao['correta'] not in ['A', 'B', 'C', 'D']:
            resultado['correta']= 'valor_errado'

    return resultado
    
def valida_questoes(questoes):
    resultado = []
    for questao in questoes:
        resultado.append(valida_questao(questao))
    return resultado

import random

def sorteia_questao(questoes, nivel):
    lista_questoes = questoes[nivel]
    indice_sorteado = random.randint(0, len(lista_questoes) - 1)
    return lista_questoes[indice_sorteado]

import random

def sorteia_questao(questoes, nivel):
    lista_questoes = questoes[nivel]
    indice_sorteado = random.randint(0, len(lista_questoes) - 1)
    return lista_questoes[indice_sorteado]


def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questao_sorteada = sorteia_questao(questoes, nivel)

    while questao_sorteada in questoes_sorteadas:
        questao_sorteada = sorteia_questao(questoes, nivel)

    questoes_sorteadas.append(questao_sorteada)
    return questao_sorteada

def questao_para_texto(questao, id):
    texto = "----------------------------------------\n"
    texto += "QUESTAO " + str(id) + "\n"
    texto += questao['titulo'] + "\n"
    texto += "RESPOSTAS:\n"
    texto += "A: " + questao['opcoes']['A'] + "\n"
    texto += "B: " + questao['opcoes']['B'] + "\n"
    texto += "C: " + questao['opcoes']['C'] + "\n"
    texto += "D: " + questao['opcoes']['D']
    return texto

import random
def gera_ajuda(questao):
    opcoes = questao['opcoes']
    correta = questao['correta']
    incorretas = []
    for letra in ['A', 'B', 'C', 'D']:
        if letra != correta:
            incorretas.append(opcoes[letra])
    quantidade = random.randint(1, 2)
    sorteadas = []
    while len(sorteadas) < quantidade:
        indice = random.randint(0, len(incorretas) - 1)
        opcao_sorteada = incorretas[indice]
        if opcao_sorteada not in sorteadas:
            sorteadas.append(opcao_sorteada)
    texto = "DICA:\n"
    texto += "Opções certamente erradas: "
    texto += sorteadas[0]
    if len(sorteadas) == 2:
        texto += " | " + sorteadas[1]
    return texto