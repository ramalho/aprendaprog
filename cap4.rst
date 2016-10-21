.. highlight:: python
   :linenothreshold: 5

=============================================================
Capítulo 4: Orçamentos, pousos lunares e tratamento de erros
=============================================================

O capítulo anterior terminou com uma questão no ar. Após estudarmos todas as formas de se usar o comando if, restou o desafio de usar um bloco elif para consertar um pequeno defeito no programa ``despdom2.py``. O bug se manifesta quando os gastos de Ana e Bia são iguais. Nesse caso, o programa escreve na tela::

  Bia deve pagar: R$ 0.0

Em vez de fazer a Bia escrever um cheque de zero reais, o melhor seria tratar esse caso especial. Veja como fazê-lo, usando uma construção if/elif/else (listagem 1). Se você guardou o arquivo despdom2.py da lição anterior, terá muito pouco o que digitar. Abra-o e salve com o nome de despdom3.py. O código é idêntico à versão anterior até a linha 14. Ali, você faz a primeira alteração: o else é substituído por um elif que verifica se Bia gastou menos que a média. As linhas 15 e 16 continuam como antes, mas agora elas só serão executadas se bia < media for verdadeiro. As linhas 17 e 18 são novas, e servem para tratar o caso em que nem ana < media nem bia < media, ou seja, quando não há diferença a ser paga. Agora você pode testar o programa digitando valores diferentes e depois valores iguais para as despesas de Ana e Bia.

.. literalinclude:: codigo/despdom3.py

Somadora infinita
==================

Logo adiante iremos reescrever o programinha acima para torná-lo mais flexível, permitindo digitar os nomes e os gastos de qualquer número de pessoas. Assim ele será útil para repartir as contas de uma viagem de férias ou daquela festa entre amigos. Para começar, vamos construir um programa um pouco mais simples, capaz de somar uma série de números (listagem 2).

.. literalinclude:: codigo/somadora1.py

Vamos ver o que faz esse programa, linha por linha.

Linhas 3 e 4
  Exibimos as instruções de uso.

Linha 5
  Usamos a função ``raw_input()`` para exibir o sinal ":" e ler o primeiro valor digitado pelo usuário, e a função float para transformar a ''string'' resultante em um número de ponto flutuante. O resultado é armazenado na variável n.

Linha 6
  A variável total servirá para guardar a soma acumulada. Para começar, colocamos nela o primeiro valor digitado.

Linha 7
  Aqui usamos um novo comando de bloco, o while. Essa linha pode ser traduzida assim: "enquanto n é diferente de zero...". Assim como o comando for, o while causa a execução repetida do bloco subordinado (linhas 8 e 9). Em um comando while, a repetição é condicionada a uma expressão lógica do mesmo tipo que usamos com o comando if. Nesse exemplo, a condição n != 0 causará a repetição do bloco enquanto for verdadeiro que n é diferente de 0. No momento que n contiver o valor 0, a condição será falsa e a repetição deixará de ocorrer. O programa então seguirá para a linha 10.

Linha 10
  Mostramos o total acumulado. Fim do programa.

Mais sobre o while
===================

Os comandos while e for são semelhantes por causarem a repetição de um bloco. Ambos são chamados, pelos computólogos, de comandos de iteração (iteração é sinônimo de repetição; não confunda com "interação", que é uma ação recíproca entre dois ou mais agentes).

A diferença é que no comando for a iteração serve para percorrer uma lista de itens, como fizemos anteriormente quando trabalhamos com tabelas de conversão. No caso do for, o número de repetições é sempre conhecido de antemão: o bloco será executado uma vez para cada item da lista. O comando while serve para todos os outros casos de iteração, quando o número de repetições é indefinido. Nossa somadora infinita é um exemplo típico: a iteração que solicita valores e os totaliza poderá ser repetida qualquer número de vezes, dependendo apenas da sua vontade.

Agora vamos analisar de perto duas circunstâncias especiais. Rode o programa e digite 0 (zero) como primeiro valor. Nas linhas 5 e 6 o programa armazenará o zero nas variáveis n e total. A seguir, na linha 7, o comando while verificará a condição n != 0. Nesse caso, a condição será falsa. Então o bloco subordinado ao while não será executado nenhuma vez, e o programa passará direto para a linha 10, mostrando o total.

Outro momento interessante ocorre quando o primeiro valor digitado não é zero, e a iteração é executada. Digamos que o usuário digitou [1][Enter], [2][Enter] e [0][Enter]. O zero digitado pelo usuário será lido e armazenado em n na linha 8, como já vimos. Na linha 9 o valor de n é somado ao total. Nessa iteração o valor de n é zero, portanto estamos somando zero ao total, uma operação inofensiva. Só após efetuar essa soma inútil, o programa retornará ao início do bloco e verificará que a condição do while não é mais verdadeira, pois agora nosso n é igual a zero. É importante perceber que, apesar de o valor de n passar a ser zero na linha 8, a execução continua até o fim do bloco, passando pela linha 9, para só então ocorrer o retorno ao início do bloco e a verificação da condição de continuidade da repetição.

Quando estudamos as condições lógicas no final do capítulo anterior, aprendemos que Python considera o valor 0 (zero) como sinônimo de "falso", e valores não-zero como "verdadeiros". Programadores experientes em Python costumam tirar proveito desse fato para abreviar as condições que colocam em seus ifs e whiles. Em nosso programa ``somadora1.py``, a linha 7::

  while n != 0:

pode ser escrita de forma mais abreviada assim::

  while n:

Faça essa alteração no programa e experimente. Você verá que nada mudou no seu funcionamento. Isso porque, quando n é diferente de zero, a condição "n" expressa em ``while n:`` é considerada verdadeira, e a iteração é executada. Quando n passa a ser zero, a condição é falsa, encerrando a iteração.

Loops (quase) infinitos
========================

Outra forma de escrever a somadora, mais elegante em minha opinião, é a mostrada na listagem 3.

.. literalinclude:: codigo/somadora2.py

Aqui a lógica é um pouco diferente: na linha 6 o loop ``while`` tem como condição a constante ``True``, ou "verdadeiro". Assim o loop das linhas 6 a 9 seria repetido infinitas vezes, em tese. Na prática, a linha 8 verifica se o valor de n é zero. Em caso afirmativo, o comando "break" é acionado. Isso faz com que o loop while seja interrompido imediatamente, e a execução do programa passa diretamente para a próxima linha após o bloco (linha 10 em nosso exemplo).

Essa forma de codificar, usando loops infinitos com breaks, não está de acordo com a Programação Estruturada, a filosofia dominante entre os programadores nos anos 70. O problema é que não fica imediatamente aparente qual é a condição de terminação do loop e alguns professores de computação podem descontar pontos por isso. Mas em se tratando de um bloco de apenas três linhas, não acho que isso seja um grande problema. A vantagem é que agora a função de leitura de dados ocorre em apenas um lugar no programa (na linha 7) e não em dois, como na versão anterior (linhas 5 e 8 de somadora1.py). Isso simplificará nossa próxima alteração. Além disso, não acontece mais a totalização inútil da linha 9, somando zero ao total na saída, porque o comando break da linha 8 faz o programa passar direto para a linha 10.

Uma forma mais natural de codificar esse loop seria usar comandos com o do/while ou repeat/until existentes em linguagens como C/C++/Java e Pascal/Delphi; nessas estruturas de controle, o teste é feito no fim do loop, garantindo a execução do bloco ao menos uma vez. É o que precisamos fazer aqui, mas Python não possui um comando de loop especial para essa situação. Vejamos outro exemplo.

Suponha que você queira, por algum motivo estranho, somar os números naturais (1, 2, 3 etc.) até obter um total maior ou igual a 100. Observe na listagem 4 como ficaria o loop central para fazer isso em Delphi, Java e Python.

Delphi
-------

.. code-block:: pascal

  REPEAT
      n := n + 1;
      total := total + n;
  UNTIL (total >= 100);


Java
-----

.. code-block:: java

  do {
      n = n + 1;
      total = total + n;
  } while (total < 100);


Python
-------

::

  while True:
      n = n + 1
      total = total + n
      if total >= 100: break

Note que os três programas acima estão incompletos; reproduzimos apenas o loop principal. Generalizando, qualquer loop com teste no final pode ser codificado em Python usando-se uma combinação de while True e if/break, assim::

  while True:
      comando1
      comando2
      # etc.
      if condicao_final: break

Um programa mais tolerante
===========================

Um defeito das nossas somadoras, e de todos os programas que fizemos até agora, é que eles não toleram falhas na digitação. Se você rodar o programa ``somadora2.py`` e digitar apenas [Enter] para encerrar, verá a seguinte mensagem na tela::

   Traceback (innermost last):
         File 'somadora1.py', line 7, in ?
    n = float(raw_input())
   ValueError: empty string for float()

A segunda linha dessa mensagem identifica o local do erro: linha 7 do arquivo (file) ``somadora1.py``. Na terceira linha está reproduzida a linha do programa onde ocorreu o problema, e a mensagem final informa qual foi o erro. Podemos traduzí-la assim: "Erro de valor: ''string'' vazia para a função ``float()``".

O problema é que, ao digitarmos ``[Enter]`` sem fornecer um número, a função ``raw_input()`` retorna uma ''string'' vazia (nada mais justo, pois nada foi digitado). Em seguinda, a função ``float()`` tenta transformar a ''string'' vazia em um ponto flutuante, mas não sabe como. É ela que dispara a mensagem de erro, fazendo com que o programa seja interrompido antes de mostrar o valor total da soma.

Efeito semelhante pode ser obtido se você digitar um texto qualquer em vez de um número. Experimente.

Nesse caso, a mensagem de erro final é: "ValueError: invalid literal for ''float''(): blah". Nesse caso, a reclamação é de "''invalid literal''", significando que o texto fornecido para a função ``float()`` não se parece com um número.

A melhor maneira de resolver esse problema envolve o uso de mais uma comando de bloco de Python: o conjunto ``try/except`` (tentar/exceto). Esse par de palavras-chave formam o mecanismo de "tratamento de exceções" de Python, algo que só se encontra em linguagens bastante modernas como Java e as versões mais recentes de C++. A idéia básica é simples: no caso da nossa somadora, vamos tentar (``try``) converter a ''string'' digitada em ''float''; se isso não der certo, temos uma exceção, que deve ter tratamento especial. No nosso caso, vamos simplesmente acionar o comando ``break`` para interromper o ''loop'' e exibir a totalização.

Veja na listagem abaixo como fica a ``somadora3.py``, agora com tratamento de exceções.

.. literalinclude:: codigo/somadora3.py

Vamos comentar apenas as diferenças em relação à versão anterior:

Linha 4
  Mudamos a mensagem para o usuário, já que agora basta um ``[Enter]`` para encerrar.

Linha 7
  Início do bloco ``try``: tentaremos executar as linhas 8 e 9. Qualquer erro que ocorrer aqui será tratado no bloco except.

Linha 8
  Aqui é o local mais provável do erro, quando ``float()`` tenta converter o resultado de ``raw_input()``.

Linha 9
  Se ocorrer um erro na linha 8, a linha 9 não será executada porque, dentro do bloco try qualquer erro causa a transferência imediata da execução para o bloco except correspondente.

Linha 10
  Início do bloco ``except`` associado ao bloco ``try`` da linha 7

Linha 11
  Tratamento do erro: em caso de exceção, vamos simplesmente interromper o loop com um comando ``break``.

Linha 12
  Como esta linha vem logo após um loop infinito (``while True``), a única forma de chegarmos aqui é através de um ``break``. Ou seja, nesse caso o loop só termina em conseqüência de uma exceção.

Experimente o programa agora: ele ficou muito mais conveniente de usar. Para interromper a soma e obter o total, basta teclar [Enter] em uma linha em branco. Uma boa melhoria na "usabilidade" da somadora!

Como tratar um erro de verdade
===============================

A terceira versão da nossa somadora ainda não chegou lá: tratamos da mesma forma a situação em que usuário não digitou nada e aquela onde ele digitou algo que não é um número válido em Python. Pode ser que o usuário seja um datilógrafo à moda antiga, que digita L minúsculo no lugar do dígito 1. Ou ainda alguém que quer usar, com toda razão, a "," como separador decimal (Python só aceita números com ponto decimal). Para diferenciar um tipo de erro do outro, e saber quando o usuário apenas quer encerrar o programa, precisamos guardar a linha que ele digitou antes de tentar transformá-la em um número. Veja como na listagem abaixo:

.. literalinclude:: codigo/somadora4.py
    :linenos:

Vamos analisar as novidades dessa versão:

Linha 8
  A nova variavel ``linha`` armazena a linha digitada pelo usuário, para verificação posterior.

Linha 9
  A linha é convertida em número.

Linha 11
  Início do bloco que tratará os erros, provavelmente ocorridos na linha 9.

Linha 12
  A função ``len()`` retorna o número de itens de uma seqüência; nesse caso, o número de caracteres da ''string'' ``linha``. Se o número é igual a zero, então a string está vazia.

Linha 13
  No caso da ''string'' vazia, executamos um ``break`` porque o usuário não quer mais digitar.

Linha 14
  O operador ''in'' (em) retorna verdadeiro se o item à esquerda for encontrado na seqüência à direita; nesse caso verificamos se existe uma vírgula dentro da ''string'' ``linha``.

Linha 15
  Como encontramos uma vírgula, vamos supor que o usuário tentou digitar um número fracionário. Então vamos sugerir que ele use o ponto decimal. Nesse caso, não executamos o ``break``. Nenhum outro comando no bloco if/elif/else será executado, e o loop recomeçará de novo a partir da linha 6.

Linhas 16 e 17
  Aqui vamos tratar todos os demais casos, dizendo que o que foi digitado não se parece com um número. Novamente, sem o ``break``, o ''loop'' reiniciará, e logo o sinal ':' aparecerá na tela aguardando nova digitação.

Associação de nomes a valores
==============================

Voltemos ao problema do cálculo de despesas. Nossa meta é fazer um programa que seja capaz de calcular a partilha de gastos de qualquer grupo de pessoas, e não apenas de Ana e Bia. Para isso, vamos precisar associar o nome das pessoas aos seus respectivos gastos. A linguagem Python possui uma estrutura de dados ideal para essa aplicação. É o dicionário, conhecido pelos programadores Perl como ''hash'' ou associação. Como ocorre em Perl, em Python o dicionário serve para associar chaves a valores. O mais comum é que as chaves sejam ''strings'', como no nosso caso, onde as chaves serão nomes de pessoas. Mas as chaves podem ser qualquer tipo de objeto.

Em Python o dicionário é bem mais poderoso que em Perl, pois seus valores podem conter qualquer tipo de objeto como listas e até mesmo outros dicionários. Para entender rapidamente o funcionamento de um dicionário, nada melhor que experimentar com o interpretador interativo IDLE. Faça os seguintes testes, que explicaremos a seguir, com a abaixo::

  Python (#0, Apr 13 1999, 10:51:12) [MSC 32 bit (Intel)] on win32
  Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam
  >>> dic = {}
  >>> dic['ze'] = 300
  >>> dic['mauricio'] = 100
  >>> dic['heloisa'] = 150
  >>> dic['ze']
  300
  >>> dic
  {'mauricio': 100, 'ze': 300, 'heloisa': 150}
  >>> dic['ze'] = 200
  >>> dic
  {'mauricio': 100, 'ze': 200, 'heloisa': 150}
  >>> dic.keys()
  ['mauricio', 'ze', 'heloisa']
  >>> dic['paulo']
  Traceback (innermost last):
      File '', line 1, in ?
       dic['paulo']
  KeyError: paulo
  >>> dic.has_key('heloisa')
  True
  >>> dic.has_key('paulo')
  False
  >>>


Linha 3
  Antes de usar um dicionário, é preciso criá-lo. Nesse caso, criamos um dicionário vazio. As chaves {} são usadas para representar dicionários, como veremos novamente nas linhas 10 e 13.

Linhas 4, 5 e 6
  Criamos três itens no dicionário, usando as chaves 'ze', 'mauricio' e 'heloisa' e os valores 300, 100 e 150, respectivamente.

Linhas 7 e 8
  Aqui acessamos o valor associado à chave 'ze' e obtemos o número 300.

Linhas 9 e 10
  Agora acessamos o dicionário como um todo, e obtemos uma listagem entre chaves, com os itens separados por vírgula. Cada par de chave e valor aparece separado pelo sinal ':'. Note que a ordem dos itens não tem lógica aparente. Python não garante a ordem dos itens de um dicionário.

Linha 11
  Associamos um novo valor a uma chave existente. Num dicionário, todas as chaves são únicas. Não pode haver dois itens com a mesma chave 'ze'. Assim, essa operação muda o valor associado à esta chave.

Linhas 12 e 13
  Exibimos de novo o dicionário inteiro. Note que o valor associado à chave 'ze' mudou.

Linha 14
  O método ``keys()`` retorna a lista de chaves do dicionário. Um método nada mais é que uma função associada a um objeto, que deve ser invocada usando a sintaxe objeto.metodo(). Em nosso exemplo temos dic.keys().

Linha 15
  Aqui aparece a lista de chaves. Note que a lista, como sempre, vem delimitada por colchetes. O resultado do método ``keys()`` é uma lista de chaves, e não um dicionário.

Linhas 16 a 20
  Tentamos acessar o valor de uma chave inexistente. Python reclama com a mensagem ``KeyError: paulo``, indicando que o dicionário não possui uma chave igual a 'paulo'.

Linhas 21 a 24
  Para verificar se uma determinada chave existe, usamos o método has_key() (tem_chave). Os exemplos mostram que has_key() retorna 1 quando a chave existe, e zero quando ela não existe.

Resolvendo o Orçamento da República
====================================

Agora que conhecemos o funcionamento básico dos dicionários, podemos implementar o nosso aplicativo de acerto de contas, que pode ser muito útil por exemplo na administração de uma república de universitários. Antes de mais nada, vejamos como vai funcionar o programa::

  C:\PythonXX\Curso>python desprep1.py
  Balanco de despesas da Republica Recanto Suico

  (deixe um nome em branco para encerrar)

  Digite o nome da pessoa: Marcos
  Quanto gastou Marcos? 10
  Digite o nome da pessoa: Alexandre
  Quanto gastou Alexandre? 500
  Digite o nome da pessoa: Tyrone
  Quanto gastou Tyrone? 250
  Digite o nome da pessoa: Harley
  Quanto gastou Harley? 124,67
  Numero invalido.
  Quanto gastou Harley? 124.67
  Digite o nome da pessoa:

  Numero de pessoas: 4
  Total de gastos: R$ 884.67
  Gastos por pessoa: R$ 221.17

  Saldo de Marcos: -211.17
  Saldo de Alexandre: 278.83
  Saldo de Tyrone: 28.83
  Saldo de Harley: -96.50

  C:\PythonXX\Curso>


Linha 1
  Invocação do programa a partir da linha de comando.

Linhas 2 e 4
  Apresentação e instruções de uso.

Linha 6
  O programa pergunta o nome de uma pessoa.

Linha 7
  A seguir, solicita o valor dos gastos daquela pessoa.

Linhas 8 a 12
  O processo é repetido quantas vezes for necessário.

Linha 13
  O usuário digita um número com vírgula no lugar do ponto decimal.

Linha 14
  O programa informa que o numero é "inválido".

Linha 15
  Novamente o programa pede o valor gasto por Harley.

Linha 16
  O usuário não fornece outro nome, encerrando a digitação.

Linhas 18 a 20
  O número de pessoas, o total gasto e o gasto médio por pessoa são calculados.

Linhas 22 a 25
  Para cada pessoa, o programa exibe seu saldo. Aqueles que têm saldo negativo têm valores a pagar; os que de saldo positivo têm valores a receber.

Agora, vamos à listagem do programa ``desprep1.py``:

.. literalinclude:: codigo/desprep1.py
  :linenos:

Linhas 3 a 5
  Exibir identificação e instruções.

Linha 7
  A variável total é inicializada com o valor zero. Isso é necessário em função da linha 21.

Linha 8
  O dicionário de contas é criado, sem conteúdo. Ele armazenará as contas de cada pessoa.

Linha 9
  Início do loop principal.

Linha 10
  Solicitamos um nome e armazenamos na variável pessoa.

Linha 11
  Se a variável pessoa estiver vazia, nenhum nome foi digitado. Então executamos um break para deixar o loop principal, já que o usuário não quer mais fornecer nomes.

Linha 12
  Início do loop secundário, para digitação do valor numérico.

Linha 13
  Solicitamos o valor gasto pela pessoa em questão.

Linha 14
  Início do bloco ``try``, onde tentaremos converter a string digitada em número.

Linha 15
  A conversão fatídica. Em caso de erro aqui, o programa saltará para o bloco ``except``, na linha 17.

Linha 16
  Esse ``break`` só será executado se não ocorrer erro na linha 15. Sua função é interromper o loop secundário quando obtivermos um valor numérico.

Linhas 17 e 18
  O bloco ``except`` simplesmente exibe na tela a mensagem "Numero invalido". Aqui se encerra o loop secundário, que repetirá novamente a partir da linha 12, solicitando outro valor.

Linha 19
  O gasto obtido é armazenado no dicionário, usando o nome da pessoa como chave.

Linha 20
  O total de gastos é atualizado. Aqui é o final do loop principal. Daqui o programa voltará para a linha 9, e pedirá os dados da próxima pessoa.

Linha 22
  A função ``len()`` é usada para contar o número de itens no dicionário.

Linhas 23 a 25
  São exibidos o número de pessoas e total gasto. A notação ``%.2f`` faz com que os gastos apareçam com duas casas decimais, pois trata-se de um valor em dinheiro.

Linhas 26 a 27
  O gasto por cabeça é calculado e mostrado, também com duas casas decimais.

Linha 29
  Aqui começamos um loop for que será repetido para cada nome que constar na lista de chaves do dicionário. A lista de chaves é obtida através do método keys(). A variável nome apontará, sucessivamente, para cada nome encontrado nesta lista.

Linha 30
  Os valor gasto por uma pessoa é obtido acessando o dicionário com a expressão contas[nome]. Subtraímos o gasto médio para obter o saldo daquela pessoa.

Linha 31
  Exibimos o nome e o saldo da pessoa. Esta é a última linha do loop for, que percorrerá todas as chaves do dicionário.

Nossa primeira simulação
=========================

Agora já sabemos tudo o que precisávamos para implementar um jogo simples, como havíamos prometido no capítulo anterior. Trata-se de uma simulação de pouso lunar, em modo texto. Esse programinha é baseado em um jogo clássico escrito para calculadoras HP-25. Nossa versão é bem mais fácil de entender que o original para calculadora. Em vez de explicar linha por linha o funcionamento do programa, colocamos comentários abundantes na própria listagem, delimitados pelo sinal #. Lembre-se de que não é preciso digitar os comentários (e o programa inteiro pode ser simplesmente copiado aqui no site). Esse simulador de alunissagem é um game de recursos mínimos, mas ainda assim deve valer alguns minutos de diversão, especialmente se você curte a física newtoniana ensinada no colegial.

.. literalinclude:: codigo/desprep1.py

Como jogar
-----------

Seu objetivo é desacelerar a nave, queimando combustível na dosagem certa ao longo da queda, para tocar o solo lunar com uma velocidade bem próxima de zero. Se você quiser, pode usar um diagrama como o mostrado abaixo (colocamos em nosso site um desses em branco, para você imprimir e usar). As unidades estão no sistema inglês, como no original. O mais importante é você saber que cada 5 unidades de combustível queimadas anulam a aceleração da gravidade. Se queimar mais do que 5 unidades, você desacelera; menos do que 5, você ganha velocidade. Primeiro, pratique seus pousos preocupando-se apenas com a velocidade final. Depois você pode aumentar a dificuldade, estabelecendo um limite de tempo: por exemplo, o pouso tem que ocorrer em exatos 13 segundos. Uma última dica: cuidado para não queimar combustível cedo demais. Se você subir, vai acabar caindo de uma altura ainda maior! Boas alunissagens!
