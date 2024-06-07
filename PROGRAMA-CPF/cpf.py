import cpf_funcoes
import os

while True:
    print("CPF\n\n1.Verificar se um cpf é válido.\n2.Encontrar os últimos 2 dígitos sabendo os outros 9\n3.Sair\n\n")
    modo = input("Escolha uma opção:\n=====> ")
    if modo == "1":
        os.system('cls')
        cpf = input("\nDigite o cpf que você deseja verificar: ")
        numeros_cpf = cpf_funcoes.somente_numeros(cpf)
        cpf = ""
        for i in range(9):
            cpf += numeros_cpf[i]
            
        for i in range(2):
            cpf_numeros = cpf_funcoes.organizar_cpf(cpf)
            cpf += cpf_funcoes.decobrir_digito(cpf_numeros)
        cpf = cpf_funcoes.somente_numeros(cpf)
        if cpf == numeros_cpf:
            print("\nEste cpf é válido!")
            exit()
        else:
            print("\nEste cpf é inválido!")
            exit()
    
    elif modo == "2":

        os.system('cls')
        cpf = input("\nDigite os 9 primeiros dígitos do seu cpf: ")
        for i in range(2):
            cpf_numeros = cpf_funcoes.organizar_cpf(cpf)
            cpf += cpf_funcoes.decobrir_digito(cpf_numeros)

        if len(cpf_funcoes.finalizar_cpf(cpf)) == 14:
            print("\n" , cpf_funcoes.finalizar_cpf(cpf), sep="")
            exit()
        else:
            print("\nVocê não digitou 9 números, tente novamente!\n")

    elif modo == "3":

        os.system('cls')
        print("\nVocê saiu!")
        exit()

    else:
        os.system('cls')
        print("\nOpção inválida! Digite um número de 1 a 3!\n")