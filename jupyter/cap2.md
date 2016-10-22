Capítulo 2: Criando uma tabela
==============================

No final do capítulo anterior digitamos o seguinte programa diretamente no interpretador Python:

    >>> d = 1.686
    >>> for p in range(50,150): print p, p * d

O resultado desta seqüência de comandos é uma longa lista de números em duas colunas. Sabemos que a primeira coluna da esquerda contém preços em dólar e a outra, em reais. Mas nada na listagem indica isto. Observe esse trecho:

    95 160.17
    96 161.856
    97 163.542
    98 165.228
    99 166.914
    100 168.6
    101 170.286
    102 171.972
    103 173.658
    104 175.344
    105 177.03

Aqui podemos observar outras deficiências: as colunas não estão corretamente alinhadas, e os valores em reais aparecem com uma, duas ou três casas decimais. Como se trata de uma tabela de preços, os valores em ambas colunas deveriam ter sempre duas casas decimais. Vamos fazer algumas melhorias em nosso programa gerador de tabelas de preços.

Quatro tipos de dados
---------------------

Para evitar aquele degrau na segunda coluna entre o 99 e o 100, precisamos fazer um pequeno desvio para começar a aprender a lidar com textos, além de números. Digite `eu =` seguido do seu nome entre aspas:

    >>> eu = 'Fulano'

Você tem que digitar as aspas para evitar um erro. As aspas podem ser 'simples' ou "duplas". Python guardará uma cópia do seu nome na memória do computador, e associará o identificador `eu` a esse dado. Agora basta digitar eu para ver o seu nome.

    >>> eu
    'Fulano'
    >>>

Antes havíamos criado a variável `d` referindo-se à cotação do dólar, e no capítulo anterior também criamos uma variável chamada `lista`, contendo uma lista de valores. Agora criamos a variável `eu` para se referir ao seu nome. Estes são exemplos de três tipos de dados que Python é capaz de processar: número de ponto flutuante, lista de valores, e texto.

Você pode saber o tipo de uma variável ou estrutura de dados usando a função `type`. Veja estes exemplos:

    >>> eu = 'Luciano'
    >>> d = 1.902
    >>> type(eu)
    <type 'str'>
    >>> type(d)
    <type 'float'>
    >>>

Python acaba de nos dizer que a variável `eu` refere-se a um objeto do tipo `str`, uma abreviatura de "string" (basicamente o computador encara um texto como uma cadeia de caracteres). E a variável `d` aponta para um objeto do tipo `float`, ou "número de ponto-flutuante", como já vimos antes.

Vejamos mais alguns tipos de dados:

    >>> type(1)
    <type 'int'>
    >>> type(1.)
    <type 'float'>
    >>> type([1,2,3])
    <type 'list'>
    >>>

Observe que o número 1 não é `float`, mas `int`. Já o número `1.` ("um" seguido de um ponto decimal) é considerado um `float`. Como já dissemos no primeiro capítulo, inteiros e ''floats'' têm tratamento diferente em Python. Uma divisão de inteiros (como 7/2), sempre fornece um resultado inteiro (3, nesse exemplo). O próximo dado testado é uma lista, `[1,2,3]`, que Python chama de `list`.

Agora, experimente fazer esses dois testes:

    >>> type(range)
    <type 'builtin_function_or_method'>
    >>> type(range(3))
    <type 'list'>
    >>>

Ao perguntarmos qual é o tipo associado ao nome `range`, Python responde: `builtin_function_or_method`. Também já vimos isso no capítulo anterior: o nome `range` refere-se a uma função embutida no próprio interpretador. No teste seguinte, fornecemos um argumento para a função `range`, e assim produzimos um resultado (neste caso, a lista `[0,1,2]`, que foi criada na memória do seu computador, mas não foi exibida). É sobre este resultado que a função `type` foi aplicada, retornando a informação de que se trata de um dado do tipo `list`. Ou seja, `range` é uma expressão do tipo `builtin_function_or_method`, mas `range(3)` é uma expressão do tipo `list`. Faz sentido? Se não faz, escreva reclamando!

Cada tipo de dados suporta operações diferentes. Faça algumas experiências e analise os resultados:

    >>> n1 = 10
    >>> n2 = 20
    >>> n1 + n2
    30
    >>> n1 = 'abacate'
    >>> n2 = 'banana'
    >>> n1 + n2
    'abacatebanana'
    >>> n2 + n1
    'bananaabacate'
    >>>

Por exemplo, o operador + realiza uma soma quando aplicado a dados numéricos, mas quando aplicado a dados do tipo '`string`', o sinal `+` faz uma operação de concatenação (junção de duas seqüências). Agora experimente isto:

    >>> x = 3.
    >>> x * 5
    15.0
    >>> 'x' * 5
    'xxxxx'
    >>>

Note que x e 'x' são coisas totalmente diferentes. x é o nome de uma variável que neste momento se refere ao valor `3.` (um '`float`'). O resultado de `x * 5` é `15.0` (outro '`float`', como era de se esperar). Já `x` é uma '`string`' com um caractere. Quando o sinal `*` é aplicado entre uma '`string`' e um número inteiro, Python realiza uma operação de repetição. Como você pode notar, os operadores `+` e `*` fazem coisas diferentes dependendo dos tipos de dados fornecidos na expressão.

É um prazer trabalhar com Python porque é uma linguagem muito coerente. Observe:

    >>> [1,2] + [3,4]
    [1, 2, 3, 4]
    >>> '12' * 3
    '121212'
    >>> [1,2] * 3
    [1, 2, 1, 2, 1, 2]
    >>>

No primeiro exemplo, vemos o operador `+` concatenando duas listas. Os outros dois exemplos mostram a operação de repetição. Note que `12` não é um número, mas uma '`string`' composta pelos caracteres `1` e `2`. Para Python, '`strings`' e listas têm muito em comum: ambas são seqüências de itens. Enquanto '`strings`' são seqüências de caracteres, listas são seqüências de itens quaisquer. Nos dois casos, concatenação e repetição funcionam de forma logicamente idêntica.

Enfeitando a tabela
-------------------

Agora que sabemos sobre alguns tipos de dados, e que os operadores funcionam de forma diferente conforme os dados da expressão, estamos prontos para aperfeiçoar nosso gerador de tabelas usando o poderoso operador '%', que em Python não tem nada a ver com porcentagens. Para ver como ele funciona, vamos criar uma '`string`' como esta:

    >>> msg = 'um dólar vale %f real.'
    >>>

Agora vamos ver o que acontece quando chamamos a variável `msg`:

    >>> msg
    'um d\363lar vale %f real.'
    >>>

Python representa varíaveis '`string`' dessa forma: entre aspas simples, e trocando os acentos por códigos especiais (estamos falando do código ASCII em notação octal, algo que explicaremos depois). Se você quiser exibir o conteúdo de `msg` de forma mais apresentável, use o comando `print`:

    >>> print msg
    um dólar vale %f real.
    >>>

OK, é hora de explicar porque colocamos esse estranho `%f` dentro da mensagem. Trata-se de um marcador de posição para sinalizar onde Python deverá inserir um número quando quisermos imprimir a mensagem com o valor da cotação. Experimente digitar o seguinte:

    >>> d = 1.902
    >>> print msg % d
    um dólar vale 1.902000 real.
    >>>

Veja o que aconteceu: Python substituiu a marca `%f` pelo valor da variável `d`. É assim que funciona: a partir de uma '`string`' com marcas de posição e um ou mais valores, o operador `%` produz uma nova '`string`' com os valores inseridos nas respectivas posições. Veja agora um exemplo com dois valores:

    >>> msg2 = 'Um dólar vale %f real e um real vale %f dólar.'
    >>> print msg2 % (d, 1/d)
    Um dólar vale 1.902000 real e um real vale 0.525762 dólar.
    >>>

Note que os valores `d` e `1/d` estão entre parênteses. Isso é obrigatório quando queremos passar mais de um valor para o operador `%` (uma sequência de valores entre parênteses é uma "tupla", um tipo especial de sequência que explicaremos em um outro capítulo).

O símbolo `%f` serve para informar a Python que o valor a ser inserido naquela posição é um '`float`'. Se você quiser limitar o número de casas após o ponto decimal, basta usar um formato como esse:

    >>> d = 1.685
    >>> '%.2f' % d
    '1.69'
    >>>

Após o marcador `%`, a indicação `.2` determina que devem aparecer duas casas decimais após o ponto. Note que o resultado é arredondado: `1.685` virou `1.69`. Vamos usar esse recurso na nossa tabela:

    >>> for p in range(4,16):  print 'US$ %.2f = R$ %.2f' % (p,p*d)

    US$ 4.00 = R$ 6.74
    US$ 5.00 = R$ 8.43
    US$ 6.00 = R$ 10.12
    US$ 7.00 = R$ 11.80
    US$ 8.00 = R$ 13.49
    US$ 9.00 = R$ 15.17
    US$ 10.00 = R$ 16.86
    US$ 11.00 = R$ 18.55
    US$ 12.00 = R$ 20.23
    US$ 13.00 = R$ 21.92
    US$ 14.00 = R$ 23.60
    US$ 15.00 = R$ 25.29
    >>>

Está quase linda. Falta só consertar o degrau que acontece entre a linha do 9 e do 10. No marcador de posição você também pode colocar um número à esquerda do ponto para definir a largura total do espaço que será reservado. Na faixa de preços de 4 a 15, os maiores valores tem cinco caracteres de comprimento (incluindo o ponto decimal), por isso vamos usar `%5.2f`. Agora podemos fazer uma versão bem melhor da tabela:

    >>> for p in range(4,16):  print 'US$ %5.2f = R$ %5.2f' % (p,p*d)

    US$  4.00 = R$  6.74
    US$  5.00 = R$  8.43
    US$  6.00 = R$ 10.12
    US$  7.00 = R$ 11.80
    US$  8.00 = R$ 13.49
    US$  9.00 = R$ 15.17
    US$ 10.00 = R$ 16.86
    US$ 11.00 = R$ 18.55
    US$ 12.00 = R$ 20.23
    US$ 13.00 = R$ 21.92
    US$ 14.00 = R$ 23.60
    US$ 15.00 = R$ 25.29
    >>>

Entendendo melhor o for
-----------------------

Como você percebeu, no comando `for` tudo aquilo que aparece após os sinal ":" é repetido várias vezes, uma vez para cada item da lista de valores indicada após a palavra `in`. Mas os comandos a serem repetidos podem ser vários, e na maioria das vezes não são escritos na mesma linha que o `for`, como temos feito, mas sim em linhas subseqüentes.

O comando `for` é algo que chamamos de "estrutura de controle", que serve para determinar a forma de execução de um comando ou de uma seqüência de comandos, às vezes chamada de um "bloco". Em outras linguagens, os blocos são delimitados por marcadores especiais. Java, Perl e C++ usam os sinais { e } para este fim. Pascal e Delphi usam as palavras `BEGIN` e `END`. Além desses marcadores exigidos pelas linguagens, os programadores usam também o recurso da endentação, ou seja, o recuo em relação à margem esquerda, para tornar mais fácil a visualização da estrutura do programa. Veja este exemplo em Perl:

``` sourceCode
for ($i = 0; $i < 5; $i++) {  # Atenção: isto é Perl, e não Python.
    $v = $i * 3;
    print "$v\n";
}
```

Aqui, os comandos `$v = $i * 3;` e `print "$v\n";` formam o bloco que está sobre o controle do comando `for`, ou seja, os dois comandos serão executados repetidamente. O programa equivalente em Python é escrito assim:

    for i in range(5):
        v = i * 3
        print v

Na minha opinião, o código em Python é bem mais legível. Para sinalizar quais comandos fazem parte do bloco que está sob o controle do `for`, apenas a endentação é utilizada. Se você está usando o IDLE, esse recuo acontece automaticamente quando uma linha de comando termina com o sinal ':', que em Python sempre indica o início de um bloco. No interpretador Python invocado a partir da linha de comando no DOS ou em UNIX, a endentação não é automática. Você precisa digitar ao menos um espaço em branco para evitar uma mensagem de erro como essa:

    >>> for i in range(5):
    ... print i
      File "", line 2
        print i
            ^
    SyntaxError: invalid syntax

Note que o interpretador está reclamando de sintaxe inválida, e apontando (^) para a primeira palavra do bloco que deveria estar recuado. Veja a mesma coisa, com a segunda linha recuada com a tecla \[TAB\]:

    >>> for i in range(5):
    ...     print i
    ...
    0
    1
    2
    3
    4
    >>>

Já deve ter ficado claro porque era preciso teclar \[ENTER\] duas vezes depois do `for` nos exemplos anteriores: é que, no modo interativo, o interpretador Python espera uma linha em branco para sinalizar o final de uma série de comandos que formam um bloco dentro de uma estrutura de controle.

Agora que entendemos o conceito de bloco, podemos enfeitar ainda mais a nossa tabela colocando um segundo comando `print` dentro do nosso `for`.

Veja este exemplo:

    >>> for p in range(9,13):
    ...    print 'US$ %5.2f = R$ %5.2f' % (p, p * d)
    ...    print '-' * 20
    ...
    US$  9.00 = R$ 15.17
    --------------------
    US$ 10.00 = R$ 16.85
    --------------------
    US$ 11.00 = R$ 18.54
    --------------------
    US$ 12.00 = R$ 20.22
    --------------------
    >>>

A outra face do `%`
-------------------

Antes de encerrar este capítulo, vale a pena contar que, assim como o `+` e o `*`, o operador `%` também tem dupla personalidade. Quando aplicado sobre dois números, que podem ser inteiros ou '`floats`', o `%` retorna o resto da divisão inteira do primeiro pelo segundo. Veja só:

    >>> 6 % 3
    0
    >>> 7 % 3
    1
    >>> 8 % 3
    2
    >>> 9 % 3
    0
    >>>

Explicando: `6 / 3` dá 2, e o resto é 0; a divisão inteira de `7 / 3` também dá 2, mas o resto é 1. Esta operação é chamada de "modulo" em inglês. Sua principal utilidade é determinar se um número é múltiplo de outro. Nos exemplos acima, o resultado de `6 % 3` e `9 % 3` é zero, porque 6 e 9 são múltiplos de 3.

No próximo capítulo vamos começar a elaborar programas mais extensos. O modo interativo, que temos usado até agora, vai continuar sendo útil para testarmos novas idéias e observar o comportamento de funções e módulos do Python rapidamente. Mas, a partir da próxima sessão, vamos começar a gravar nossos programas para uso posterior, em vez de digitá-los diretamente no interpretador. E vamos também descobrir como solicitar informações do usuário, de forma que os programas possam ser utilizados por pessoas que não sabem programar e preferem ficar longe de um interpretador interativo.
