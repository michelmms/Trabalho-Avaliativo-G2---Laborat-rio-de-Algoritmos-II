# Trabalho-Avaliativo-G2---Laboratorio-de-Algoritmos-II

O código implementa um modelo similar ao jogo "Termo" em Python, com foco no modo simplificado. Abaixo, está explicada a arquitetura do sistema, suas funcionalidades e como o jogo funciona:

# Arquitetura do Sistema:
O sistema é composto por um conjunto de funções que trabalham juntas para proporcionar uma experiência de jogo interativa. As principais funções incluem:
01. carregar_palavras: Lê um arquivo chamado "palavras.txt" contendo uma lista de palavras de 5 letras e retorna essas palavras em uma lista.
02. salvar_palavras_utilizadas: Recebe uma lista de palavras já utilizadas durante os jogos e as salva em um arquivo chamado "palavras_utilizadas.txt".
03. carregar_palavras_utilizadas: Lê o arquivo "palavras_utilizadas.txt" para obter a lista de palavras já utilizadas nos jogos anteriores.
04. escolher_palavra: Seleciona uma palavra aleatória das palavras disponíveis, evitando repetições utilizando as palavras já utilizadas. Mantém um histórico das palavras utilizadas.
05. validar_palavra: Verifica se uma palavra possui exatamente 5 letras e consiste apenas em caracteres alfabéticos.
06. comparar_palavras: Compara duas palavras (a tentativa do usuário e a palavra secreta) e destaca as letras corretas na posição exata em verde, as letras corretas, mas na posição errada, em amarelo, e as letras ausentes na palavra com branco.
07. jogar_modo_simplificado: Implementa o modo simplificado do jogo. O jogador tem 5 tentativas para adivinhar a palavra secreta. Após cada tentativa, o sistema fornece feedback destacando as letras corretas e incorretas.

# Funcionalidades do Sistema:
01. Escolha Aleatória de Palavras: O sistema escolhe aleatoriamente uma palavra de 5 letras para o jogador adivinhar.
02. Registro de Palavras Utilizadas: O sistema mantém um histórico das palavras utilizadas para garantir que não sejam repetidas durante o jogo.
03. Validação de Entrada do Usuário: Garante que as tentativas do usuário sejam palavras válidas de exatamente 5 letras, sem caracteres especiais.
04. Feedback Interativo: Após cada tentativa, o sistema fornece feedback visual destacando as letras corretas e incorretas na palavra.

# Funcionamento do Jogo:
01. O jogador inicia o jogo no modo simplificado.
02. Uma palavra de 5 letras é escolhida aleatoriamente pelo sistema.
03. O jogador tem até 5 tentativas para adivinhar a palavra.
04. Após cada tentativa, o sistema fornece feedback destacando as letras corretas na posição exata, as letras corretas em posição errada e as letras ausentes.
05. O jogo termina quando o jogador acerta a palavra ou atinge o limite de tentativas.
06. A palavra secreta é revelada no final do jogo.
