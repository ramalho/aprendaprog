.. highlight:: python
   :linenothreshold: 5

==================================================
Capítulo 3: Do console para o editor de programas
==================================================

Depois de dois capítulos bem básicos, é hora de engatar uma segunda e começar a criar programas mais dignos desse nome. Não vamos desprezar o que fizemos até aqui, digitando diretamente na deixa do interpretador Python. Ao contrário: tenha sempre em mente que você pode usá-lo para esclarecer aquela dúvida rápida ou mesmo localizar um bug escondido em um sistema complexo. A maioria das outras linguagens não oferece um ambiente para execução imediata de comandos como o Python. Uma exceção famosa é a linguagem Logo, onde o interpretador interativo serve justamente para facilitar a aprendizagem da programação através da exploração e experimentos.

Mas a partir de agora vamos atacar programas mais extensos, e não vamos querer digitá-los linha por linha no modo interativo. Em vez disso, vamos escrever os comandos em um editor de textos, salvar o arquivo, e mandar o interpretador Python ler o programa salvo.

Rodando programas no IDLE
==========================

A versão Windows do Python traz o IDLE, um interpretador interativo em modo gráfico que já apresentamos no primeiro capítulo. Se você não usa essa versão do Python, vá direto para a próxima seção: Testando no sistema. O IDLE inclui um editor de programas simplório, mas útil para quem está aprendendo a linguagem. O editor do IDLE exibe com cores diferentes as palavras da linguagem, de acordo com sua função sintática (lembra da aula de português onde o verbo era verde, o sujeito vermelho etc?). Para abrir o editor, rode o IDLE e acione o comando ``File > New window``. A janela que se abrirá, com o título ``untitled``, é um editor. Experimente digitar um programinha como esse::

  for i in range(100):
      print 'Fulano ',
  print 'e seus Sicranos'

Note que o editor pinta algumas palavras de laranja. São as chamadas palavras-chave, peças tão importantes em Python como os verbos em português. Outras cores indicaom funções e variáveis. E os textos entre aspas aparecem em verde: dessa forma, fica difícil esquecer de fechar aspas. Outra coisa que acontece magicamente é a endentação. O editor "sabe" que após os ":" do comando for, deve vir um bloco endentado. Para encerrar o bloco endentado, você pode teclar ``[ENTER]`` duas vezes para pular uma linha, como ocorre também na deixa do interpretador, ou então teclar ``[BackSpace]`` para apagar de uma vez só os quatro espaços à esquerda da linha.

Uma vez digitado esse programinha você pode executá-lo de duas maneiras: diretamente de dentro do IDLE ou no console do sistema operacional. Para fazer o IDLE rodar o seu programa é só teclar ``[F5]``. Se você ainda não salvou o código do seu programa, o IDLE vai exibir uma mensagem pedindo para que você o faça. Basta usar o comando File > Save, ou melhor ainda, ``[CTRL]+[S]``. Se você não sabe onde salvar, sugiro que crie uma pasta chamada Curso dentro da pasta onde está o seu interpretador Python e salve ali (provavelmente a pasta ficará sendo ``C:\Python25\Curso``, no caso do Python 2.5). Assim fica fácil encontrá-lo depois. Use o nome ``egotrip.py``.

O programinha ``egotrip.py`` faz o nome do autor aparecer 100 vezes, seguinda do nome de sua banda. No tempo dos computadores de 8 bits, programinhas como esse eram invariavelmente os primeiros exercícios de qualquer estudante de programação. No IDLE, a "saída" do programa (aquilo que ele exibe ao rodar), aparece dentro de uma janela intitulada ``Python Shell``. Você pode fechar essa janela quando o programa parar.

Você talvez tenha notado que o programa é meio lento. Em meu velho ''notebook'' Pentium 133 o programa levava 10 segundos para escrever as 101 linhas. É muito. Mas a culpa não é do Python, e sim do IDLE, como veremos a seguir.

Navegando pela linha de comando
================================

No Linux a linha de comando está em toda parte, mas no Windows fica um pouco escondida. Para encontrá-la, clique na barra de tarefas do Windows XP em ``Iniciar > Executar...``. Na janelinha que se abre, digite apenas ``cmd``. Isso executa o interpretador de comandos do Windows, equivalente ao velho MS-DOS nos Windows mais antigos. Para quem nunca navegou pelo sistema via prompt, eis aqui o mínimo que você precisa saber. Veja o que aparece na janela do Prompt:

À esquerda do cursor, você tem a informação mais importante para se orientar: a letra do drive e o nome da pasta onde você se encontra. Se o seu Windows está com a configuração de fábrica, você estará em ``C:\Windows``. O sinal > é apenas a deixa do sistema, equivalente ao ``>>>`` usado pelo Python para indicar que está pronto para receber um comando. Antes de mais nada, vamos acionar um programinha que nos poupará muita digitação posteriormente.

Agora, vamos ver o que existe na pasta onde estamos (a pasta Windows). Digite::

  C:\Windows>dir [ENTER]

Você verá uma longa listagem de arquivos, com seus nomes abreviados, extensões, tamanhos, datas e nomes longos. Em meu ''notebook'' aparecem 236 arquivos na pasta Windows. Não estamos interessados neles agora, o objetivo era apenas mostrar que o comando dir produz uma listagem dos arquivos da pasta, ou diretório, atual.

Agora vamos navegar até o diretório onde foi gravado o programa ``egotrip.py``. Digite::

  C:\Windows>cd \ [ENTER]

Agora você está no chamado diretório raiz do seu disco. Digite ``dir`` e veja como a maioria dos itens dentro dessa pasta são outras pastas, como a própria pasta Windows. Agora vamos entrar na pasta do Python::

  C:\>cd pythonXX [ENTER]

E, em seguida, na pasta Curso, que você deve ter criado quando salvou o arquivo ``egotrip.py``.

::

  C:\PythonXX>cd curso
  C:\PythonXX\Curso>dir

Você deverá ver uma listagem como essa::

  O volume da unidade C é XXX
  O número de série do volume é XXXX-XXXX
  Pasta de C:\PythonXX\Curso

  .              <DIR>        25/10/99  20:57 .
  ..             <DIR>        25/10/99  20:57 ..
  EGOTRIP  PY             89  25/10/99  20:32 egotrip.py
           1 arquivo(s)             89  bytes
           2 pasta(s)      21.331.968  bytes disponíveis

  C:\PythonXX\Curso>

Agora você está no ponto certo para digitar o comando que causará a execução do seu programa ``egotrip.py``.

Testando no sistema
====================

Meu ambiente favorito para rodar programas em Python é a própria linha de comando do sistema operacional. Não costumo usar o editor do IDLE, mas sim o NotePad++, um excelente editor de textos livre e gratuito para Windows. Seja qual for o editor que você usa, o importante é salvar o arquivo como texto puro, sem marcas de formatação. O Notepad é melhor que Word para esse fim, mas o NotePad++ é muito melhor. No Linux, Gedit, Kate, Pico, Vi e Emacs são alguns editores de texto puro bastante comuns. Entre esses, prefiro Gedit e Kate, que têm interfaces mais modernas. Uma vez digitado e salvo o arquivo, você precisa executá-lo a partir da linha de comando do seu sistema.

Quem usa Linux ou já está habituado ao DOS, pode seguir até a próxima seção, ASCII art.

ASCII art
==========

No Windows, para executar o programa, digite esse encantamento (supondo que você fez tudo conforme descrito na seção acima, ou fez tudo diferente mas sabia o que estava fazendo)::

  C:\PythonXX\Curso>..\python egotrip.py

Os sinais ``..\`` na frente do comando python servem para dizer ao DOS para executar um programa que está no diretório anterior no caminho atual. Assim, acionamos o programa ``python.exe`` que está na pasta ``C:\PythonXX``.

No Linux, você precisará chegar até o diretório que contém o exemplo, e digitar::

  $ python egotrip.py

Ou, se isso não funcionar, tente algo como segue (o comando exato vai depender da sua instalação)::

  $ /usr/local/bin/python egotrip.py
  $ /usr/bin/python egtrip.py

Bom, deu trabalho mas chegamos. E como você deve ter notado, a execução do programinha foi bem mais veloz que no IDLE (em meu computador, menos de 1 segundo, em vez de 10).

Agora vamos fazer uma pequena mudança no programa egotrip que terá um grande efeito. Para fazer essa alteração, no Windows o modo mais rápido é segurar a tecla ``[ALT]`` e pressionar ``[TAB]`` até que o ícone do editor do IDLE identificado pelo nome do arquivo ``egotrip.py`` esteja selecionado. Então solte a tecla ``[ALT]``, que o editor aparecerá sobrepondo-se às demais janelas. Agora vamos modificar o programa egotrip. Ao final da segunda linha, digite uma vírgula. O seu programa deverá ficar assim::

  for i in range(100):
      print 'Luciano ',
  print 'e seus Camargos'

Salve com ``[CTRL]+[S]`` e rode o programa novamente. Tecle ``[F5]`` para rodar no IDLE, ou siga esses passos para testar no DOS:

   * ``[ALT]+[TAB]`` até voltar ao ''prompt'' do DOS
   * ``[↑]`` (seta para cima) para repetir o comando ``..\python egotrip.py``
   * ``[ENTER]`` para executar o comando.

10 entre 10 programadores que usam a plataforma Windows têm muita prática com a sequência ``[ALT]+[TAB]``, ``[↑]``, ``[ENTER]``. Logo, logo, em sua primeira sessão de caça a um bug, você terá oportunidade de praticar bastante.

Nesse caso, é interessante testar o programa tanto no IDLE quanto na linha de comando. Você verá que os resultados são bem diferentes. Experimente e tente explicar porquê.

Como exercício final, substitua o argumento 100 da função range pelo número 1000, e rode o programa novamente (não recomendo usar o ``[F5]`` do IDLE dessa vez; será bem demorado). Tente acrescentar ou retirar letras dos nomes. O efeito será diferente. Bem vindo ao mundo da expressão artística com caracteres de computador.

Seu primeiro programa interativo
=================================

Até agora, todos os programas que mostramos não são interativos, ou seja, uma vez rodando, eles não aceitam a entrada de dados de um usuário ou do sistema. Programas não interativos são usados em muitas situações comuns. O programa que emite os cheques da folha de pagamentos de uma grande empresa provavelmente não é interativo, mas recebe todos os dados necessários em um único lote, antes de sua execução. Mas os programas mais interessantes, como um processador de textos, um ''game'' ou o piloto automático de um avião são todos interativos. Esse é o tipo de programa que passaremos a desenvolver agora.

Nosso passeio pela ASCII art não teve apenas objetivos estéticos. Quisemos mostrar como rodar um programa em Python a partir da linha de comando porque, a partir de agora, vamos usar um comando da linguagem Python que não funciona na atual versão do IDLE. O comando chama-se ``raw_input``, e sua função é receber uma entrada de dados do usuário (input quer dizer entrada de dados; cuidado porque você deve ter sido condicionado a acreditar que "antes de P e B sempre vem a letra M", mas input é inglês, e se escreve com N mesmo; eu perdi uma hora com isso quando aprendia BASIC).

Vejamos um primeiro exemplo. Observe que não estamos acentuando o texto no programa porque o DOS não reproduz corretamente os acentos do Windows, e precisamos do DOS para testar esse programa. Deve haver uma forma de convencer o DOS a exibir os acentos corretos do Windows, mas ainda não descobrimos como.

De qualquer forma, isso não quer dizer que não dá para fazer programas com acentuação correta em Python; quando aprendermos a criar softwares gráficos esse problema desaparecerá.

Digite o programinha abaixo, salve como ``despdom1.py`` e execute na linha de comando.

.. todo:: Mostrar como usar encoding para fazer mensagens acentuadas

::

  # despdom1.py - Calculadora de despesas domesticas

  print 'Balanco de despesas domesticas'
  ana = raw_input('Quanto gastou Ana? ')
  bia = raw_input('Quanto gastou Bia? ')
  total = float(ana) + float(bia)
  print 'Total de gastos = R$ %s.' % total
  media = total/2
  print 'Gastos por pessoa = R$ %s.' % media

Os números que aparecem à esquerda na listagem acima não fazem parte do programa e não devem ser digitados. Eles estão aí para facilitar a explicação que vem logo a seguir.

Antes de esmiuçar o programa, vale a pena executá-lo para ver o que acontece. Você será solicitado a digitar um valor para Ana e outro para Bia. Note que os valores deverão ser apenas números. Se quiser usar centavos, use o ponto decimal em vez de vírgula, como já vínhamos fazendo antes. E nada de $ ou R$. Vejamos um exemplo de execução::

  C:\PythonXX\Curso>..\python despdom1.py
  Balanco de despesas domesticas

  Quanto gastou Ana? 10
  Quanto gastou Bia? 20
  Total de gastos = 30.0
  Gastos por pessoa = 15.0

  C:\PythonXX\Curso>

Dissecando o código
====================

Agora vamos acompanhar, linha por linha, como o interpretador executou o programa. Essa é a atividade mais importante para desenvolver você como programador ou programadora. Você precisa aprender a ler um programa e simular mentalmente que acontece dentro do computador. "Quando você aprender a se colocar no lugar do computador ao ler um programa, estará pronto, Gafanhoto".

Linha 1
  O sinal # indica comentário. Tudo o que aparece em uma linha a partir desse sinal é ignorado pelo interpretador Python. Neste caso, o comentário explica para nós, humanos, o propósito do programa. Note que o comentário não aparece para o usuário final quando o programa é executado. Comentários servem apenas para ser lidos por outros programadores.

Linha 3
  O velho comando ``print`` é usado para escrever o título "Balanco de despesas domesticas" na tela do usuário.

Linha 4
   O comando ``raw_input`` exibe a pergunta "Quanto gastou Ana?", aguarda uma resposta e armazena na varíavel ana.

Linha 5
   O mesmo comando é usado para guardar os gastos de Bia na variável bia.
   
Linha 6
  Aqui é calculado o total. Note o uso da função ''float''. Acontece que a função ``raw_input`` não retorna números, e sim ''strings''. Como vimos no capítulo anterior, o operador "+" tem efeitos diferentes quando aplicado a ''strings''; em vez de somar, ele concatena ou junta os textos. Nesse caso, se ana é 10 e bia é 20, ana + bia seria 1020. Para realizar a soma, precisamos antes transformar as ''strings'' em números, o que é feito pela funções ''float'' ou ''int''. Nesse caso, usamos float porque não vamos nos limitar a aceitar números inteiros.

Linha 7
  O total é exibido, com o auxílio do operador % que insere o valor na posição assinalada pelos caracteres %s dentro da mensagem. O código %s faz com que Python transforme o número em ''string''.

Linha 8
  Cálculo da média. Como ambos os valores são float, o resultado será preciso (se fossem inteiros, o resultado também seria forçado a ser inteiro, o que nesse caso levaria a erros do tipo).

Linha 9
  Mostramos a média, usando a mesma técnica da linha 7.

Experimente rodar o programa algumas vezes. Note que não é um programa muito robusto: se você não digitar coisa alguma e teclar [ENTER] após uma das perguntas, ou responder com letras em vez de números, o programa "quebra". No próximo capítulo aprenderemos a lidar com entradas inesperadas.

Um programa mais esperto
=========================

O programa acima é quase útil. Ele calcula a despesa total e a média, mas não responde à pergunta fundamental: quanto Ana tem que pagar a Bia, ou vice-versa? A aritmética envolvida é simples: se Ana gastou menos, ela precisa pagar a Bia um valor igual à diferença entre o que gastou e a média. Gostaríamos que nosso programa funcionasse assim::

  Balanco de despesas domesticas

  Quanto gastou Ana? 10
  Quanto gastou Bia? 20
  Total de gastos: R$ 30.0
  Gastos por pessoa: R$ 15.0
  Ana deve pagar: R$ 5.0

Utilize o comando ``File > Save As...`` para salvar o programa ``despdom1.py`` como ``despdom2.py``. Agora vamos modificá-lo para fazer o que queremos. Abaixo, o programa final, e a seguir, a explicação de cada mudança que foi feita.

::

  # despdom2.py - Calculadora de despesas domesticas - versao 2

  print 'Balanco de despesas domesticas'
  ana = float(raw_input('Quanto gastou Ana? '))
  bia = float(raw_input('Quanto gastou Bia? '))
  print
  total = ana + bia
  print 'Total de gastos: R$ %s' % total
  media = total/2
  print 'Gastos por pessoa: R$ %s' % media
  if ana < media:
      diferenca = media - ana
      print 'Ana deve pagar: R$ %s' %diferenca
  else:
      diferenca = media - bia
      print 'Bia deve pagar: R$ %s' % diferenca

O que mudou:

Linha 1
  Acrescentamos "versao 2" ao comentário

Linhas 4 e 5
  Aqui fazemos a conversão dos resultados de raw_input para float imediatamente, de modo que os valores armazenados na variáveis ana e bia são números, e não ''strings'' como antes.

Linha 6
  Uma mudança cosmética apenas: acrescentamos uma linha com apenas um print, para deixar na tela uma linha em branco entre as perguntas e os resultados.

Linhas 7
  Agora podemos simplesmente somar os valores de ana e bia, que já foram convertidos para float nas linhas 4 e 5.

Linhas 8 a 10
  Exibimos o total e processamos a média, como antes.

Linha 11
  Apresentamos um novo comando de bloco, o comando ``if``, que pode ser traduzido exatamente como "se". Essa linha diz, literalmente: "se ana < media:". Ou seja, se o valor de Ana for menor que o valor da média, execute o bloco endentado a seguir (linhas 12 e 13). Caso contrário, não execute essas linhas, e passe direto para a linha 14.

Linhas 12 e 13
  Calculamos e exibimos quanto Ana deve pagar.

Linha 14
  Aqui vemos outro comando de bloco, o ``else``, que pode ser traduzido como "senão". O ``else`` só pode existir após um bloco iniciado por ``if``. O bloco que segue o ``else`` só é executado quando a condição prevista no ``if`` não ocorre. Isso significa que, quando temos um bloco ``if`` e um bloco ``else``, é garantido que apenas um dos dois será executado. Nesse caso, as linhas 15 e 16 só serão executadas se o valor de ``ana`` não for menor que a média.

Linhas 15 e 16
  Calculamos e exibimos quanto Bia deve pagar.

Experimente um pouco com o programa ``despdom2.py``. O que acontece quando os gastos de Ana e Bia são iguais? Tente responder essa pergunta sem rodar o programa. A chave está na linha 11. Qual é a média quando os gastos são iguais? Tente simular mentalmente o comportamento do computador na execução passo a passo do programa. Dedique alguns minutos a esse desafio, e só então rode o programa com valores iguais para ver se acontece o que você imaginou.

Tudo sobre o ``if``
===================

O comando ``if``, que acabamos de conhecer através de um exemplo, é uma peça fundamental da linguagem Python, e de quase todas as linguagens de programação existentes. Sua função é descrita como "comando de execução condicional de bloco", ou seja, é um comando que determina a execução ou não de um bloco de comandos, de acordo com uma condição lógica. No exemplo, a condição lógica é ``ana < media``. O operador < serve para comparar dois números e determinar se o primeiro é menor que o segundo (ele também funciona com ''strings'', mas aí a comparação segue uma regra parecida com a ordem usada dos dicionários). Os operadores de comparação de Python são os mesmos usados em Java e C++:

======== ================ ==========
Operador Descrição        Exemplo
======== ================ ==========
==       igual a          ``a == b``
!=       diferente de     ``a != b``
<        menor que        ``a < b``
>        maior que        ``a > b``
>=       maior ou igual a ``a >= b``
<=       menor ou igual a ``a <= b``
======== ================ ==========

Para sentir o funcionamento desses operadores, abra o interpretador interativo do Python e digite esses testes (não vamos mostrar os resultados aqui; faça você mesmo).

.. highlight:: python
   :linenothreshold: 500

::

  >>> a = 1
  >>> b = 2
  >>> a == 1
  >>> a == 2
  >>> a == b
  >>> 2 == b
  >>> a != b
  >>> a != 1
  >>> a < b
  >>> a >= b

As linhas 1 e 2 não produzem nenhum resultado, como já vimos antes. Elas apenas atribuem valor às variáveis a e b. A linha 3 parece um pouco com a linha 1, mas significa algo completamente diferente. Aqui não acontece nenhuma atribuição, apenas uma comparação, que vai gerar um resultado. Um erro bastante comum cometido por quem está aprendendo Python, C ou Java é usar = no lugar de == ao fazer uma comparação (em Basic, por exemplo, o = é usado nos dois casos). Após cada as linhas a partir da linha 3, o interpretador mostrará um número 1 ou 0, para indicar que a comparação é verdadeira (1) ou falsa (0).

Voltando ao comando ``if``, não existe nenhuma lei que obrigue a presença de um operador de comparação na condição do ``if``. A única coisa que interessa é que a expressão que estiver no lugar da condição será considerada falsa se for igual a 0 (zero), uma ''string'' vazia, uma lista vazia ou o valor especial ``None``, sobre o qual voltaremos a falar depois. Qualquer valor que não seja um desses será considerado "verdadeiro", e provocará a execução do bloco subordinado ao ``if``. É por isso que os operadores de comparação retornam 0 ou 1 para representar falso ou verdadeiro.

Não é obrigatória a presença de um bloco ``else`` após um ``if``. Mas um ``else`` só pode existir após um ``if``. E um ``if`` pode conter, no máximo, um ``else``. Existe um terceiro comando de bloco relacionado a esses, chamado ``elif``. Ele corresponde à combinação ``else-if`` existente em outras linguagens. Assim como o ``if``, cada ``elif`` deve ser acompanhado de uma condição que determinará a execução do bloco subordinado. Como todo comando de bloco, a primeira linha do ``elif`` deve ser terminada por um sinal de ``:``.

Um ``if`` pode ser seguido de qualquer quantidade de blocos ``elif``, e se houver um bloco ``else`` ele deverá vir depois de todos os ``elif``. Veja esse fragmento de código, parte de um jogo simples que criaremos no próximo capítulo::

  if vf == 0:
      print 'Alunissagem perfeita!'
  elif vf <= 2:
      print 'Alunissagem dentro do padrao.'
  elif vf <= 10:
      print 'Alunissagem com avarias leves.'
  elif vf <= 20:
      print 'Alunissagem com avarias severas.'
  else:
      print 'Modulo lunar destruido no impacto.'

Numa sequencia de ``if/elif/elif/.../else`` é garantido que um, e apenas um dos blocos será executado. Fica como desafio para o leitor descobrir como usar o comando elif para corrigir o bug dos gastos iguais, que aparece no programa ``despdom2.py``.
