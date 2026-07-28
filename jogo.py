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

def joga_uma_partida(nome, base):
    # Executa uma partida completa, do início até o fim (vitória, derrota ou parada voluntária)
 
    # Estado inicial da partida
    premio_atual = 0
    pulos = PULOS_INICIAIS
    ajudas = AJUDAS_INICIAIS
    questoes_sorteadas = []  # guarda todas as perguntas já sorteadas nesta partida, para não repetir
 
    # Flags que indicam como/se a partida terminou
    perdeu = False
    ganhou_tudo = False
    parou_por_vontade = False
 
    # Laço externo: representa as 9 rodadas da partida
    rodada = 0
    while rodada < len(PREMIOS):
        nivel = NIVEIS_POR_RODADA[rodada]
 
        # Passo 3 do enunciado: sorteia uma pergunta inédita do nível da rodada atual
        questao = sorteia_questao_inedita(base, nivel, questoes_sorteadas)
 
        # Controla se a ajuda já foi usada NESTA pergunta (reseta a cada nova pergunta)
        ajuda_usada_nesta_pergunta = False
 
        # Laço interno: mantém a mesma pergunta na tela até haver uma resposta A/B/C/D
        respondendo = True
        while respondendo:
            print()
            # Exibe a pergunta formatada (função do EP2)
            print(questao_para_texto(questao, rodada + 1))
            print()
            print("Prêmio atual: " + formata_dinheiro(premio_atual))
            print("Pulos restantes: " + str(pulos) + " | Ajudas restantes: " + str(ajudas))
 
            escolha = le_escolha_usuario()
 
            if escolha in ['A', 'B', 'C', 'D']:
                if escolha == questao['correta']:
                    # Passo 7: resposta correta -> aumenta o prêmio
                    premio_atual = PREMIOS[rodada]
                    print()
                    print("Parabéns, " + nome + "! Resposta correta!")
                    print("Prêmio atual: " + formata_dinheiro(premio_atual))
 
                    if premio_atual == PREMIOS[-1]:
                        # Atingiu o prêmio máximo (R$ 1.000.000): o jogo acaba automaticamente
                        ganhou_tudo = True
                        respondendo = False
                    else:
                        # Passo 9: pergunta se o jogador quer parar (levando o prêmio) ou continuar
                        resp = input("Deseja PARAR e levar o prêmio, ou CONTINUAR jogando? (parar/continuar): ").strip().lower()
                        if resp == 'parar':
                            parou_por_vontade = True
                        respondendo = False  # em qualquer caso, sai do loop interno
                else:
                    # Passo 8: resposta errada -> perde tudo e a partida acaba
                    print()
                    print("Que pena, " + nome + "! Resposta ERRADA!")
                    print("A resposta correta era: " + questao['correta'] + " - " + questao['opcoes'][questao['correta']])
                    premio_atual = 0
                    perdeu = True
                    respondendo = False
 
            elif escolha == 'ajuda':
                # Passo 5: pedido de ajuda
                if ajuda_usada_nesta_pergunta:
                    # Regra: não pode usar mais de uma ajuda na mesma pergunta
                    print("Você já usou uma ajuda nesta pergunta! Escolha outra opção.")
                elif ajudas <= 0:
                    # Regra: só há 2 ajudas no total da partida
                    print("Você não tem mais ajudas disponíveis!")
                else:
                    # Gera a dica (1 ou 2 opções erradas) usando a função do EP2
                    print(gera_ajuda(questao))
                    ajudas -= 1
                    ajuda_usada_nesta_pergunta = True
                # Não altera 'respondendo': a mesma pergunta continua sendo exibida
 
            elif escolha == 'pula':
                # Passo 6: pedido para pular a pergunta
                if pulos <= 0:
                    # Sem pulos disponíveis: informa e reexibe a MESMA pergunta
                    print("Você não tem mais pulos disponíveis!")
                else:
                    pulos -= 1
                    print("Pergunta pulada! Sorteando uma nova pergunta do mesmo nível...")
                    # Sorteia uma NOVA pergunta inédita do mesmo nível, substituindo a atual
                    questao = sorteia_questao_inedita(base, nivel, questoes_sorteadas)
                    # A nova pergunta ainda não teve ajuda usada nela
                    ajuda_usada_nesta_pergunta = False
                # Não altera 'respondendo': o loop interno continua com a pergunta (nova ou mesma)
 
        # Fora do loop interno: a pergunta da rodada foi respondida (certo ou errado)
        if perdeu or ganhou_tudo or parou_por_vontade:
            # Algum motivo de término da partida ocorreu: interrompe o laço de rodadas
            break
 
        # Resposta certa e o jogador optou por continuar: avança para a próxima rodada
        rodada += 1
 
    # Fim da partida: exibe a mensagem final de acordo com o motivo do término
    print()
    print("=" * 50)
    if ganhou_tudo:
        print("PARABÉNS, " + nome + "! Você ganhou o prêmio máximo de " + formata_dinheiro(PREMIOS[-1]) + "!")
    elif perdeu:
        print("Fim de jogo, " + nome + ". Você saiu sem nenhum prêmio.")
    else:
        print("Você decidiu parar, " + nome + ". Seu prêmio final foi de " + formata_dinheiro(premio_atual) + ".")
    print("=" * 50)