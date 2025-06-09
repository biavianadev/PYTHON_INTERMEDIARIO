# Comandos Condicionais - capítulo 8

## Comando match-case

### Conceito Geral

O comando `match-case` é usado quando há necessidade de realizar **múltiplos testes** de forma clara e concisa. Ele compara o valor de uma **expressão** com diferentes valores definidos em cláusulas `case`, executando o bloco correspondente ao primeiro valor compatível.

### Estrutura Geral

```python
match <expressão>:
    case <valor1>:
        <bloco de comandos 1>
    case <valor2>:
        <bloco de comandos 2>
    ...
    case _:
        <bloco de comandos final>
```

### Características

* A **expressão** pode ser um objeto, uma expressão aritmética ou o retorno de uma função.
* As cláusulas `case` são **mutuamente exclusivas**: apenas o primeiro bloco correspondente é executado.
* A cláusula `case _` (underline) funciona como um **caso padrão**, executado quando nenhuma outra correspondência é encontrada.
* A **ordem das cláusulas** não é obrigatoriamente sequencial, mas a cláusula `case _` deve vir por último.

### Benefícios

* **Estrutura concisa**: substitui múltiplos `if-elif-else` com legibilidade.
* **Legibilidade**: sintaxe clara e fácil de compreender.
* **Segurança**: permite tratar todos os padrões possíveis.

### Integração com outros comandos

Pode ser combinado com:

* `if-elif-else`
* `while`
* `for`

## Comando if de única linha (inline if ou operador ternário)

### Conceito Geral

É uma forma compacta do comando `if-else`, usada quando há **apenas uma instrução** para cada caso (verdadeiro ou falso). Muito útil para tornar o código mais enxuto.

```python
<comando se verdadeiro> if <condição> else <comando se falso>
```

### Características

* **Somente um comando** pode ser usado em cada bloco (`if` e `else`).
* A cláusula `else` é **obrigatória**.
* Pode retornar valores diretamente, permitindo construções utilizando:

```python
<objeto> = <comando se verdadeiro> if <condição> else <comando se falso>
```

* Para casos onde o `else` não seria usado, pode-se incluir `else 0` como valor neutro.

----------------------------------------------
# Conjuntos - capítulo 9

## Classe set

A classe `set` permite a criação de **coleções de elementos únicos**, **não ordenados** e **mutáveis**, com restrições específicas quanto aos tipos de dados que podem ser armazenados.

### Características

* **Elementos únicos**: não permite duplicação de valores.
* **Elementos não ordenados**: a ordem é arbitrária e definida internamente pelo interpretador Python.
* **Mutável**: é possível adicionar ou remover elementos após a criação.
* **Elementos devem ser imutáveis**: apenas objetos **hashable** (com valor de hash fixo) podem ser inseridos.

## Criação de Conjuntos

```python
# Conjunto não vazio
c1 = {16, 8, 29}

# Conjunto vazio
c2 = set()

# set utilizando lista 
c3 = set([elementos da lista])

# set utilizando objeto
x = 'texto'
c4 = set(x)
```

* O uso de `{}` é válido apenas para conjuntos **não vazios**.
* Para criar conjuntos vazios, use obrigatoriamente `set()`.
* Pode-se utilizar o `set` para conjuntos não vazios, apenas adicionando um único argumento, através de um objeto, uma tupla ou lista.

## Conceitos: Hash e Hashable

* O **hash** é um número inteiro gerado a partir do conteúdo de um objeto.
* Objetos **imutáveis** possuem hash; objetos **mutáveis** (listas, dicionários) não possuem.
* A função `hash()` retorna o hash de um objeto, se aplicável.
* **Tuplas** têm hash; **listas** não.
* **Exemplo**: `26` e `26.0` têm o mesmo hash, então não coexistem em um mesmo conjunto.

### Relação entre Hash e Conjuntos

* Somente objetos **hashable** podem ser membros de conjuntos.
* A **unicidade** dos elementos em um conjunto é controlada pelo seu valor de hash.
* Objetos com o mesmo hash não podem aparecer duas vezes.

## Principais Métodos da Classe set

| Método             | Descrição                               |
| ------------------ | --------------------------------------- |
| `.add(x)`          | Adiciona o elemento `x` ao conjunto     |
| `.remove(x)`       | Remove `x`; erro se não existir         |
| `.discard(x)`      | Remove `x`; **sem erro** se não existir |
| `.clear()`         | Remove **todos** os elementos           |
| `.copy()`          | Retorna uma cópia rasa do conjunto      |
| `.union(s)`        | Retorna a união com o conjunto `s`      |
| `.intersection(s)` | Retorna a interseção com `s`            |
| `.difference(s)`   | Retorna a diferença com `s`             |
| `.issubset(s)`     | Verifica se é subconjunto de `s`        |
| `.issuperset(s)`   | Verifica se é superconjunto de `s`      |

---------------------------------------------
`STATUS: em andamento`
