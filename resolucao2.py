valores = input().split() #Utilizando a função split para dividir o conteúdo da variável de acordo com as condições especificadas 

# TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
h = int(valores[0])
p = int(valores[1])

media = h/p 

print(f"{media: .2f}")
