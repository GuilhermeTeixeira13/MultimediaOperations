from functions import *
import numpy 
import os

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
            videoPretoBranco('videos/video.mp4')
        elif option == 4:
            clearConsole()
            print_menuCompressao()
            option = ''
            try:
                option = int(input('\nEscolha uma opção: '))
            except:
                print('Input inválido, por favor escolha um número...\n')
            if option == 1:
                image_path = ('images/cao.jpg')
                image = load_image(image_path)
                w, h, d = image.shape
                X = image.reshape((w * h, d))
                K = 4 # the desired number of colors in the compressed image
                colors, _ = find_k_means(X, K, max_iters=20)
                idx = find_closest_centroids(X, colors)
                idx = numpy.array(idx, dtype=numpy.uint8)
                X_reconstructed = numpy.array(colors[idx, :] * 255, dtype=numpy.uint8).reshape((w, h, d))
                compressed_image = Image.fromarray(X_reconstructed)
                compressed_image.save('images/imagemCompressao.png')
                tamanhoImagem = os.stat('images/cao.jpg').st_size
                tamanhoImagemComp = os.stat('images/imagemCompressao.png').st_size
                razao = tamanhoImagem/tamanhoImagemComp
                print("Imagem cao.png comprimida com sucesso, verificar imagemCompressao.png")
                print("Tamanho do imagem original: {0}KB\nTamanho da imagem comprimida: {1}KB\nTaxa de compressão: {2}".format(tamanhoImagem, tamanhoImagemComp, razao))
                sleep(5)


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