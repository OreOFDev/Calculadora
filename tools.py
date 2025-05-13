# criei a funcao inicio
def inicio():

    # printei as operações
    print("+, -, *, /")

    # criei a variavel opE e fiz ela ser o input da operação
    opE = input("Digite a operação que voce deseja: ")

    # retornei o opE para usar ele depois
    return opE

# criei a funcao n1_n2
def n1_n2():

    # criei a variavel n1 que e um input do numero
    n1 = input("Digite o primeiro número: ")

    # criei a variavel n2 que e um input do numero
    n2 = input("Digite o segundo número: ")

    # tente
    try:

        # transformei n1 e n2 em float
        n1 = float(n1)
        n2 = float(n2)

        # retornei n1 e n2
        return n1, n2
    
    # se der erro de valor
    except ValueError:

        # printei o erro
        print("Número inválido!")

        # retornei nada
        return None, None

# criei a funcao somar
def somar():

    # printei
    print("Somar Escolhido!")

    # n1,n2 e igual o retorno da funcao n1_n2
    n1, n2 = n1_n2()

    # se n1 e n2 nao forem nulos
    if n1 is not None and n2 is not None:

        # printei n1 + n2
        print(n1 + n2)

# criei a funcao subtrair
def subtrair():

    # printei
    print("Subtrair Escolhido!")

    # n1,n2 e igual o retorno da funcao n1_n2
    n1, n2 = n1_n2()

    # se n1 e n2 nao forem nulos
    if n1 is not None and n2 is not None:

        # printei n1 - n2
        print(n1 - n2)

# criei a funcao multiplicar
def multiplicar():

    # printei
    print("Multiplicar Escolhido!")

    # n1,n2 e igual o retorno da funcao n1_n2
    n1, n2 = n1_n2()

    # se n1 e n2 nao forem nulos
    if n1 is not None and n2 is not None:

        # printei n1 * n2
        print(n1 * n2)

# criei a funcao dividir
def dividir():
    
    # printei
    print("Dividir Escolhido!")

    # n1,n2 e igual o retorno da funcao n1_n2
    n1, n2 = n1_n2()

    # se n1 e n2 nao forem nulos
    if n1 is not None and n2 is not None:

        # printei n1 / n2
        print(n1 / n2)
# feito por OreDev :D