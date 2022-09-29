from collections import OrderedDict
treinamentos = [{'treinamento':'Scrum','moedas':30},
                {'treinamento':'Data Science','moedas':40},
                {'treinamento':'Gestão de Projetos','moedas':50},
                {'treinamento':'Marketing','moedas':30},
                {'treinamento':'Cloud','moedas':20},
                {'treinamento':'Python','moedas':30},
                {'treinamento':'SQL','moedas':80}]
pedidos = ['SQL','SQL','SQL','SQL','SQL','SQL','SQL','SQL','SQL','SQL','SQL','Cloud','Cloud','Cloud','Cloud','Cloud','Cloud','Marketing','Scrum','Data Science','Gestão de Projetos','Marketing','Cloud','Python','Python','Python', 'Scrum','Data Science','Gestão de Projetos','Marketing','Data Science','Gestão de Projetos', 'Python','Marketing','Data Science','Gestão de Projetos','Data Science','Gestão de Projetos','Data Science']

#treinamento e moedas #tratando e unindo os dados
treinamento = [treinamentos[c]['treinamento'] for c in range(len(treinamentos))]#pega cada treinamento no dicionario
moedas = [treinamentos[c]['moedas'] for c in range(len(treinamentos))] #pega o valor  em moedas de cada treinamento
treinamento_moedas = list(zip(treinamento, moedas)) #junta os treinamentos com suas respectivas moedas

#quantidade e pedidos #tratando e unindo os dados
quantidade = [pedidos.count(pedidos[c]) for c, elemento in enumerate(pedidos)] #pega a quantidade de pedidos de cada treinamentos
nome = [elemento for c, elemento in enumerate(pedidos)]# pega o nome de cada treinamento
treinamento_pedido = list(zip(nome, quantidade))#junta os nomes do treinamento com seus respectivo pedido

#ajustando a lista 'quantidade pedido'
treinamento_pedido = set(treinamento_pedido)#tira os valores repetidos
treinamento_pedido = list(treinamento_pedido)#transforma o object set em lista
treinamento_pedido = sorted(treinamento_pedido)#ordena a lista em ordem crescente
lista_final_pedidos = [list(treinamento_pedido[c]) for c in range(len(treinamento_pedido))]#pega cada tupla dentro da lista e transforma em lista

#ajustando a lista treinamento moedas
treinamento_moedas = sorted(treinamento_moedas)#ordena a lista em ordem crescente
lista_final_moedas = [list(treinamento_moedas[c]) for c in range(len(treinamento_moedas))]#pega cada tupla dentro da lista e transforma em lista


lista_final = [lista_final_moedas[c][1] for c in range(len(lista_final_moedas)) if lista_final_moedas[c][0] in lista_final_pedidos[c][0]]
lista_final_definitiva = [lista_final_pedidos[c].append(lista_final[c]) for c in range(len(lista_final_pedidos))]
moedas = [lista_final_pedidos[c][2] for c in range(len(lista_final_pedidos))]
pedido = [lista_final_pedidos[c][1] for c in range(len(lista_final_pedidos))]
treinamento = [lista_final_pedidos[c][0] for c in range(len(lista_final_pedidos))]
finalmente = list(zip(pedido,moedas, treinamento))
lista_final_definitiva = [list(finalmente[c]) for c in range(len(finalmente))]
lista_final_definitiva = sorted(lista_final_definitiva, reverse=True)
orcamento = 150
fim=[]
valor = 0
for c in range(len(lista_final_definitiva)):
    valor+=lista_final_definitiva[c][1]
    if valor<=orcamento:
        fim.append(lista_final_definitiva[c])
    if c<len(fim):
        print(f'O curso {fim[c][2]} foi comprado por {fim[c][1]} moedas e teve um total de {fim[c][0]} pedidos')