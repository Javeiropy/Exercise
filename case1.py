area = [200,'null',720,1500,1000,275,'null',1200,2400,'null']
altura = ['null',30,40,30,10,25,33,'null',12,20]
largura = [20,20,'null',50,100,'null',30,100,200,10]

terreno = list(zip(area, largura, altura))#transforma as 3 listas em uma só
terreno = [list(terreno[c]) for c in range(len(terreno))]# transofrma cada tupla dentro da lista em uma lista

for c in range(len(terreno)):
    if terreno[c][0]=='null':
        terreno[c][0] = terreno[c][1]*terreno[c][2]

    if terreno[c][1] == 'null':
        terreno[c][1] = terreno[c][0]/terreno[c][2]

    if terreno[c][2] == 'null':
        terreno[c][2] = terreno[c][0] / terreno[c][1]

print(sorted(terreno, reverse=True))
