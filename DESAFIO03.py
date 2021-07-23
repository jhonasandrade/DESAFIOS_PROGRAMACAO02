'''
O cardápio de uma lanchonete é o seguinte:
Código    Especificação        Preço unitário
100        Cachorro quente              1,10
101        Bauru simples                1,30
102        Bauru c/ovo                  1,50
103        Hamburger                    1,10
104        Cheeseburger                 1,30
105        Refrigerante                 1,00
Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a 
ser pago por aquele lanche. Considere que a cada execução somente será calculado um item.
'''
lanche01 ={
    'codigo':'100','nome':'cachorro quente','valor': 1.10
    }
lanche02 ={
    'codigo':'101','nome':'bauru simples','valor':1.30
}
lanche03 ={
    'codigo':'102','nome':'bauru com ovo','valor':1.50
}
lanche04 ={
    'codigo':'103','nome':'hamburger','valor':1.10
}
lanche05 ={
    'codigo':'104','nome':'chessburger','valor':1.30
}
lanche06 ={
    'codigo':'105','nome':'refrigerante','valor':1.00
}

quanti = int(input("Nº DE LANCHES:\n"))
i = int(input("ESCOLHA UMA OPCAO DE 1 A 6: CACHORRO QUENTE(1):BAURU SIMPLES(2):BAURU/OVO(3):HAMBURGER(4):CHESSBURGER(5):REFRIGERANTE(6):\n"))
if i==1:
    print("o codigo e ",lanche01['codigo'],"lanche",lanche01['nome'])
    valor = quanti * 1.10
    print(f"O VALOR DA COMPRA E ${valor:.1f}")
elif i == 2: 
    print("o codigo e ",lanche02['codigo'],"lanche",lanche02['nome'])
    valor2 = quanti * 1.30
    print(f"O AVLOR DA COMPRA E ${valor2:.1f}")
elif i == 3:
    print("o codigo e ",lanche03['codigo'],"lanche",lanche03['nome'])
    valor3 = quanti * 1.50
    print(f"O VALOR DA COMPRA E ${valor3:.1f}")
elif i == 4:
    print("o codigo e ",lanche04['codigo'],"lanche",lanche04['nome'])
    valor4 = quanti * 1.10
    print(f"O VALOR DA COMPRA E ${valor4:.1f}")
elif i == 5:
    print("o codigo e ",lanche05['codigo'],"lanche",lanche05['nome'])
    valor5 = quanti * 1.30
    print(f"O VALOR DA COMPRA E ${valor5:.1f}")
elif i == 6:
    print("o codigo e ",lanche06['codigo'],"lanche",lanche06['nome'])
    valor6 = quanti * 1.50
    print(f"O VALOR DA COMPRA E ${valor6:.1f}")     
else:
    print("ESCOLHA UMA DAS OPCOES:")               



