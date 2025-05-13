# importei o modulo tools que e outro arquivo python que contem as funcoes e chamei ele de t
import tools as t

# criei a variavel opE e fiz ela ser o t.inicio()
opE = t.inicio()

# se o opE for igual a +
if opE == "+":

    # chamei a funcao somar
    t.somar()

# se o opE for igual a -
elif opE == "-":

    # chamei a funcao subtrair
    t.subtrair()

# se o opE for igual a *
elif opE == "*":

    # chamei a funcao multiplicar
    t.multiplicar()

# se o opE for igual a /
elif opE == "/":

    # chamei a funcao dividir
    t.dividir()

# se nao for nenhuma das opcoes acima
else:

    # printar opcao invalida
    print("Operação Invalida!")

# feito por OreDev :D