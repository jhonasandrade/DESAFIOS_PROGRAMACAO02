'''
Uma empresa produz três tipos de peças mecânicas: parafusos, porcas e arruelas. Têm-se 
os preços unitários de cada tipo de peça e sabe-se que sobre estes preços incidem descontos 
de 10% para porcas, 20% para parafusos e 30% para arruelas. Escreva um algoritmo que 
calcule o valor total da compra de um cliente. Deve ser mostrado o nome do cliente. O 
número de cada tipo de peça que o mesmo comprou, o total de desconto e o total a pagar 
pela compra.
TRES PEÇAS MECANIAS:
PORCAS=$$ - 10% DE DESCONTO;
PARAFUSO=$$ - 20% DE DESCONTO;
ARRUELAS=$$ - 30% DE DESCONTO;
POR DEFINIÇÃO OS VALORES DAS PECAS SERAO:0,50;1,50;0,45.
'''
########NOME DO CLIENTE##########
nome_client = str(input("DIGITE O NOME DO CLIENTE:\n"))
print(nome_client)
#######DADOS DA COMPRA#############
nome_pec_acompr = str(input("DIGITE O NOME DA PECA QUE DESEJA COMPRAR:\n"))
print(nome_pec_acompr)
########QUANTIDADE A COMPRAR##########
quanti_porca = int(input("DIGITE A QAUNTIDADEDE DE PORCAS:\n"))
print(quanti_porca)
quanti_arruela = int(input("DIGITE A QUANTIDADE DE ARRUELAS:\n"))
print(quanti_arruela)
quanti_parafuso = int(input("DIGITE A QUANTIDADE DE PARAFUSOS:\n"))
print(quanti_parafuso)
quanti_total = quanti_porca + quanti_arruela + quanti_parafuso
print(quanti_total)
#######VALOR DA COMPAR SEM DESCONTO##############
porca = quanti_porca * 0.50
arruela = quanti_arruela * 1.50 
parafuso = quanti_parafuso * 0.45
valor_total = porca + arruela + parafuso 
print(valor_total)
#########VALOR DO DESCONTO########
valor_descon =  valor_total - quanti_total * 50/100 
print(valor_descon)