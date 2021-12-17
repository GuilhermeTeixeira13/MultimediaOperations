from functions import *

if __name__=='__main__':
    clearConsole()
    while(True):
        print('TP - Múltimédia - a45662 / a45644\n')
        print_menuPrincipal()
        option = ''
        try:
            option = int(input('\nEscolha uma opção: '))
        except:
            print('Input inválido, por favor escolha um número...\n')
        clearConsole()
        if option == 1:
            clearConsole()
            print_menuImagens()
            option = ''
            try:
                option = int(input('\nEscolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...\n')
            if option == 1:
                clearConsole()
                print_menuOperacoesAritmeticas()
                option = ''
                try:
                    option = int(input('\nEscolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...\n')
                if option == 1:
                    imagemMultiplicacao('cao.jpg', 'gato.jpg')
                elif option == 2:
                    imagemSubtracao('cao.jpg', 'gato.jpg')
                elif option == 3:
                    clearConsole()
                    breakpoint
                else:
                    clearConsole()
                    print('Opção inválida, escolha um número entre 1 e 3.\n')
                clearConsole()
            elif option == 2:
                clearConsole()
                print_menuOperacoesLogicas()
                option = ''
                try:
                    option = int(input('\nEscolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...\n')
                if option == 1:
                    imagemNegativo("cao.jpg")
                elif option == 2:
                    imagemAND("bandeiraBelgica.jpg", "bandeiraAlemanha.jpg")
                elif option == 3:
                    clearConsole()
                    breakpoint
                else:
                    clearConsole()
                    print('Opção inválida, escolha um número entre 1 e 3.\n')
                clearConsole()
            elif option == 3:
                clearConsole()
                print_menuFiltragem()
                option = ''
                try:
                    option = int(input('\nEscolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...\n')
                if option == 1:
                    imagemThreshold('grayScaleImage.jpeg')
                elif option == 2:
                    imagemPretoBranco("gato.jpg")
                elif option == 3:
                    clearConsole()
                    breakpoint
                else:
                    clearConsole()
                    print('Opção inválida, escolha um número entre 1 e 3.\n')
                clearConsole()
            elif option == 4:
                clearConsole()
                breakpoint
            else:
                clearConsole()
                print('Opção inválida, escolha um número entre 1 e 4.\n')
            clearConsole
        elif option == 2:
            clearConsole()
            print_menuAudio()
            option = ''
            try:
                option = int(input('\nEscolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...\n')
            if option == 1:
                clearConsole()
                print_menuAudioEdicao()
                option = ''
                try:
                    option = int(input('\nEscolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...\n')
                if option == 1:
                    audioCortar()
                elif option == 2:
                    audioJuntar()
                elif option == 3:
                    clearConsole()
                    breakpoint
                else:
                    clearConsole()
                    print('Opção inválida, escolha um número entre 1 e 3.\n')
                clearConsole()
            elif option == 2:
                clearConsole()
                print_menuAudioFiltros()
                option = ''
                try:
                    option = int(input('\nEscolha uma opção: '))
                except:
                    print('Input inválido, por favor escolha um número...\n')
                if option == 1:
                    print_menuAudioEdicao()
                    option = ''
                    try:
                        option = int(input('\nEscolha uma opção: '))
                    except:
                        print('Input inválido, por favor escolha um número...\n')
                    if option == 1:
                        audioAumentarFreq()
                    elif option == 2:
                        audioAcelerar()
                    elif option == 3:
                        clearConsole()
                        breakpoint
                    else:
                        clearConsole()
                        print('Opção inválida, escolha um número entre 1 e 3.\n')
                    clearConsole()
            elif option == 3:
                clearConsole()
                breakpoint
            else:
                exit()
        elif option == 3:
            videoPretoBranco()
            clearConsole()
        elif option == 4:
            clearConsole()
            print_menuCompressao()
            option = ''
            try:
                option = int(input('\nEscolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...\n')
            if option == 1:
                comprimeImagem()
            elif option == 2:
                comprimeVideo()
            elif option == 3:
                clearConsole()
                breakpoint
            else:
                clearConsole()
                print('Opção inválida, escolha um número entre 1 e 3.\n')
            clearConsole()
        elif option == 5:
            clearConsole()
            exit()
        else:
            clearConsole()
            print('Opção inválida, escolha um número entre 1 e 5.\n')