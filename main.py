# aqui eu crio a variavel calculadora que e um ascii de calculadora 
calculadora = """
 _____________________
|  _________________  |
| |   1234567890   | | 
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|


"""
# aqui eu printo a calculadora
print(calculadora)

# print de bem vindo
print("Bem vindo a calculadora")

# aqui eu crio a funcao de mostrar o menu meio inutil kk
def mostrarMenu():

    # aqui cria o menu
    menu = """
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    5 - Avaliar
    0 - Sair
    """

    # aqui printa o menu
    print(menu)

# loop infinito pq sim
while True:

    # mostrar o menu aqui
    mostrarMenu()

    # aqui a pessoa escolha uma opcao do menu e guarda na variavel op / op = opcao escolhida
    op = input("Escolha uma opcao do menu: ")

    # aqui se o op for um numero inteiro executar
    if op.isdigit():

        # se for um numero virar int
        op = int(op)

        # se for 1 entao e somar
        if op == 1:

            # a pessoa digita 2 numeros para somar
            numero1 = input("Digite o primeiro numero que quer somar: ")
            numero2 = input("Digite o segundo numero que quer somar: ")

            # aqui e se e decimal / float se e eu somo se nao printa um erro
            if numero1.isdecimal() and numero2.isdecimal():
                numero1 = float(numero1)
                numero2 = float(numero2)
                total = numero1 + numero2

                # aqui printa o resultado
                print(f"O seu resultado deu: {total}")

            # se nao for decimal
            else:

                # print de erro
                print("Digite um numero decimal / float!")


        # se for 2 entao e subtrair
        elif op == 2:

            # a pessoa digita 2 numeros para subtrair
            numero1 = input("Digite o primeiro numero que quer subtrair: ")
            numero2 = input("Digite o segundo numero que quer subtrair: ")

            # aqui e se e decimal / float se e eu subtraio se nao printa um erro
            if numero1.isdecimal() and numero2.isdecimal():
                numero1 = float(numero1)
                numero2 = float(numero2)
                total = numero1 - numero2

                # aqui printa o resultado
                print(f"O seu resultado deu: {total}")


            # se nao for decimal
            else:
                # print de erro
                print("Digite um numero decimal / float!")


        # se for 3 entao e multiplicar
        elif op == 3:

            # a pessoa digita 2 numeros para multiplicar
            numero1 = input("Digite o primeiro numero que quer multiplicar: ")
            numero2 = input("Digite o segundo numero que quer multiplicar: ")

            # aqui e se e decimal / float se e eu multiplico se nao printa um erro
            if numero1.isdecimal() and numero2.isdecimal():
                numero1 = float(numero1)
                numero2 = float(numero2)
                total = numero1 * numero2
                # aqui printa o resultado
                print(f"O seu resultado deu: {total}")

            # se nao for decimal
            else:
                # print de erro
                print("Digite um numero decimal / float!")



        # se for 4 entao e dividir
        elif op == 4:

            # a pessoa digita 2 numeros para dividir
            numero1 = input("Digite o primeiro numero que quer dividir: ")
            numero2 = input("Digite o segundo numero que quer dividir: ")

            # aqui e se e decimal / float se e eu divido se nao printa um erro
            if numero1.isdecimal() and numero2.isdecimal():
                numero1 = float(numero1)
                numero2 = float(numero2)
                total = numero1 / numero2
                # aqui printa o resultado
                print(f"O seu resultado deu: {total}")

            # se nao for decimal
            else:
                # print de erro
                print("Digite um numero decimal / float!")



        # se for 5 e avaliar
        # essa parte de verificar se e 10 ou menor ta errado ai pq to usando is decimal entao tem q mudar ai para isdigit mas ai queria com float msm entao seila
        elif op == 5:

            # aqui pede a avaliacao da pessoa
            avaliacao = input("Qual sua avaliacao 1/10: ")

            # se for um decimal executar
            if avaliacao.isdecimal():
                
                # se for 10 printar
                if avaliacao == 10:
                    print("Muito obrigado por seu 10 :D")

                # se for maior que 10 printar
                elif avaliacao > 10:
                    print("Seloku melhor que 10 ai sim!")

                # se for menor que 1 printar
                elif avaliacao < 1:
                    print("Menor que 1 que isso po")       

                # se nao for nenhum acima printar
                else:
                    print("Obrigado pela avaliacao :D")

            # se nao for um decimal printar erro
            else:
                print("Digite um numero decimal Ex: 1.5 ou 1")

        # se for 0 e sair entao break
        elif op == 0:
            break
            
        # se nao for nem 1 2 3 4 5 entao e invalido entao menssagem de erro
        else:
            print("Digite uma opcao valida!")
            
    # se o op nao for um numero entao erro
    else:
        print("Digite um numero inteiro Ex: 1")
