=========================================
Capítulo 5: O segredo dos objetos-função
=========================================

O simulador de alunissagem {{{lunar.py}}}, apresentado no último capítulo, tem 50 linhas de código. É um jogo bem simples, mas foi nosso exemplo mais extenso até o momento. Em termos de programação profissional, trata-se de um programa bem pequeno. No mundo real, softwares modestos têm milhares de linhas de código, e essa contagem chega aos milhões quando se fala de grandes aplicativos como o Microsoft Word ou o sistema operacional Linux. Ao se trabalhar com programas maiores, é fundamental poder dividir o trabalho em módulos, em vez de criar uma solução "monolítica" como a do nosso lunar.py, onde o programa inteiro está expresso em uma única sequência de comandos. A partir de agora, vamos ver porque e como modularizar nossos programas, utilizando os conceitos de função, objeto, classe, módulo e pacote.

=== Dividir para conquistar ===

Um programa modularizado facilita o planejamento, a distribuição de tarefas entre vários programadores, o controle de qualidade e a reutilização de soluções. Por exemplo, no capítulo anterior utilizamos várias vezes sequências de comandos para ler dados do usuário, parecidas com o fragmento do programa {{{desprep1.py}}} (mostrado na listagem abaixo).

O ideal seria reunir sequências como esta em um módulo que nós pudéssemos reutilizar facilmente em qualquer um de nossos programas, em vez de redigitar ou cortar e colar esse código sempre que precisarmos reutilizá-lo. Ao evitar a redigitação, não só economizamos tempo, mas ainda limitamos a propagação de "bugs", ou falhas de programação. Imagine se, após meses de programação, usando centenas de vezes o fragmento, descobrimos que ele contém um erro em sua lógica. Se o código foi copiado manualmente para cada programa onde foi utilizado, seremos obrigados a localizá-lo e corrigi-lo em centenas de arquivos diferentes. Por outro lado, se o fragmento foi devidamente empacotado em um módulo, a correção somente precisa ser feita em um arquivo.

{{{
#!python
while 1:
    resp = raw_input('Quanto gastou %s? ' % pessoa)
    try:
        gasto = float(resp)
        break
    except:
        print 'Numero invalido.'
}}}

=== Programação estruturada ===

A primeira grande onda a favor da modularização no desenvolvimento de software foi a chamada "programação estruturada". No início dos anos 70, essa expressão estava tão na moda quanto a "programação orientada a objetos" de hoje. Na realidade, a programação orientada a objetos, ou OOP, pode ser entendida como uma radicalização da programação estruturada. A peça-chave da programação estruturada é o conceito de subprograma, um fragmento com começo, meio e fim, que desempenha um papel bem definido dentro de um programa maior. Na linguagem Python, um subprograma é definido através do comando de bloco def. Existem dois tipos de subprogramas: procedimentos e funções. Em Python, a única diferença entre eles é que as funções produzem valores, e os procedimentos não. Seguindo a tradição da linguagem C, os criadores do Python preferem falar apenas de funções, considerando os procedimentos apenas um tipo especial de função.

Vamos usar o IDLE para ver como se define uma função. Digite as duas linhas abaixo e tecle [Enter] duas vezes para concluir:

{{{
>>> def dobro(x):
... return x * 2
}}}

Aparentemente, nada acontece. Mas você acabou de definir uma função, chamada dobro, que está armazenada na memória do interpretador Python. Para ver sua função funcionar, basta invocá-la assim:

{{{
>>> dobro(3)
6
}}}

Agora vamos aos detalhes da nossa definição de função. A primeira linha, def dobro(x):, traz duas informações importantes: o nome da função, dobro, e a presença de um argumento, x. O argumento é uma variável especial que é associada ao valor fornecido pelo usuário na invocação da função. Ao receber a instrução dobro(3), Python associa x ao valor 3. A segunda linha da função, return x * 2 pode ser lida da direita para a esquerda. Primeiro Python calcula a expressão x * 2. Em nosso exemplo, o x está associado ao valor 3, portanto o resultado é 6. O comando return sinaliza o fim da função, e faz com que o resultado seja passado para quem a invocou. No exemplo abaixo, a função é invocada no meio de uma expressão aritmética:

{{{
>>> y = dobro(7) + 1
>>> y
15
>>>
}}}

É hora de quebrar algumas regras para ver o que acontece. Primeiro, experimente digitar isso:

{{{
>>> dobro()
}}}

O resultado será um "traceback" com a mensagem de erro "not enough arguments; expected 1, got 0", ou "argumentos insuficientes; 1 esperado, 0 recebido". Isso aconteceu porque nossa definição, def dobro(x), obriga o usuário da função a fornecer um argumento. É possível criar uma função que não pede argumentos, como veremos depois.

Outro experimento interessante é digitar apenas o nome da função:

{{{
>>> dobro
<function dobro at 82fa30>
}}}

Vale a pena parar e pensar no que acabou de acontecer.

Se você digita o nome da função sem parênteses, o interpretador não a executa, mas apenas informa a que se refere aquele nome. O que ocorre quando usamos o comando def é a criação, na memória, de um objeto do tipo "function", ou função. O nome fornecido após o comando def é associado ao objeto-função. Mas o objeto função existe independente do nome.

=== Funções como objetos ===

Acabamos de fazer uma afirmação importante, que vale a pena repetir: Python permite criar funções que são tratadas da mesma forma que outros objetos da linguagem, como números e listas. Para entender as implicações disso, é bom reforçar o nosso entendimento de como Python lida com os objetos que criamos. Para tanto, vamos deixar as funções um pouco de lado e voltar a brincar com listas:

{{{
>>> l = [10,20,30,40]
}}}

Acabamos de criar uma lista "l" com quatro elementos. Essa é a forma sucinta de dizer o que ocorreu. Uma descrição bem melhor é a seguinte: criamos uma lista com quatro elementos e associamos a variável "l" a esta lista. A letra "l" é apenas uma etiqueta que identifica a lista; é importante notar que a lista existe mesmo antes de receber uma etiqueta.

Comprove:

{{{
>>> m = l
>>> m
[10, 20, 30, 40]
>>>
}}}

Agora associamos m a l, ou melhor, à lista associada a l. Nosso objeto-lista agora tem duas etiquetas. Podemos usar qualquer uma delas para nos referirmos a ele, tanto que, ao digitarmos m, o interpretador mostra a mesma lista. Podemos também acessar e modificar um item específico da lista:

{{{
>>> m[2]
30
>>> m[2] = 55
>>> m
[10, 20, 55, 40]
>>>
}}}

Agora digite l e veja o resultado:

{{{
>>> l
[10, 20, 55, 40]
>>>
}}}

O que aconteceu com o l? Absolutamente nada! Ele continua sendo uma mera etiqueta colada em nosso objeto-lista. Mudamos a lista através da etiqueta m, mas tanto m quanto l referem-se à mesma lista, como você acabou de comprovar.

O mesmo ocorre com funções. Ao interpretar o código def dobro(x): return x * 2, Python cria um objeto-função e o associa à etiqueta dobro. Nada impede que você associe outras etiquetas ao mesmo objeto, assim:

{{{
>>> f = dobro
>>> f
<function dobro at 82fa30>
}}}

Note que o nome f agora está associado ao mesmo objeto-função que antes chamamos de dobro.

O novo nome também pode ser usado para invocar a função:

{{{
>>> f(19)
38
>>> y = f(17) + 2
>>> y
36
>>>
}}}

Ao tratar funções como objetos, Python deixa para trás linguagens mais tradicionais como C++ e Java, e se junta a uma classe de linguagens utilizadas em trabalhos avançados de Ciência da Computação: linguagens de programação funcional. A mais famosa delas, Lisp, tem sido ferramenta fundamental na pesquisa de Inteligência Artificial há várias décadas. Um dialeto simplificado de Lisp, chamado Scheme, é usado nos cursos introdutórios de computação do MIT (Massachussetts Institute of Technology), um dos mais importantes centros de pesquisa em informática do planeta. Como você vê, estudando Python estamos em ótima companhia.

Vejamos na prática uma vantagem de tratarmos funções como objetos. Python possui uma função poderosa chamada map. Vamos usá-la agora:

{{{
>>> map(dobro, m)
[20, 40, 110, 80]
>>>
}}}

Invocamos a função map com dois argumentos. O primeiro é a nossa função dobro, e o segundo é a lista m, [10, 20, 55, 40]. A função map aplica o objeto-função a cada item do segundo argumento. O resultado é a criação de um novo objeto-lista, sem modificar o original.

Veja este outro exemplo:

{{{
>>> map(str, m)
['10', '20', '55', '40']
>>>
}}}

Neste caso, usamos a função embutida (ou pré-definida) str para converter cada um dos itens numéricos em uma string.

=== Argumentos default ===

Como já dissemos, uma função não precisa retornar um valor. Veja este exemplo:

{{{
>>> def bom_dia():
... print 'Bom dia, humanóide!'
}}}

Isso é o que chamamos de procedimento: uma função que faz alguma coisa (neste caso, imprime uma mensagem), mas não retorna um valor. Você pode invocá-lo assim:

{{{
>>> bom_dia()
Bom dia, humanóide!
>>>
}}}

É inútil usar esse procedimento em uma expressão:

{{{
>>> x = bom_dia()
Bom dia, humanóide!
>>> x
>>> x == None
1
>>>
}}}

Nossa função bom_dia dispensa argumentos, já que em sua definição não colocamos nada entre os parênteses. Para sermos mais simpáticos com nossos usuários, poderíamos modificá-la para aceitar um nome, desta maneira:

{{{
>>> def bom_dia(nome = 'humanóide'):
... print 'Bom dia, %s!' % nome
}}}

Note que, neste caso, associamos um valor ao argumento nome. É o chamado valor "default", que será usado caso o argumento não seja fornecido.

Veja como:

{{{
>>> bom_dia('Martinha')
Bom dia, Martinha!
>>> bom_dia()
Bom dia, humanóide!
>>>
}}}

A idéia de argumento default é outro ponto forte da linguagem Python, oferecendo grande flexibilidade na definição de funções.

=== Usando módulos ===

Uma vez entendido o básico de funções, podemos passar para os módulos, que são coleções de funções. Antes de criarmos nossos próprios módulos, é bom aprender a usar módulos prontos, para não ficarmos "reinventado a roda". Assim como qualquer boa linguagem moderna, Python possui uma coleção de módulos com milhares de funções testadas e prontas para uso em diferentes tipos de aplicações. O Python inclui mais de 140 módulos, sem contar com a extensão gráfica Tk. E muitos outros podem ser encontrados a partir do site Python.org, quase todos livres e gratuitos.

Que tipo de coisa pode ser encontrada nessa vasta biblioteca? Eis alguns exemplos de módulos, apenas para dar uma idéia:

   * {{{cgi}}}: programação de páginas dinâmicas para a Web
   * {{{ftplib}}}: montagem de scripts para interação com servidores FTP
   * {{{gzip}}}: leitura e escrita de arquivos comprimidos
   * {{{math}}}: funções matemáticas (trigonometria, logaritmos etc.)
   * {{{re}}}: buscas de texto avançadas com expressões regulares (como na linguagem Perl)
   * {{{string}}}: operações com strings, incluindo conversões de listas
   * {{{time}}}: hora atual e conversão de formatos de data
   * {{{xmllib}}}: interpretação de arquivos em formato XML

Como primeiro exemplo de como se usa um módulo, vamos recorrer ao módulo calendar, um conjunto de funções de alto nível (ou seja, fáceis de usar) para gerar calendários. Voltando ao seu interpretador Python, digite o seguinte:

{{{
>>> import calendar
}}}

O comando import geralmente não produz um resultado visível. Ele localiza o módulo mencionado, carrega para a memória suas funções e executa os comandos de inicialização do módulo, se existirem. Em nosso caso, as funções do arquivo calendar.py acabaram de ser lidas para a memória. Para usá-las, você digita o nome do módulo e o nome da função separados por um ".":

{{{
>>> calendar.prmonth(2000,3)
     March 2000
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
>>>
}}}

Fornecendo o ano e o mês, você recebe o calendário do mês prontinho. Existe também uma função para gerar um calendário anual. Experimente:

{{{
>>> calendar.prcal(2000)
}}}

Devido a limitações das bibliotecas-padrão da linguagem C que são a base do Python, o módulo calendar não chega a ser um "calendário perpétuo". Ele só trabalha com datas de janeiro de 1970 a janeiro de 2038. Para os curiosos, a explicação é que, internamente, as funções de C armazenam datas contando o número de segundos transcorridos desde 1/1/1970. Exatamente sete segundos após 1:14 da madrugada do dia 19/01/2038, esse número excederá o limite de um número inteiro de 32 bits. É mais um bug do novo milênio...

Agora, vamos supor que você deseja exibir o calendário mensal de uma outra maneira, por exemplo, separando os dias por tabs, para facilitar a exportação para um programa de editoração eletrônica. Ou ainda, podemos querer gerar um calendário em HTML. Nesses dois casos, o resultado da função prmonth() não é muito útil. A função monthcalendar() nos dá mais liberdade. Veja como ela funciona:

{{{
>>> calendar.monthcalendar(2000,3)
[[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9,
10, 11, 12], [13, 14, 15, 16, 17, 18,
19], [20, 21, 22, 23, 24, 25, 26], [27,
28, 29, 30, 31, 0, 0]]
>>>
}}}

O resultado é uma lista de listas. Cada uma das cinco listas de dentro representa uma semana com seus respectivos dias. Zeros aparecem nos dias que ficam fora do mês.

Agora vamos começar a destrinchar o resultado da função monthcalendar. Antes de mais nada, já que vamos usar muitas vezes essa função, podemos economizar alguma digitação se usarmos uma outra forma do comando import:

{{{
>>> from calendar import monthcalendar
}}}

Agora não precisaremos mais usar o prefixo calendar, podendo chamar a função monthcalendar() diretamente por seu nome; assim:

{{{
>>> for semana in monthcalendar(2000,3):
...     print semana
...
[0, 0, 1, 2, 3, 4, 5]
[6, 7, 8, 9, 10, 11, 12]
[13, 14, 15, 16, 17, 18, 19]
[20, 21, 22, 23, 24, 25, 26]
[27, 28, 29, 30, 31, 0, 0]
>>>
}}}

Através do comando for, listamos separadamente cada semana. Para trabalhar com cada dia individualmente, podemos criar outro comando for para percorrer cada uma das semanas. O resultado você pode ver na listagem 2.

A cada ciclo do primeiro for, a variável semana representa uma lista de sete dias. No segundo for, cada ciclo escreve na tela um dia. Para que todos os dias da semana apareçam na mesma linha, usamos um truque do comando print: a vírgula no final de print '%s\t' % dia, faz com que o Python não inicie uma nova linha. Note pela indentação que o último comando print está dentro do primeiro for, e não dentro do segundo. Isso significa que esse print será executado uma apenas vez para cada semana.

Em programação, sempre há uma outra forma de obter algum resultado. Neste caso, não resistimos à tentação de mostrar um outro jeito de gerar a mesma listagem. O módulo string contém uma função, join, que serve para transformar listas em strings, concatenando (juntando) os elementos da lista com algum elemento separador. Para usar esta função, precisamos primeiro importá-la:

{{{
>>> from string import join
}}}

Para testá-la, experimente digitar algo assim:

{{{
>>> join(['1','2','3'])
'1 2 3'
>>> join(['1','2','3'], ' + ')
'1 + 2 + 3'
>>>
}}}

Note que o segundo argumento define a string que será usada como separador. No primeiro exemplo, omitimos o separador e Python usou o argumento default, um espaço. Agora vamos pegar uma semana do mês para fazer mais algumas experiências:

{{{
>>> s = monthcalendar(2000,3)[0]
>>> s
[0, 0, 1, 2, 3, 4, 5]
>>>
}}}

Aqui usamos o mecanismo de indexação de Python para obter apenas uma semana do mês. Chamamos a função monthcalendar(2000,3) com um índice, [0]. Lembre-se que monthcalendar retorna uma lista de listas. O índice [0] refere-se ao primeiro elemento da lista, ou seja a lista dos dias da primeira semana de março de 2000. Para exibir os dias dessa semana separados por tabs, usamos a função join com o caractere de tabulação, representado por '\t', assim:

{{{
>>> join(s, '\t')
Traceback (innermost last):
  File "<interactive input>", line 1, in ?
TypeError: first argument must be sequence of strings
>>>
}}}

Oops, Python reclamou: "Erro de tipo: o primeiro argumento tem que ser uma sequência de strings". Precisamos transformar a lista s, que contêm números, em uma lista de strings. Felizmente, acabamos de descobrir como fazer isso usando a função map, no início deste capítulo:

{{{
>>> map(str, s)
['0', '0', '1', '2', '3', '4', '5']
}}}

Agora podemos executar o join:

{{{
>>> join(map(str,s), '\t')
'0\0110\0111\0112\0113\0114\0115'
}}}

O resultado ficou pouco apresentável, porque Python exibe o caractere "tab" através de seu código em numeração octal, \011. Mas isso não ocorre se usamos o comando print:

{{{
>>> print join(map(str,s), '\t')
0   0   1   2   3   4   5
>>>
}}}

Agora podemos fazer em duas linhas o que fizemos em quatro linhas na listagem abaixo:

{{{
>>> for semana in monthcalendar(2000,3):
...     for dia in semana:
...         print '%s\t' % dia,
...     print
...
0   0   1   2   3   4   5
6   7   8   9   10  11  12
13  14  15  16  17  18  19
20  21  22  23  24  25  26
27  28  29  30  31  0   0
>>>
}}}

Veja:

{{{
>>> for semana in monthcalendar(2000,3):
...     print join( map(str,semana), '\t')
...
0   0   1   2   3   4   5
6   7   8   9   10  11  12
13  14  15  16  17  18  19
20  21  22  23  24  25  26
27  28  29  30  31  0   0
>>>
}}}

Agora que aprendemos o básico sobre funções e sabemos como importar módulos, estamos prontos para criar nossas próprias "bibliotecas de código". Hoje vimos como definir e importar funções. Em seguida, aprenderemos como organizá-las em módulos e usá-las no contexto de programas maiores, aplicando primeiro conceitos da programação estruturada, e depois, da orientação a objetos. Mas isso terá que ficar para o mês que vem.
