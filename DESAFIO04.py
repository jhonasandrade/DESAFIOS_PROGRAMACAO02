'''
A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente,
a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das
três notas mencionadas obedecem aos pesos a seguir:
Nota                     Peso
Trabalho de laboratório   2
Avaliação semestral       3
Exame final               5
Escreva um programa que receba as três notas, calcule e mostre a média ponderada
e o conceito que segue a tabela:
Média ponderada    Conceito
8,0 <= valor <= 10,0  A
7,0 <= valor < 8,0    B
6,0 <= valor < 7,0    C
5,0 <= valor < 6,0    D
0,0 <= valor < 5,0    E
'''
traba_lab = float(input("DIGITE A NOTA DO TRABALHO:\n"))
nota_aval = float(input("DIGITE A NOTA DA PROVA:\n"))
exame_final = float(input("DIGITE A NOTA DO EXAME FINAL:\n"))

media_pond =(traba_lab * 2 + nota_aval * 3 + exame_final * 5) / 10

if media_pond >= 7.9 and media_pond <= 10.0:
    print(f"A MEDIA DAS NOTAS E {media_pond:.2f} E O CONCEITO E (A) ")
elif media_pond >= 6.9 and media_pond < 7.9:
    print(f"A MEDIA DAS NOTAS E {media_pond:.2f} E O CONCEITO E (B)")
elif media_pond >= 5.9 and media_pond < 6.9 :
    print(f"A MEDIA DAS NOTAS E {media_pond:.2f} E O CONCEITO E (C)")
elif media_pond >= 0.9 and media_pond < 5.9 :
    print(f"A MEDIA DAS NOTAS E {media_pond:.2f} E O CONCEITO E (D)")
elif media_pond <= 0 :
    print(f"A MEDIA DAS NOTAS E {media_pond:.2f} E O CONCEITO E (E)")  
else:
    print("DIGITE AS NOTAS!")                
