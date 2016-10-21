=========================================
Capítulo 1: Abrindo e fechando o console
=========================================

A melhor forma de aprender a programar é usando o console de um interpretador em modo interativo. Dessa forma você pode digitar comandos linha por linha e observar a cada passo como o computador interpreta e executa esses comandos. Para fazer isso em Python, há duas maneiras:

..todo:: Jupyter

1. executar o interpretador em modo texto (clicando em "Python (command line)" no Windows, ou simplesmente ``python3`` no Linux ou no MacOS X)

2. usar o IDLE, que é um ambiente baseado em janelas.

Se você usa Windows, escolha o IDLE para começar a acompanhar esse tutorial. O IDLE também está disponível para a plataforma Linux (algumas distribuições colocam o IDLE em um pacote separado do pacote do Python).

Seja qual for o interpretador que você escolheu, ao executá-lo você verá uma mensagem com informações de *copyright* mais ou menos como essa::

    Python 2.5.1 (r251:54863, Oct  5 2007, 13:50:07)
    [GCC 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

O símbolo ``>>>`` exibido pelo interpretador é o que os americanos chamam de "prompt", que alguns traduzem por "aviso", mas nós vamos chamar de "deixa" (em teatro, o termo "prompt" é a deixa que indica ao ator a hora de dizer ou fazer algo; em computação, o "prompt" informa o usuário que o sistema está pronto para receber um novo comando).

Para sair do interpretador você pode fechar a janela do IDLE, ou teclar ``[CTRL]+[D]`` (no IDLE ou no interpretador em UNIX) ou ``[CTRL]+[Z]`` e então ``[ENTER]`` (no interpretador DOS).

Uma calculadora melhor
=======================

Vamos então aproveitar a deixa e escrever algo. Experimente escrever uma expressão aritmética bem simples, como ``2+2``::

    >>> 2+2
    4
    >>>

A resposta é reconfortante: para Python, ``2+2`` é igual a 4. Você pode experimentar outras expressões mais complexas, mas é bom saber que os quatro operadores básicos em Python (e em quase todas as linguagens modernas) são esses:

   * ``+`` adição
   * ``-`` subtração
   * ``*`` multiplicação
   * ``/`` divisão

Em Python, assim como na linguagem C, os números inteiros têm um tratamento especial. Isso fica evidente quando fazemos uma divisão::

    >>> 7/2
    3
    >>>


Em vez de 3,5, o resultado foi 3. Isso acontece sempre que todos os números de uma expressão são inteiros. Neste caso, Python imagina que se deseja um resultado inteiro também (esse comportamento estranho às vezes é conveniente em programação).

Se você quiser operar com números decimais, deve usar o ponto e não a vírgula como separador decimal::

    >>> 7.0/2
    3.5
    >>> 7/2.0
    3.5
    >>> 7/2.
    3.5
    >>>


Note que basta digitar um ponto após o número. O computador não consegue lidar com números do conjunto dos reais, mas apenas com uma aproximação chamada "número de ponto-flutuante" (porque o ponto decimal pode aperecer em qualquer posição do número). Ao lidar com ponto-flutuante, às vezes vemos resultados estranhos::

    >>> 2.4 * 2
    4.7999999999999998
    >>>

O resultado não deveria ser 4.8? Deveria, mas antes de ficar revoltado note que a diferença foi muito pequena. Acontece que o sistema de "ponto-flutuante" padrão IEEE-754 usado em quase todos os computadores atuais tem uma precisão limitada, e Python não esconde este fato de você, programador. O problema não está na conta, mas na própria representação interna do valor ``2.4``::

    >>> 2.4
    2.3999999999999999


Para exibir valores de ponto-flutuante para um usuário sem assustá-lo, use o comando ``print``::

    >>> print 2.4 * 2
    4.8
    >>>


Você pode digitar espaços entre os números e operadores para fazer uma expressão longa ficar mais legível. Veja esse exemplo::

    >>> 1 + 2 * 3
    7
    >>>

Note que o interpretador Python é mais esperto que uma calculadora comum. Ele sabe que a multiplicação deve ser efetuada antes da adição. Se você teclar a mesma expressão em uma calculadora qualquer obterá o resultado 9, que é incorreto. Em Python, se você realmente deseja efetuar a soma antes da multiplicação, precisa usar parênteses::

    >>> (1 + 2) * 3
    9
    >>>

Ao contrário do que você aprendeu na escola, aqui os símbolos [] e {} não servem para agrupar expressões dentro de outras expressões. Apenas parênteses são usados::

    >>> ( 9 - ( 1 + 2 ) ) / 3.0
    2.0
    >>> ( 9 - 1 + 2 ) / 3.0
    3.33333333333
    >>>

.. note::  Dica

  Se você escrever algo que o interpretador não reconhece, verá na tela uma mensagem de erro. Não crie o mau hábito de ignorar essas mensagens, mesmo que elas pareçam difíceis de entender num primeiro momento. A única vantagem de cometer erros é aprender com eles, e se a preguiça o impedir de ler as mensagens, seu aprendizado será bem mais lento.

.. admonition:: Como decifrar as mensagens de erro do Python

  A dura realidade é que um programador profissional passa boa parte de sua vida caçando erros, e por isso é fundamental saber extrair o máximo de informações das mensagens resultantes.

  A essa altura você talvez já tenha provocado um erro para ver o que acontece. Vamos fazer isso agora, e aprender a ler as mensagens resultantes. Pode parecer perda de tempo, mas é importantíssimo saber interpretar as mensagens de erro porque a melhor forma de aprender a programar é experimentando, e ao experimentar você certamente vai provocar muitos erros.

  Como exemplo, vamos digitar uma expressão aritmética sem sentido::

    >>> 7 + / 2
      File "<stdin>", line 1
        7 + / 2
            ^
    SyntaxError: invalid syntax
    >>>

  O interpretador indica o local de erro em vermelho no IDLE, ou com o sinal ^ no console. Nos dois casos a última linha contém as informações mais importantes: ``SyntaxError: invalid syntax``. A primeira parte, ``SyntaxError`` é o tipo do erro, e após o sinal de ``:`` vem a descrição: erro de sintaxe inválida.

  No console a primeira linha da mensagem de erro indica em a linha do seu código onde ocorreu o problema. No modo interativo essa informação pouco útil, mas quando fizermos programas extensos será muito bom saber exatamente em qual linha está a falha.
  Agora vamos provocar um outro tipo de erro::

    >>> 1.5/0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: float division
    >>>

  Novamente, a parte mais importante é a última linha, que nesse caso é bem fácil de entender: ``ZeroDivisionError: float division``, ou "erro de divisão por zero em divisão de ponto-flutuante".

Conversor de dólares
=====================

Digamos que você tem uma loja de discos importados, e precisa constantemente converter dólares em reais. O valor do dólar para venda em 20/05/1999 é de 1.686. Para converter US$9,95 e US$11,95 em reais você pode digitar::

    >>> 9.95 * 1.686
    16.775699999999997
    >>> 11.95 * 1.686
    20.147699999999997
    >>>

Mas há uma forma melhor: em vez de digitar o valor 1.686 o tempo todo, você pode armazenar esse valor na memória do computador, assim::

    >>> d = 1.686
    >>>

Note que o interpretador não respondeu nada (a menos que você tenha cometido um erro), mas ele guardou o número em uma posição de sua memória, e associou o símbolo ``d`` a essa posição. Agora, fica mais confortável converter dólares em reais::

    >>> 9.85 * d
    16.607099999999999
    >>> 11.95 * d
    20.147699999999997
    >>> 5 * d, 7 * d, 9 * d
    (8.4299999999999997, 11.802, 15.173999999999999)
    >>>

No último caso, convertemos de uma vez só os valores 5, 7 e 9 em dólares. Para um resultado mais apresentável, use o comando ``print``::

    >>> print 5 * d, 7 * d, 9 * d
    8.43 11.802 15.174
    >>>

E se a cotação do dólar mudou para 1.61? Basta armazenar o novo número e refazer os cálculos::

    >>> d = 1.61
    >>> print 5 * d, 7 * d, 9 * d
    8.05 11.27 14.49
    >>>

Você precisa digitar a linha mais longa de novo. No IDLE, clique sobre a linha que digitamos no exemplo anterior e tecle ``[ENTER]``. A linha será reproduzida na última deixa, e bastará um novo ``[ENTER]`` para processá-la. No console, teclando a seta para cima você acessa o histórico de comandos.

Tabela de preços em dólares e reais
====================================

Agora vamos mostrar como o interpretador Python é muito mais poderoso que uma calculadora. Imagine que em sua loja de discos importados você tem um balcão de ofertas com discos de $4 até $9. Se quisesse fazer uma tabela de preços em reais você poderia digitar::

    >>> print 4*d, 5*d, 6*d, 7*d, 9*d
    6.44 8.05 9.66 11.27 14.49
    >>>

Mas isso é um tanto chato e repetitivo. Em programação, sempre que você fizer algo repetitivo é porque não encontrou ainda a melhor solução. Lidar com séries de números é uma atividade comum, e Python pode ajudar muito nesses casos. Digite o seguinte::

    >>> lista = [5,6,7,8,9]
    >>>


Aqui nós criamos uma lista de preços na memória do computador e associamos o nome "lista" a esses dados. Em seguida, digite o seguinte (você terá que teclar ``[ENTER]`` duas vezes ao final dessa linha; depois saberá porque).

::

    >>> for p in lista: print p * d

    8.05
    9.66
    11.27
    12.88
    14.49
    >>>


Aqui nós instruímos o interpretador a fazer os seguintes passos:

- para cada item sucessivo da ``lista``:
    - associe o nome ``p`` ao item da vez
    - exiba o valor de ``p * d``

Agora digamos que você tem discos com valores de 4 a 15 dólares. Você poderia digitar a lista de novo, mas a coisa começa a ficar repetitiva novamente. Há uma forma melhor. A linguagem Python possui uma palavra chamada ``range`` que serve para gerar faixas de números. Vamos usar essa palavra. Digite::

    >>> range
    <built-in function range>
    >>>

Quando você digita o nome de uma função sem fornecer dados, Python limita-se a dizer a que se refere o nome. Nesse caso: ``built-in function range``, ou função embutida ``range``. Isso quer dizer que a palavra ``range`` é o nome de uma função, um tipo de comando que produz resultados a partir de dados fornecidos. E trata-se ainda de uma função embutida, ou seja, incluída no próprio interpretador (a maioria das funções da linguagem Python não são embutidas, mas fazem parte de módulos que o programador precisa chamar explicitamente; isso será explicado depois).

Acabamos de dizer que uma função "produz resultados a partir de dados fornecidos", então vamos fornecer algum dado para ver que resultados a função range produz. Digite ``range(5)`` e veja o que acontece::

    >>> range(5)
    [0, 1, 2, 3, 4]
    >>>

Quando apenas um dado N é fornecido, ``range`` gera uma lista de N números, de zero até N-1. É um comportamento um pouco estranho, mas útil em programação (o primeiro item de uma série, em Python e na maioria das linguagens, é o item número zero; isso será discutido mais profundamente quando aprendermos mais sobre listas).

Agora digamos que eu queira uma sequência a partir de 2, e não zero. Digite::

    >>> range(2,5)
    [2, 3, 4]
    >>>

Agora para obter a lista de valores de discos podemos digitar::

    >>> range(4,16)
    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    >>>

E usando o comando for, calcular de uma só vez todos os valores convertidos::

    >>> for p in range(4,16): print p * d
    ...
    6.44
    8.05
    9.66
    11.27
    12.88
    14.49
    16.1
    17.71
    19.32
    20.93
    22.54
    24.15
    >>>


Mas o ideal mesmo era ter os valores em dólares e reais lado a lado. Isso é fácil::

    >>> for p in range(4,16): print p, p * d
    ...
    4 6.44
    5 8.05
    6 9.66
    7 11.27
    8 12.88
    9 14.49
    10 16.1
    11 17.71
    12 19.32
    13 20.93
    14 22.54
    15 24.15
    >>>


Resumindo o que foi feito até aqui, com apenas duas linhas de código em Python, você pode gerar tabelas de conversão de qualquer tamanho. Experimente::

    >>> d = 1.686
    >>> for p in range(50,150): print p, p * d


Parabéns, você acaba de construir seu primeiro programa!
