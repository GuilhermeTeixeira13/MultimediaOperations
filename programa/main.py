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
                    imagemMultiplicacao("/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/cao.jpg", "/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/gato.jpg")
                elif option == 2:
                    imagemSubtracao("/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/cao.jpg", "/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/gato.jpg")
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
                    imagemNegativo("/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/cao.jpg")
                elif option == 2:
                    imagemAND("/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/bandeiraBelgica.jpg", "/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/bandeiraAlemanha.jpg")
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
                    imagemThreshold('/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/grayScaleImage.jpeg')
                elif option == 2:
                    imagemPretoBranco("/home/jbaltazar17/Documents/GitHub/TP-MULT/imagens/gato.jpg")
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
                    audioCortar("sound2.wav")
                elif option == 2:
                    audioJuntar("/home/jbaltazar17/Documents/GitHub/TP-MULT/sound/soundJ1.wav", "/home/jbaltazar17/Documents/GitHub/TP-MULT/sound/soundJ2.wav")
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
            videoPretoBranco("video.mov")
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