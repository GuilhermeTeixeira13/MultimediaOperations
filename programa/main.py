from functions import *
import numpy 
# Defenições de compressão de Imagem
def initialize_K_centroids(X, K):
    """ Choose K points from X at random """
    m = len(X)
    return X[numpy.random.choice(m, K, replace=False), :]

def find_closest_centroids(X, centroids):
    m = len(X)
    c = numpy.zeros(m)
    for i in range(m):
        # Find distances
        distances = numpy.linalg.norm(X[i] - centroids, axis=1)

        # Assign closest cluster to c[i]
        c[i] = numpy.argmin(distances)

    return c

def compute_means(X, idx, K):
    _, n = X.shape
    centroids = numpy.zeros((K, n))
    for k in range(K):
        examples = X[numpy.where(idx == k)]
        mean = [numpy.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids

def find_k_means(X, K, max_iters=10):
    centroids = initialize_K_centroids(X, K)
    previous_centroids = centroids
    for _ in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        if (centroids == previous_centroids).all():
            # The centroids aren't moving anymore.
            return centroids
        else:
            previous_centroids = centroids

    return centroids, idx

def load_image(path):
    """ Load image from path. Return a numpy array """
    image = Image.open(path)
    return numpy.asarray(image) / 255


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
                image_path = 'images/cao.jpg'

                
                image = load_image(image_path)
                w, h, d = image.shape
                print('Image found with width: {}, height: {}, depth: {}'.format(w, h, d))
                X = image.reshape((w * h, d))
                K = 20 # the desired number of colors in the compressed image
                colors, _ = find_k_means(X, K, max_iters=20)
                idx = find_closest_centroids(X, colors)
                idx = numpy.array(idx, dtype=numpy.uint8)
                X_reconstructed = numpy.array(colors[idx, :] * 255, dtype=numpy.uint8).reshape((w, h, d))
                compressed_image = Image.fromarray(X_reconstructed)
                compressed_image.save('images/imagemCompressao.png')

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