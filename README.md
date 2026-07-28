# EP2-dessoft-dp-ferias-
# Jogo do Milhão

## Contexto

Este é um jogo de perguntas e respostas em terminal, inspirado no
"Show do Milhão". O jogador responde a uma sequência de 9 perguntas de
múltipla escolha, organizadas em ordem crescente de dificuldade (fácil,
médio e difícil). A cada resposta certa, o prêmio acumulado aumenta,
seguindo uma tabela pré-definida que vai de R$ 1.000 até R$ 1.000.000.

A tensão do jogo está em uma regra simples: **um único erro encerra a
partida e faz o jogador perder tudo o que já havia acumulado**. Por
isso, o jogador conta com duas ferramentas de apoio para tentar chegar
mais longe:

Pulos: trocam a pergunta atual por outra do mesmo nível, caso o
  jogador não saiba responder e prefira arriscar uma pergunta diferente.
Ajudas: eliminam 1 ou 2 alternativas que certamente estão erradas,
  facilitando a escolha entre as opções restantes.

O jogo termina de três formas possíveis: o jogador erra uma pergunta
(sai sem nada), o jogador acerta a última pergunta e ganha o milhão, ou
o jogador decide parar voluntariamente após um acerto, levando consigo
o prêmio já conquistado até aquele ponto.

## Como jogar

1. **Informe seu nome** quando solicitado — ele será usado nas mensagens
   do jogo.
2. **Leia o manual** exibido no início, que resume as regras e a tabela
   de prêmios.
3. A cada pergunta, você verá o título e as quatro opções (A, B, C, D).
   Digite uma das seguintes respostas:
   - `A`, `B`, `C` ou `D` — para responder a pergunta;
   - `pula` — para trocar a pergunta atual por outra do mesmo nível
     (você começa com 3 pulos por partida);
   - `ajuda` — para eliminar 1 ou 2 opções erradas (você começa com
     2 ajudas por partida, sendo no máximo 1 ajuda por pergunta).
4. **Se acertar**: seu prêmio sobe para o valor da tabela. Se ainda não
   chegou a R$ 1.000.000, o jogo pergunta se você quer **parar** (e
   garantir o prêmio) ou **continuar** para a próxima pergunta.
5. **Se errar**: o jogo mostra qual era a resposta certa, zera o
   prêmio, e a partida acaba ali.
6. **Ao acertar a última pergunta** (R$ 1.000.000), o jogo termina
   automaticamente com a vitória máxima.
7. Ao final de cada partida, você pode escolher jogar novamente.

### Tabela de prêmios

| Pergunta | Nível   | Prêmio       |
|----------|---------|--------------|
| 1        | Fácil   | R$ 1.000     |
| 2        | Fácil   | R$ 5.000     |
| 3        | Fácil   | R$ 10.000    |
| 4        | Médio   | R$ 30.000    |
| 5        | Médio   | R$ 50.000    |
| 6        | Médio   | R$ 100.000   |
| 7        | Difícil | R$ 300.000   |
| 8        | Difícil | R$ 500.000   |
| 9        | Difícil | R$ 1.000.000 |

## Como rodar no terminal

**Pré-requisitos**: ter o Python 3 instalado (não há nenhuma
dependência externa a instalar).

1. Coloque os arquivos `jogo.py`, `funcoes.py` e `perguntas.py` na
   mesma pasta.
2. Abra um terminal nessa pasta.
3. Execute:
   ```bash
   python3 jogo.py
   ```
   No Windows, se `python3` não for reconhecido, use:
   ```bash
   python jogo.py
   ```
4. Siga as instruções exibidas na tela e digite suas respostas quando
   solicitado.

Para encerrar o jogo a qualquer momento (antes do fim natural da
partida), basta fechar o terminal ou usar `Ctrl+C`.