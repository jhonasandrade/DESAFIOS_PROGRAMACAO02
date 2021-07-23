'''
Escreva um algoritmo que, para uma conta bancária, leia o seu número, o saldo, o tipo de 
operação a ser realizada (depósito ou retirada) e o valor da operação. Após, determine e 
mostre o novo saldo. Se o novo saldo ficar negativo, deve ser mostrada, também, a 
mensagem “conta estourada”.
 NUMER_CONT =
 SALDO_CONT =
 TIPO_CONT = SOMA OU SUBTRACAO
 VALOR_OPERA = SE VALOR <= 0 ENTAO = "CONTA ESTOURADA" SE VALO_OPERA >= 0 ENTAO "VOCE PODE SACAR"
'''

numer_cont = int(input("DIGITE O NUMERO DA CONTA:\n"))
valor_depo = int(input("DIGITE O VALOR DE DEPO:\n "))
valor_saq = int(input("DIGITE O VALOR DE SAQ:\n "))
saldo_cont = 0
deposito =valor_depo + saldo_cont 
saque =  deposito - valor_saq
saldo_cont2 = saque
if saldo_cont2 <= 0:
    print("CONTA ESTOURADA\n")
else:
    print("DESEJA FAZER OUTRA OPERACAO\n")
print("O NUMERO DA CONTA E {}\n".format(numer_cont))      
print("O SALDO DA CONTA E {}\n".format(saldo_cont2))      