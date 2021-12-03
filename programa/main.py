menu_options = {
    1: 'Imagens',
    2: 'Áudio',
    3: 'Compressão',
    4: 'Sair',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('opção 1')

def option2():
     print('opção 2')

def option3():
     print('opção 3')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Input inválido, por favor escolha um número...')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            exit()
        else:
            print('Opção inválida, escolha um número entre 1 e 4.')