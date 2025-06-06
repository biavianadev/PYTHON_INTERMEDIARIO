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
`STATUS: em andamento`
