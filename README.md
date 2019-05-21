# Trabalho-de-PPIOO

Discentes

Bruna Stefany Batista Marques - 103404
João Miguel de Souza Barros - 105415
Luiz Fellipe Machi Pereira - 103491



Avaliação comparativa de duas linguagens de programação

O objetivo deste trabalho é a avaliação comparativa de duas linguagens de programação.

O trabalho é em equipe de até três pessoas. O compartilhamento de informações entre as equipes é permitido e aconselhado, mas o compartilhamento de código não é permitido. Trabalhos que tenham porções significativas de código iguais, ou copiados da internet, serão anulados.
Descrição

A avaliação comparativa deve ser feita utilizando os seguintes critérios:

    Facilidade de leitura e escrita

    Confiabilidade

    Custo de execução

Algumas características que afetam estes critérios e devem ser considerados na avaliação são: simplicidade, expressividade, tipos de dados e verificação de tipos.

Para dar subsídios para a comparação um avaliador passo a passo de expressões aritméticas deve ser escrito em duas linguagens de programação, Rust e uma das seguintes linguagens: C, C++, Go, Java, Python, JavaScript ou TypeScript. As duas versão devem ter testes automatizados.

As expressões são constituídas de números inteiros, operadores de adição (+), subtração (-), multiplicação (*) e divisão (/) e parênteses (( e )) e seguem a precedência e associativa comumente usada na matemática.

O programa deve ler as expressões da entrada padrão. Cada linha da entrada representa um expressão. Para cada linha da entrada o programa deve dividi-la em tokens (números, operadores e abre e fecha parênteses) e construir uma árvore que representa a expressão (veja o algoritmo Shunting Yard). Em seguida, o programa deve exibir passo a passo a avaliação da expressão, executando sempre a expressão mais a esquerda (que pode ser avaliada). Por exemplo:

> (10 / 3 + 23) * (1 - 4)
(3 + 23) * (1 - 4)
26 * (1 - 4)
26 * -3
-78

Para ajudar na avaliação comparativa é sugerido escrever uma versão inicial (com os testes e o programa principal) apenas com as operações de adição e multiplicação. Cada versão inicial pode ser escrita por membros diferentes da equipe que depois completam a outra implementação.

A lista a seguir sugere algumas funções que podem ser implementadas nos programas:

    lexer: recebe uma string e devolve um arranjo de tokens. Exemplo

    "31  * (4 + 10)"   ->   [31, "*", "(", 4, "+", 10, ")"]

    parser: recebe uma lista de tokens e devolve uma árvore que representa a expressão. Exemplo

    [31, "*", "(", 4, "+", 10, ")"]      ->         *
                                                  /   \
                                                 31    +
                                                     /   \
                                                    4    10

    eval-step: recebe uma árvore que representa uma expressão e devolve uma árvore com um operador avaliado. Exemplo

         *                        *
       /   \                    /   \
      31    +        ->        31   14
          /   \
         4    10

    to-string: recebe uma árvore que representa um expressão e devolve uma string que representa a mesma expressão. Exemplo

         *
       /   \
      31    +        ->        "31 * (4 + 10)"
          /   \
         4    10

