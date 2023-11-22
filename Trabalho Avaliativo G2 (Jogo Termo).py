# Nome do Aluno: Michel Matias Schmengler

"""
Termo

Desenvolva um sistema inspirado no jogo 'Termo' (https://term.ooo/), que desafia os jogadores a testarem suas habilidades ao tentar adivinhar
uma palavra aleatória escolhida pelo sistema. No modo simplificado, o usuário dispõe de 5 tentativas para desvendar a palavra secreta. A cada
tentativa, o sistema destaca as letras corretas na posição exata com verde, as letras corretas, mas na posição errada, com amarelo, e as
letras ausentes na palavra com branco. O jogador vence ao acertar a palavra. Além do modo simplificado, o jogo oferece outras modalidades
emocionantes. No modo dueto, o desafio é adivinhar duas palavras simultaneamente em 6 tentativas, mantendo a lógica do modo simplificado. Se
o jogador acertar uma das palavras, ela é retirada das tentativas subsequentes. Para vencer, é necessário acertar ambas as palavras. Já no
modo quarteto, o desafio amplia-se para quatro palavras, com 8 tentativas para acertar.

Requisitos Técnicos:

- Criação de um arquivo contendo todas as possibilidades de palavras a serem utilizadas no jogo.
- Elaboração de um arquivo com registro das palavras já utilizadas, garantindo que uma palavra não seja sorteada mais de uma vez.
- Utilização de listas, exceções, modularização e manipulação de arquivos no desenvolvimento do sistema.

Requisitos Funcionais:

- Caso o usuário não acerte a palavra durante um jogo, ela poderá aparecer futuramente.
- Implementação de funcionalidade que permita ao usuário redefinir as palavras já usadas no jogo.
- Garantia de que uma palavra não possa ser digitada duas vezes durante uma mesma partida.
- As palavras devem possuir obrigatoriamente 5 letras para serem válidas.
- As palavras sorteadas devem possuir 5 letras.
- O sistema não deve aceitar palavras com números ou espaços em branco.

Requisitos Não Funcionais:

- Desenvolvimento de uma interface amigável.
- O código deve ser disponibilizado no GitHub em um projeto próprio.
- O código deve ser acompanhado com um arquivo Readme.md contendo explicações em relação à arquitetura do sistema, suas funcionalidades e
como o jogo funciona.
- Junto ao repositório deve conter um vídeo de ambos os integrantes do grupo explicando o código-fonte e suas funcionalidades;

Requisitos de Avaliação:

- Atendimento dos Requisitos Funcionais e Não Funcionais;
- Qualidade do código;
- Autoria;
- Apresentação (em aula e vídeo);
- Interface;

A apresentação do trabalho será realizada no dia 22/11/2023.
"""

import random
import os

def carregar_palavras():
    with open("palavras.txt", "r") as arquivo:
        return [palavra.strip().lower() for palavra in arquivo.readlines()]

def salvar_palavras_utilizadas(palavras_utilizadas):
    with open("palavras_utilizadas.txt", "w") as arquivo:
        for palavra in palavras_utilizadas:
            arquivo.write(f"{palavra}\n")

def carregar_palavras_utilizadas():
    if os.path.exists("palavras_utilizadas.txt"):
        with open("palavras_utilizadas.txt", "r") as arquivo:
            return [palavra.strip().lower() for palavra in arquivo.readlines()]
    else:
        return []

def escolher_palavra(palavras, palavras_utilizadas):
    palavras_disponiveis = [palavra for palavra in palavras if palavra not in palavras_utilizadas]
    if not palavras_disponiveis:
        palavras_disponiveis = palavras
        palavras_utilizadas.clear()
    palavra_escolhida = random.choice(palavras_disponiveis)
    palavras_utilizadas.append(palavra_escolhida)
    salvar_palavras_utilizadas(palavras_utilizadas)
    return palavra_escolhida

def validar_palavra(palavra):
    return len(palavra) == 5 and palavra.isalpha()

def comparar_palavras(palavra_secreta, tentativa):
    resultado = []
    for i in range(5):
        if tentativa[i] == palavra_secreta[i]:
            resultado.append("\033[92m" + tentativa[i] + "\033[0m")  # Verde
        elif tentativa[i] in palavra_secreta:
            resultado.append("\033[93m" + tentativa[i] + "\033[0m")  # Amarelo
        else:
            resultado.append("\033[97m" + tentativa[i] + "\033[0m")  # Branco
    return resultado

def jogar_modo_simplificado():
    palavras = carregar_palavras()
    palavras_utilizadas = carregar_palavras_utilizadas()
    palavra_secreta = escolher_palavra(palavras, palavras_utilizadas)
    
    print("Bem-vindo ao jogo Termo - Modo Simplificado!")
    print("Tente adivinhar a palavra secreta de 5 letras.")
    
    for _ in range(5):
        tentativa = input("Digite sua tentativa: ").lower()
        
        if not validar_palavra(tentativa):
            print("Digite uma palavra válida com 5 letras.")
            continue
        
        if tentativa == palavra_secreta:
            print("Parabéns! Você acertou a palavra secreta.")
            break
        else:
            resultado = comparar_palavras(palavra_secreta, tentativa)
            print("Resultado:", " ".join(resultado))
    
    print(f"A palavra secreta era: {palavra_secreta.capitalize()}")

jogar_modo_simplificado()
