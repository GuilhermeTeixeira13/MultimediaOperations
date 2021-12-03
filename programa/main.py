menuPrincipalOptions = {
    1: 'Imagens',
    2: 'Áudio',
    3: 'Vídeo',
    4: 'Compressão',
    5: 'Sair'
}

menuImagensOptions = {
    1: 'Operações Aritméticas',
    2: 'Operações Lógicas',
    3: 'Filtros',
    4: 'Sair',
}

menuAudioOptions = {
    1: 'Edição',
    2: 'Filtros',
    3: 'Sair',
}

menuCompressaoOptions = {
    1: 'Compressão de imagem',
    2: 'Compressão de vídeo',
    3: 'Sair',
}

def print_menuPrincipal():
    for key in menuPrincipalOptions.keys():
        print (key, '--', menuPrincipalOptions[key] )

def print_menuImagens():
    for key in menuImagensOptions.keys():
        print (key, '--', menuAudioOptions[key] )

def print_menuAudio():
    for key in menuImagensOptions.keys():
        print (key, '--', menuImagensOptions[key] )

def print_menuCompressao():
    for key in menuCompressaoOptions.keys():
        print (key, '--', menuCompressaoOptions[key] )

def videoPretoBranco():
    print('Vídeo a preeto e branco')

def imagemAdicao():
    print('Adição de imagens')

def imagemSubtracao():
    print('Subtração de imagens')

if __name__=='__main__':
    while(True):
        print_menuPrincipal()
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Input inválido, por favor escolha um número...')
        if option == 1:
            print_menuImagens()
            option = ''
            try:
                option = int(input('Escolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...')
            if option == 1:
                
            elif option == 2:
                
            elif option == 3:

            else
                exit()

        elif option == 2:
            print_menuAudio()
        elif option == 3:
            videoPretoBranco()
        elif option == 4:
            print_menuCompressao()
        elif option == 5:
            exit()
        else:
            print('Opção inválida, escolha um número entre 1 e 5.')