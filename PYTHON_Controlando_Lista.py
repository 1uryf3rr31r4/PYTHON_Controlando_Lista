lista=[]

def adicionar_inicio(lista):
    item=''
    while item.lower()!='s':
        item=input("Insira o elemento ou digite 's' para finalizar: ")
        if item!='s':
            lista.insert(0, item)
            print(lista)

def adicionar_fim(lista):
    item=''
    while item.lower()!='s':
        item=input("Insira o elemento ou digite 's' para finalizar: ")
        if item!='s':
            lista.append(item)
            print(lista)

def remover_elemento(lista):
    item=input('Digite o item a ser removido: ')
    for value in lista:
        if value==item:
            lista.remove(item)
            return f'O elemento {item} foi removido.'
    return 'Este elemento não pertence a lista'

def tamanho_lista(lista):
    return len(lista)

def opcao():
    print('1 - Inserir elemento no inicio da lista')
    print('2 - Inserir elemento no final da lista')
    print('3 - Remover elemento da lista')
    print('4 - Retomar o tamanho da lista')
    print('5 - Imprimir a lista')
    print('6 - Esvaiar a lista')
    print('7 - Sair do Programa')

def menu():
    escolha=0
    while escolha!=7:
        opcao()
        escolha=int(input('>> '))
        if escolha==1:
            adicionar_inicio(lista)
        elif escolha==2:
            adicionar_fim(lista)
        elif escolha==3:
            print(remover_elemento(lista))
        elif escolha==4:
            print(f'Tamanho da lista: {tamanho_lista(lista)}')

if __name__=='__main__':
    menu()