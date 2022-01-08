from functions import *
import numpy 
import os

# Defenições do vídeo preto e branco
class VideoToGrayscaleWidget(object):
    def __init__(self, src=0):
        # Cria um objeto de video captura
        self.capture = cv2.VideoCapture(src)

        # Resoluções padrão do frame 
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Configuração do codec e da saída do output do video
        self.codec = cv2.VideoWriter_fourcc('X','V','I','D')
        self.output_video = cv2.VideoWriter('videos/videoPretoBranco.mp4', self.codec, 30, (self.frame_width, self.frame_height), isColor=False)

        # Os threads começam a ler os frames da stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Lê o frame seguinte através de um thread diferente do anterior
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        # Conversão para preto e branco
        if self.status:
            self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('grayscale frame', self.gray)

        # Press 'q' on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        # Guarda os frames já convertidos para preto e branco, para um ficheiro
        self.output_video.write(self.gray)


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
            """video_src = 'videos/video.mp4'
            video_stream_widget = VideoToGrayscaleWidget(video_src)
            while True:
                try:
                    video_stream_widget.show_frame()
                    video_stream_widget.save_frame()

                except AttributeError:
                    pass"""
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