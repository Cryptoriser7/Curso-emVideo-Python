# Tratamento de strings
'''frase = 'Curso em Video Python'

Se escrever: frase[9] - o programa vai identificar o caracter nr 9, neste caso, a letra 'V' de Video.
Se escrever: frase[9:13] - o programa vai pegar as letras desde a 9º até á 12º, uma vez que o programa exclui o ultimo caracter na lista pedida
se escever: frase[9:21:2] - o prpgrama vai selecionar os caracteres desde 9 ate 20, saltando de dois em dois
Se escrever: frase[:5] - o programa vai selecionar desde o inicio até ao 5º caracter
Se escrever: frase [15:] - o programa vai selecionar desde o 15º caracter até ao fim
Se escrever: frase[9::3] - o programa vai começar no 9º, vai até ao fim e a saltar de 3 em 3 letras

Para saber quantos caracteres tem uma frase utiliza-se len(frase)
Para contar determinados caracteres utiliza-se a formula: frase.count('letra')
Para contar determinados caracteres dentro de um determinado espaço utiliza-se a forma: frase.count('letra',0,13) sendo 0 e 13 o espaço exemplo.
Para encontrar palavras uza-se: frase.find('palavra').
Quando colocamos uma string que nao existe dentro do find(), o programa devolve a mensagem: -1
Para verificar dse existem determinadas palavras na string, usa-se 'palavra' in frase

Transformação:
frase.replace(x,y) permite substituir palavras nas strings
frase.upper() Coloca toda a string em maiusculas
frase.lower() Coloca toda a string em minusculas
frase.capitalize() Coloca apenas o primeiro caracter da string em maiuscula
frase.title() Coloca todas as palavras a começar em maiuscula

frase.strip() Remove todos os espaços inuteis antes e depois da string
frase.rstrip() Remove todos os espaços inuteis DEPOIS da string
frase.lstrip() Remove todos os espaços inuteis ANTES da string

Divisão:
frase.split() Divide a string numa lista, onde cada elemento é separado pelo seu delimitador padrao
que neste caso é o espaço
'-'.joint(frase) Une todos os elementos separados pelo split, e utiliza o - como divisão entre as palavras
'''

frase = '   Curso em Video Python    '
#print(len(frase.strip()))

dividido = frase.split()
print(dividido[0])
