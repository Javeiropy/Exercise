def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]


usuarios_feedback = [{'nome':'Peter','nota':9,'genero':'M','comentario':'bom demais e agil'},
                     {'nome':'Joao','nota':10,'genero':'M','comentario':'agil e eficiente'},
                     {'nome':'user_not_found','nota':0,'genero':'M','comentario':'Horrível'},
                     {'nome':'Marta','nota':10,'genero':'F','comentario':'muito agil bom demais'},
                     {'nome':'Beatriz','nota':10,'genero':'F','comentario':'rápido e eficaz'},
                     {'nome':'user_not_found','nota':2,'genero':'M','comentario':'ruim'},
                     {'nome':'Jéssica','nota':10,'genero':'F','comentario':'agil'},
                     {'nome':'José','nota':7,'genero':'M','comentario':'ok'},
                     {'nome':'Elias','nota':5,'genero':'M','comentario':'precisa melhorar'},
                     {'nome':'Miriã','nota':9,'genero':'F','comentario':'foi muito agil e rápido'},
                     {'nome':'Maria','nota':10,'genero':'F','comentario':'muito bom e agil'}]

#separa cada palavra da lista de comentarios
lista_comentarios =  [usuarios_feedback[c]['comentario'].split() for c in range(len(usuarios_feedback))]

#transforma a lista de lista em uma unica lista
lista_comentarios = lista_simples(lista_comentarios)

#conta a quantidade de palavras iguais
quantidade_palavras = [lista_comentarios.count(lista_comentarios[c]) for c in range(len(lista_comentarios))]

#junta a lista de quantidades com a de palavras
lista_final = list(zip(quantidade_palavras, lista_comentarios))

#retira os valores repetidos
lista_final = set(lista_final)

#transforma o bject set em uma lista
lista_final = list(lista_final)

#ordena da palavra mais comentada para a menos comentada
lista_final = sorted(lista_final, reverse=True)

for c, item in lista_final:
    print(f'A palavra mais comentada foi: {item.upper()}\n e teve: {c} comentários\n')
