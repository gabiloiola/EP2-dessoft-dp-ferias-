# Importa funções do EP2 que o jogo utiliza
from funcoes import (
    transforma_base,
    valida_questoes,
    sorteia_questao_inedita,
    questao_para_texto,
    gera_ajuda,
)
# Importa o banco de perguntas (lista 'quest') do arquivo perguntas.py
from perguntas import quest
# Tabela de prêmios: índice 0 = pergunta 1 (R$1.000) ... índice 8 = pergunta 9 (R$1.000.000)
PREMIOS = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
 
# Define o nível de dificuldade de cada uma das 9 rodadas: 3 fáceis, 3 médias, 3 difíceis
NIVEIS_POR_RODADA = ['facil', 'facil', 'facil',
                      'medio', 'medio', 'medio',
                      'dificil', 'dificil', 'dificil']
 
# Quantidade inicial de pulos e ajudas que o jogador recebe no começo de cada partida
PULOS_INICIAIS = 3
AJUDAS_INICIAIS = 2
 
 
def formata_dinheiro(valor):
    # Formata um número inteiro como valor monetário em reais (ex: 1000000 -> "R$ 1.000.000")
    # format(valor, ',d') usa vírgula como separador de milhar; depois trocamos por ponto (padrão BR)
    return "R$ " + format(valor, ',d').replace(',', '.')
 
 
def exibe_manual():
    # Passo 1 do enunciado: exibe um pequeno manual explicando as regras do jogo
    print("=" * 50)
    print("BEM-VINDO AO JOGO DO MILHÃO!")
    print("=" * 50)
    print("Regras:")
    print("- Você responderá 9 perguntas, cada uma com 4 opções (A, B, C, D).")
    print("- A cada acerto, seu prêmio aumenta, seguindo a tabela:")
    # Monta a tabela de prêmios dinamicamente a partir da lista PREMIOS
    for i, valor in enumerate(PREMIOS):
        print("  " + str(i + 1) + "a pergunta: " + formata_dinheiro(valor))
    print("- Se errar uma pergunta, você perde tudo e sai sem nenhum prêmio!")
    print("- Após CADA acerto, você pode escolher parar e levar o prêmio atual.")
    print("- Você tem " + str(PULOS_INICIAIS) + " pulos: usados para trocar a pergunta atual por outra.")
    print("- Você tem " + str(AJUDAS_INICIAIS) + " ajudas: eliminam 1 ou 2 opções sabidamente erradas.")
    print("- Não é possível usar mais de uma ajuda na mesma pergunta.")
    print("- O jogo termina automaticamente ao atingir o prêmio de R$ 1.000.000.")
    print("=" * 50)
    print()

def valida_base_de_dados(lista_questoes):
    # Garante que a base de perguntas está consistente antes de começar o jogo
 
    # Usa a função do EP2 para validar cada questão da lista
    resultado_validacao = valida_questoes(lista_questoes)
 
    tem_erro = False
    for i in range(len(resultado_validacao)):
        # Se o dicionário de erros da questão i não estiver vazio, há um problema
        if resultado_validacao[i]:
            tem_erro = True
            print("Problema encontrado na questão de índice " + str(i) + ": " + str(resultado_validacao[i]))
 
    # Se qualquer questão tiver erro, a base é considerada inválida e o jogo não deve iniciar
    if tem_erro:
        return False
 
    # Agrupa as questões por nível para checar se há perguntas suficientes em cada um
    base = transforma_base(lista_questoes)
 
    # O jogo precisa de pelo menos 3 perguntas por nível (3 fáceis, 3 médias, 3 difíceis)
    for nivel in ['facil', 'medio', 'dificil']:
        if nivel not in base or len(base[nivel]) < 3:
            print("A base de perguntas não possui questões suficientes no nível '" + nivel + "'.")
            return False
 
    # Base validada com sucesso
    return True
 
 
def le_escolha_usuario():
    # Passo 4 do enunciado: lê e valida a escolha do jogador (A, B, C, D, pula ou ajuda)
    # Fica em loop até receber uma entrada válida
    while True:
        escolha = input("Sua resposta (A, B, C, D, pula ou ajuda): ").strip()
 
        # Normaliza a entrada para aceitar tanto maiúsculas quanto minúsculas
        escolha_maiuscula = escolha.upper()
        escolha_minuscula = escolha.lower()
 
        if escolha_maiuscula in ['A', 'B', 'C', 'D']:
            return escolha_maiuscula
        elif escolha_minuscula == 'pula':
            return 'pula'
        elif escolha_minuscula == 'ajuda':
            return 'ajuda'
        else:
            # Entrada inexistente/inválida: avisa e volta para o início do loop
            print("Opção inválida! Digite A, B, C, D, pula ou ajuda.")