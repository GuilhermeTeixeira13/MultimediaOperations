import os

def imagemAdicao():
    print('Adição de imagens')


def imagemSubtracao():
    print('Subtração de imagens')


def imagemNegativo():
    print('Negativo de uma imagem')


def imagemAND():
    print('AND de imagens')


def imagemThreshold():
    print('Threshold de uma imagem')


def imagemPretoBranco():
    print('Preto e Branco de uma')


def audioCortar():
    print('Cortar um áudio')


def audioJuntar():
    print('Juntar um áudio a outro')


def audioAumentarFreq():
    print('Aumentar frequência')


def audioAcelerar():
    print('Acelera um áudio')


def videoPretoBranco():
    print('Vídeo a preto e branco')


def comprimeImagem():
    print('Comprime uma imagem')


def comprimeVideo():
    print('Comprime um video')


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

menuOperacoesAritmeticas = {
    1: 'Adição de imagens',
    2: 'Subtração de imagens',
    3: 'Sair',
}

menuOperacoesLogicas = {
    1: 'Negativo',
    2: 'AND',
    3: 'Sair',
}

menuFiltragem = {
    1: 'Threshold',
    2: 'Preto e Branco',
    3: 'Sair',
}

menuAudioEdicao = {
    1: 'Cortar áudio',
    2: 'Juntar áudio',
    3: 'Sair',
}

menuAudioFiltros = {
    1: 'Aumentar frequência',
    2: 'Mostrar apenas a frequência num determinado intervalo',
    3: 'Sair',
}


def print_menuPrincipal():
    print('->   Menu Principal\n    ')
    for key in menuPrincipalOptions.keys():
        print(key, '--', menuPrincipalOptions[key])


def print_menuImagens():
    print('->   Menu Imagens\n    ')
    for key in menuImagensOptions.keys():
        print(key, '--', menuImagensOptions[key])


def print_menuAudio():
    print('->   Menu Áudio\n    ')
    for key in menuAudioOptions.keys():
        print(key, '--', menuAudioOptions[key])


def print_menuCompressao():
    print('->   Menu Compressão\n   ')
    for key in menuCompressaoOptions.keys():
        print(key, '--', menuCompressaoOptions[key])


def print_menuOperacoesAritmeticas():
    print('->   Menu Operações Aritméticas\n    ')
    for key in menuOperacoesAritmeticas.keys():
        print(key, '--', menuOperacoesAritmeticas[key])


def print_menuOperacoesLogicas():
    print('->   Menu Operações Lógicas\n    ')
    for key in menuOperacoesLogicas.keys():
        print(key, '--', menuOperacoesLogicas[key])


def print_menuFiltragem():
    print('->   Menu Filtragem\n    ')
    for key in menuFiltragem.keys():
        print(key, '--', menuFiltragem[key])


def print_menuAudioEdicao():
    print('->   Menu Edição de Áudio\n    ')
    for key in menuAudioEdicao.keys():
        print(key, '--', menuAudioEdicao[key])


def print_menuAudioFiltros():
    print('->   Menu Filtros de Áudio\n    ')
    for key in menuAudioFiltros.keys():
        print(key, '--', menuAudioFiltros[key])


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


if __name__ == '__main__':
    clearConsole()
    while(True):
        print_menuPrincipal()
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Input inválido, por favor escolha um número...')
        clearConsole()
        if option == 1:
            clearConsole()
            print_menuImagens()
            option = ''
            try:
                option = int(input('Escolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...')
            if option == 1:
                clearConsole()
                print_menuOperacoesAritmeticas()
                option = ''
                try:
                    option = int(input('Escolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...')
                if option == 1:
                    imagemAdicao()
                elif option == 2:
                    imagemSubtracao
                elif option == 3:
                    breakpoint
                else:
                    print('Opção inválida, escolha um número entre 1 e 3.')
                clearConsole()
            elif option == 2:
                clearConsole()
                print_menuOperacoesLogicas()
                option = ''
                try:
                    option = int(input('Escolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...')
                if option == 1:
                    imagemNegativo()
                elif option == 2:
                    imagemAND()
                elif option == 3:
                    breakpoint
                else:
                    print('Opção inválida, escolha um número entre 1 e 3.')
                clearConsole()
            elif option == 3:
                clearConsole()
                print_menuFiltragem()
                option = ''
                try:
                    option = int(input('Escolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...')
                if option == 1:
                    imagemThreshold()
                elif option == 2:
                    imagemPretoBranco()
                elif option == 3:
                    breakpoint
                else:
                    print('Opção inválida, escolha um número entre 1 e 3.')
                clearConsole()
            else:
                print('Opção inválida, escolha um número entre 1 e 3.')
        elif option == 2:
            clearConsole()
            print_menuAudio()
            option = ''
            try:
                option = int(input('Escolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...')
            if option == 1:
                clearConsole()
                print_menuAudioEdicao()
                option = ''
                try:
                    option = int(input('Escolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...')
                if option == 1:
                    audioCortar()
                elif option == 2:
                    audioJuntar()
                elif option == 3:
                    breakpoint
                else:
                    print('Opção inválida, escolha um número entre 1 e 3.')
                clearConsole()
            elif option == 2:
                clearConsole()
                print_menuAudioFiltros()
                option = ''
                try:
                    option = int(input('Escolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...')
                if option == 1:
                    print_menuAudioEdicao()
                    option = ''
                    try:
                        option = int(input('Escolha uma opção: '))
                    except:
                        print('Input inválido, por favor escolha um número...')
                    if option == 1:
                        audioAumentarFreq()
                    elif option == 2:
                        audioAcelerar()
                    elif option == 3:
                        breakpoint
                    else:
                        print('Opção inválida, escolha um número entre 1 e 3.')
                    clearConsole()
            else:
                exit()
        elif option == 3:
            clearConsole()
            videoPretoBranco();
        elif option == 4:
            clearConsole()
            print_menuCompressao()
            option = ''
            try:
                option = int(input('Escolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...')
            if option == 1:
                print_menuAudioEdicao()
                option = ''
                try:
                    option = int(input('Escolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...')
                if option == 1:
                    comprimeImagem()
                elif option == 2:
                    comprimeVideo()
                elif option == 3:
                    breakpoint
                else:
                    print('Opção inválida, escolha um número entre 1 e 3.')
                clearConsole()
        elif option == 5:
            clearConsole()
            exit()
        else:
            print('Opção inválida, escolha um número entre 1 e 5.')
