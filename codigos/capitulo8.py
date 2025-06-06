# Comandos Condicionais (aprofundamento) - capítulo 8

# Comando mach-case
n = -1
while n != 0:
    n = int(input('Digite um inteiro: '))
    match n:
        case 1:
            print(' você digitou um')
        case 2:
            print(' você digitou dois')
        case 3:
            print(' você digitou três')
        case _:
            print(' você digitou outra coisa')
print('Fim do Programa')


# Comando if de Única Linha
X = 10
Y = 9
print(f'X é maior = {X}') if X >= Y else print(f'Y é maior = {Y}')
# o inline-if acima é o mesmo que isto:
if X >= Y:
    print(f'X é maior = {X}')
else:
    print(f'Y é maior = {Y}')

Y = 11 # alterando o valor de Y obtemos a execução do else
print(f'X é maior = {X}') if X >= Y else print(f'Y é maior = {Y}')


# Obrigatoriedade do Comando else
Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216]
Lista = []
print('Alternativa com if clássico')
for codigo in Codigos:
    if codigo >= 120 and codigo <= 200:
        Lista.append(codigo)
print(f' códigos filtrados -> {Lista}')

print('\nAlternativa com if de única linha')
Lista = []
for codigo in Codigos:
    Lista.append(codigo) if codigo >= 120 and codigo <= 200 else 0 # else 0 como valor neutro
print(f' códigos filtrados -> {Lista}')


# Retorno de Valor
X = int(input('Digite um inteiro: '))
paridade = 'par' if X % 2 == 0 else 'ímpar'
print(f'O valor {X} é {paridade}')
