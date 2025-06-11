# Conjuntos - capítulo 9

# Criação de Conjuntos
# Criação de um conjunto não-vazio usando o par de chaves {}
c1 = {16, 8, 29}
type(c1) # verificação do que foi criado, é conjunto
len(c1)
print(c1)

# Criação de um conjunto vazio usando o construtor da classe set()
c2 = set()
type(c2) # verificação do que foi criado, é conjunto

# Tentativa de criação de um conjunto vazio usando o par de chaves {}
c3 = {}
type(c3) # o uso das chaves dessa forma cria um dicionário

# Criação de um conjunto não-vazio usando o construtor da classe set()
c4 = set((23, 9, 41))
type(c4) # verificação do que foi criado, é conjunto

# Criação do conjunto a partir de string
texto = 'texto qualquer'
c = set(texto)
print(c) # observe que não há caracteres repetidos no conjunto

# Criação do conjunto a partir de tupla
tupla = (14, 26, 33, 45, 50)
c = set(tupla)
print(c)

# Criação do conjunto a partir de lista
lista = (26, 15, 49, 65, 49)
c = set(lista)
print(c)

# Criação do conjunto a partir de outro conjunto
c2 = set(c)
print(c)

# Criação do conjunto a partir de um dicionário
d = {'1235': 49, '1476': 32, '1329': 36}
c = set(d)
print(c)


# Hash e Hashable
s1 = 'texto'
hash(s1)
s2 = 'qualquer coisa'
hash(s2)
valor = 13.75
hash(valor)
x = 26
hash(x)
y = 26.0
hash(y)
t = (15, 23, 7)
hash(t)
l = [15, 23, 7]
hash(l) # mensagem de erro por se tratar de uma lista (obj mutável)


# Operações com Conjuntos
A = set('ANTONIO CARLOS')
print(A)
B = set('JOSÉ CARLOS')
print(B)
print(A - B) # Diferença - elementos em A que não estão em B
print(B - A) # Diferença - elementos em B que não estão em A
print(A | B) # União
print(A & B) # Interseção
print(A ^ B) # Diferença Simétrica
# Pertencimento
print('X' in A)
print('T' in A)
# Não Pertencimento
print('X' not in A)
print('T' not in A)


# Conjuntos Usados como Iteradores
print("primeira execução")
conjunto = {3.3, 18.6, 34.0, 43.1, 58.7}
for c in conjunto:
    print(c)

print("\nsegunda execução")
conjunto = {18.6, 3.3, 58.7, 34.0, 43.1}
for c in conjunto:
    print(c)
print('Fim do Programa')


# frozenset
A = frozenset('ANTONIO CARLOS')
print(A)
B = frozenset('JOSÉ CARLOS')
print(B)
print(A - B)
print(B - A)
print(A | B)
print(A & B)
print(A ^ B)
print('X' in A)
print('T' in A)
print('X' not in A)
print('T' not in A)
