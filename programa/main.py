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
                    imagemMultiplicacao('images/cao.jpg', 'images/gato.jpg')
                elif option == 2:
                    imagemSubtracao('images/cao.jpg', 'images/gato.jpg')
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
                    imagemNegativo("images/cao.jpg")
                elif option == 2:
                    imagemAND("images/bandeiraBelgica.jpg", "images/bandeiraAlemanha.jpg")
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
                    imagemThreshold('images/grayScaleImage.jpeg')
                elif option == 2:
                    imagemPretoBranco("images/gato.jpg")
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
            clearConsole()
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
                    audioJuntar("sound/soundJ1.wav", "sound/soundJ2.wav")
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
                    audioLowPassFilter("sound/sound2.wav")
                elif option == 2:
                    audioAcelerar("sound/soundJ1.wav", 5.0)
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
                clearConsole()
                print('Opção inválida, escolha um número entre 1 e 3.\n')
            clearConsole()
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
                comprimeVideo("videos/video.mp4", "videos/videoComprimido.mp4", 1000)
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