try:
    import sys
    import os,ffmpeg
    from PIL import Image
    from PIL import ImageEnhance
    from time import sleep
    from pydub import AudioSegment
    import math
    import numpy 
    from threading import Thread
    import cv2  
except ImportError:
    print ("Error: missing one of the libraries (numpy, pyfits, scipy, matplotlib)")
    sys.exit()

def get_file_size_in_bytes(file_path):
   ## Devolve o tamanho em bytes do ficheiro
   size = os.path.getsize(file_path)
   return size

# -> Defenições de compressão de Imagem 

# Cria pontos iniciais para os centróides.
def initialize_K_centroids(X, K):
    """ Choose K points from X at random """
    m = len(X)
    return X[numpy.random.choice(m, K, replace=False), :]

# Encontra o centróide mais próximo para cada exemplo de treino.
def find_closest_centroids(X, centroids):
    m = len(X)
    c = numpy.zeros(m)
    for i in range(m):
        # Find distances
        distances = numpy.linalg.norm(X[i] - centroids, axis=1)
        # Assign closest cluster to c[i]
        c[i] = numpy.argmin(distances)
    return c

# Calcula a distância de cada exemplo para o "seu" centróide e a média da sua distância para cada centróide
def compute_means(X, idx, K):
    _, n = X.shape
    centroids = numpy.zeros((K, n))
    for k in range(K):
        examples = X[numpy.where(idx == k)]
        mean = [numpy.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids

# Aplicação do algoritmo K-means, retorna os resultados quando os centróides já não se mexerem.
def find_k_means(X, K, max_iters=10):
    centroids = initialize_K_centroids(X, K)
    previous_centroids = centroids
    for _ in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        if (centroids == previous_centroids).all():
            return centroids
        else:
            previous_centroids = centroids

    return centroids, idx

# Como o algoritmo não recebe como parâmetro imagens, precisamos de converter a imagem dada num array.
def load_image(path):
    ## Devolve um numpy array com a imagem lida através do path
    image = Image.open(path)
    return numpy.asarray(image) / 255

# -> Fim das defenições de compressão de imagem


def imagemMultiplicacao(pathImagem1, pathImagem2):
    # Abrir imagens
    imagem1 = Image.open(pathImagem1)
    imagem2 = Image.open(pathImagem2)
    
    # Criar nova imagem onde será guardado o resultado
    imagemMult = Image.new(imagem1.mode, imagem1.size, 'white')
    imagemMult.save("images/ImagemMultiplicacao.jpg")

    # Precorrer imagem pixel a pixel
    for x in range(0, imagem1.size[0]-1):
        for y in range(0, imagem1.size[1]-1):
            # Para cada imagem, armazenar os dados do pixel
            pixelColorsValsImagem1 = imagem1.getpixel((x,y))
            pixelColorsValsImagem2 = imagem2.getpixel((x,y))

            # Criar novos valores para o RGB -> Multiplicando o valor de cada R,G,B de cada uma das imagens
            redPixel = pixelColorsValsImagem1[0] * pixelColorsValsImagem2[0]
            if redPixel > 255 :
                redPixel = 255
            elif redPixel < 0:
                redPixel = 0
            greenPixel = pixelColorsValsImagem1[1] * pixelColorsValsImagem2[1]
            if greenPixel > 255 :
                greenPixel = 255
            elif greenPixel < 0:
                greenPixel = 0
            bluePixel = pixelColorsValsImagem1[2] * pixelColorsValsImagem2[2]
            if bluePixel > 255 :
                bluePixel = 255
            elif bluePixel < 0:
                bluePixel = 0

            # Colocar em cada pixel da imagem criada, o pixel com os novos valores de RGB
            imagemMult.putpixel((x,y), (redPixel, greenPixel, bluePixel))
    
    # Guardar nova imagem e mostrar aviso ao utilizador
    imagemMult.save('images/ImagemMultiplicacao.jpg')

    print('Multiplicação de imagens realizada com sucesso --> Verificar ImagemMultiplicação.jpg')
    sleep(4)

def imagemSubtracao(pathImagem1, pathImagem2):
    # Abrir imagens
    imagem1 = Image.open(pathImagem1)
    imagem2 = Image.open(pathImagem2)

    # Criar nova imagem onde será guardado o resultado
    imagemSoma = Image.new(imagem1.mode, imagem1.size, 'white')
    imagemSoma.save("images/ImagemSubt.jpg")

    # Precorrer imagem pixel a pixel
    for x in range(0, imagem1.size[0]-1):
        for y in range(0, imagem1.size[1]-1):
            # Para cada imagem, armazenar os dados do pixel
            pixelColorsValsImagem1 = imagem1.getpixel((x,y))
            pixelColorsValsImagem2 = imagem2.getpixel((x,y))

            # Criar novos valores para o RGB -> Subtraindo o valor de cada R,G,B de cada uma das imagens
            redPixel = pixelColorsValsImagem1[0] - pixelColorsValsImagem2[0]
            if redPixel < 0:
                redPixel = 0
            greenPixel = pixelColorsValsImagem1[1] - pixelColorsValsImagem2[1]
            if greenPixel < 0:
                redPixel = 0
            bluePixel = pixelColorsValsImagem1[2] - pixelColorsValsImagem2[2]
            if bluePixel < 0:
                bluePixel = 0

            # Colocar em cada pixel da imagem criada, o pixel com os novos valores de RGB
            imagemSoma.putpixel((x,y), (redPixel, greenPixel, bluePixel))
    
    # Guardar nova imagem e mostrar aviso ao utilizador
    imagemSoma.save('images/ImagemSubt.jpg')
    print('Subtração de imagens realizada com sucesso --> Verificar ImagemSubt.jpg')
    sleep(4)

def imagemNegativo(pathImagem1):
    # Abrir imagem
    imagem1 = Image.open(pathImagem1)

    # Criar a Imagem Resultado
    imagem_negativo = Image.new(imagem1.mode, imagem1.size, 'white')
    imagem_negativo.save("images/ImagemNegativo.jpg")
    
    # Precorrer a imagem pixel a pixel
    for x in range(0, imagem1.size[0] - 1):
        for y in range(0, imagem1.size[1] - 1):

            # Encontrar o valor do pixel na posição (x,y) da imagem
            pixelColorVals = imagem1.getpixel((x,y))

            # Inverter a Cor
            redPixel = 255 - pixelColorVals[0]  # Negativo do pixel vermelho
            greenPixel = 255 - pixelColorVals[1] # Negativo do pixel verde
            bluePixel = 255 - pixelColorVals[2] # Negativo do pixel azul

            # Modificar a imagem com os pixeis invertidos
            imagem_negativo.putpixel((x,y), (redPixel, greenPixel, bluePixel))

    # Guardar nova imagem e mostrar aviso ao utilizador
    imagem_negativo.save("images/ImagemNegativo.jpg")
    print('Negativo de uma imagem realizado com sucesso --> Verificar ImagemNegativo.jpg')
    sleep(4)
  
def imagemAND(pathImagem1, pathImagem2):
    # Abrir Imagem
    imagem1 = Image.open(pathImagem1)
    imagem2 = Image.open(pathImagem2)

    # Criar a Imagem Resultado
    imagem_and = Image.new(imagem1.mode, imagem1.size, 'white')
    imagem_and.save("images/ImagemAND.jpg") 
    for x in range(0, imagem1.size[0] - 1):
        for y in range(0, imagem1.size[1] - 1):

            # Encontrar o valor do pixel na posição (x,y) da imagem1 e imagem2:
            pixelImg1 = imagem1.getpixel((x,y))
            pixelImg2 = imagem2.getpixel((x,y))


            diferencaRedPixel = pixelImg1[0] - pixelImg2[0]
            diferencaGreenPixel = pixelImg1[1] - pixelImg2[1]
            diferencaBluePixel = pixelImg1[2] - pixelImg2[2]

            # Verifica as interseções
            if diferencaRedPixel == 0 and diferencaGreenPixel == 0 and diferencaBluePixel == 0:
                imagem_and.putpixel((x,y) , (pixelImg1[0], pixelImg1[1], pixelImg1[2]))

    # Guardar nova imagem e mostrar aviso ao utilizador
    imagem_and.save("images/ImagemAND.jpg")
    print('AND de uma imagem realizado com sucesso --> Verificar ImagemAND.jpg')
    sleep(4)

def imagemThreshold(pathImagem):
    # Abrir imagens
    imagem = Image.open(pathImagem)

    # Criar nova imagem onde será guardado o resultado
    imagemThreshold = Image.new(imagem.mode, imagem.size, 'white')
    imagemThreshold.save("images/ImagemThreshold.jpg")

    # Precorrer imagem pixel a pixel
    for x in range(0, imagem.size[0]-1):
        for y in range(0, imagem.size[1]-1):
            # Para cada imagem, armazenar os dados do pixel
            pixelColorsValsImagem = imagem.getpixel((x,y))

            # Criar novos valores para o RGB -> Subtraindo o valor de cada R,G,B de cada uma das imagens
            redPixel = pixelColorsValsImagem[0]
            greenPixel = pixelColorsValsImagem[1]
            bluePixel = pixelColorsValsImagem[2]
            if redPixel > 127:
                redPixel = 255
                greenPixel = 255
                bluePixel = 255
            else:
                redPixel = 0
                greenPixel = 0
                bluePixel = 0

            # Colocar em cada pixel da imagem criada, o pixel com os novos valores de RGB
            imagemThreshold.putpixel((x,y), (redPixel, greenPixel, bluePixel))
    
    # Guardar nova imagem e mostrar aviso ao utilizador
    imagemThreshold.save('images/ImagemThreshold.jpg')
    print('Threshold da imagem realizado com sucesso --> Verificar ImagemThreshold.jpg')
    sleep(4)

def imagemPretoBranco(pathimagem1):
    # Abrir imagem
    image = Image.open(pathimagem1)

    # Recolher dados da imagem
    img_data = image.getdata()

    # Criar lista em que são colocados os pixeis da imagem lida, transformados para valores de preto e branco
    lst=[]
    for pixel in img_data:
        lst.append(pixel[0]*0.2125+pixel[1]*0.7174+pixel[2]*0.0721)

    # Criar nova imagem do mesmo tamanho da imagem lida
    new_img = Image.new("L", image.size)

    # Colocar na nova imagem o conteúdo da lista
    new_img.putdata(lst)

    # Guardar nova imagem e mostrar aviso ao utilizador
    new_img.save("images/ImagemPretoBranco.jpg")
    print('Preto e branco da imagem realizado com sucesso --> Verificar ImagemPretoBranco.jpg')
    sleep(4)

def audioCortar(pathAudio):

    # Cabeçalho da classe
    class SplitWavAudio():
        def __init__(self, folder, filename):
            self.folder = folder
            self.filename = filename
            self.filepath = folder + '/' + filename

            self.audio = AudioSegment.from_wav(self.filepath)

        # Devolve a duração em segundos
        def get_duration(self):
            return self.audio.duration_seconds

        # Corta o áudio num intervalo de tempo dado
        def single_split(self, from_min, to_min, split_filename):
            t1 = from_min * 60 * 1000
            t2 = to_min * 60 * 1000
            split_audio = self.audio[t1:t2]
            split_audio.export(self.folder + '/' + split_filename , format = "wav")
        
        # Corta o áudio em vários, dependendo do tempo que o utilizador queira para cada áudio cortado
        def multiple_split(self, min_per_split):
            total_mins = math.ceil(self.get_duration() / 60)
            for i in range(0, total_mins, min_per_split):
                split_fn = str(i) + '_' + self.filename
                self.single_split(i, i + min_per_split, split_fn)
                print(str(i) + 'Done')
                if i == total_mins - min_per_split:
                    print('All splited successfully')

    folder = 'sound'
    file = pathAudio
    split_wav = SplitWavAudio(folder, file)
    split_wav.multiple_split(min_per_split=1)
    print("Som separado com sucesso, verificar parte 0/1/2/3/4/5 do sound2.wav")
    sleep(4)

# Acrescenta um áudio ao final do outro através do '+'
def audioJuntar(pathAudio1, pathAudio2): 
    sound1 = AudioSegment.from_wav(pathAudio1)
    sound2 = AudioSegment.from_wav(pathAudio2)

    combined_sounds = sound1 + sound2
    combined_sounds.export("sound/soundJOUTPUT.wav", format="wav")
    print("Sons somados com sucesso, verificar soundJOUTPUT.wav")
    sleep(3)

def audioLowPassFilter(pathAudio):
    ## Lê som a partir de um path dado
    song = AudioSegment.from_wav(pathAudio)

    ## Cria um novo som a partir do primeiro mas com as frequências a cima de 2000Hz eliminadas
    new = song.low_pass_filter(2000)

    ## Guarda o novo som criado
    new.export("sound/sound2LowPassFilter.wav", format="wav")

    print("Low Pass FIlter aplicado com sucesso, verificar sound2LowPassFilter.wav")
    sleep(3)

def audioAcelerar(pathAudio, speed):
    ## Lê som a partir de um path dado
    sound = AudioSegment.from_wav(pathAudio)

    ## Cria um novo som acelerado "speed" vezes, sendo speed o argumento passado na função
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

    ## Guarda o novo som criado
    sound_with_altered_frame_rate.export("sound/sound2Acelerado.wav", format="wav")
    
    print("Som acelerado com sucesso, verificar sound2Acelerado.wav")
    sleep(3)

def videoPretoBranco(videopath):
    source = cv2.VideoCapture(videopath)
    while True:
        # Retira o frame
        ret, frame = source.read()
        # Se não tiver recebido o frame corretamente
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Conversão do frame da stream para preto e branco
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Mostrar o video
        cv2.imshow("Live", gray)
    
        # Sair do ciclo
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    # Fechar a janela
    cv2.destroyAllWindows()
    source.release()
    
# Outra Função de Vídeo a Preto e branco - Não usada pois não estava a funcionar bem
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
    
def comprimeVideo(video_full_path, output_file_name, target_size):
    ##  video_full_path - Path do video que pretendemos comprimir
    ##  output_file_name - Nome com que ficará guardado o video comprimido
    ##  O target é o tamanho do video comprimido desejado, em MB

    tamanhoVideo = get_file_size_in_bytes(video_full_path)

    # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000

    probe = ffmpeg.probe(video_full_path)

    # Duração do video em segundos
    duration = float(probe['format']['duration'])

    # Bitrate do áudio, em bps
    audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])

    # Bitrate total do target, em bps
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Bitrate do áudio do target, em bps
    if 10 * audio_bitrate > target_total_bitrate:
        audio_bitrate = target_total_bitrate / 10
        if audio_bitrate < min_audio_bitrate < target_total_bitrate:
            audio_bitrate = min_audio_bitrate
        elif audio_bitrate > max_audio_bitrate:
            audio_bitrate = max_audio_bitrate

    # Bitrate do vídeo do target, em bps
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)

    ## Guarda o vídeo comprimido
    ffmpeg.output(i, os.devnull,**{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}).overwrite_output().run()
    ffmpeg.output(i, output_file_name,**{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}).overwrite_output().run()

    print("Video comprimido com sucesso, verificar videoComprimido.mp4")

    ## Mostra o tamanho inicial e final do video e a respetiva taxa de conversão
    tamanhoVideoComp = get_file_size_in_bytes(output_file_name)
    razao = tamanhoVideo/ tamanhoVideoComp
    print("Tamanho do vídeo original: {0}KB\nTamanho do vídeo comprimido: {1}KB\nTaxa de compressão: {2}".format(tamanhoVideo, tamanhoVideoComp, razao))
    sleep(7)

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
    1: 'Multiplicação de imagens',
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

menuAudioEdicao= {
    1: 'Cortar áudio',
    2: 'Juntar áudio',
    3: 'Sair',
}

menuAudioFiltros = {
    1: 'Low Pass Filter (Demora cerca de 15sec a ser aplicado)',
    2: 'Acelerar áudio',
    3: 'Sair',
}

def print_menuPrincipal():
    print('->   Menu Principal\n    ')
    for key in menuPrincipalOptions.keys():
        print (key, '->', menuPrincipalOptions[key] )

def print_menuImagens():
    print('->   Menu Imagens\n    ')
    for key in menuImagensOptions.keys():
        print (key, '->', menuImagensOptions[key] )

def print_menuAudio():
    print('->   Menu Áudio\n    ')
    for key in menuAudioOptions.keys():
        print (key, '->', menuAudioOptions[key] )

def print_menuCompressao():
    print('->   Menu Compressão\n    ')
    for key in menuCompressaoOptions.keys():
        print (key, '->', menuCompressaoOptions[key] )

def print_menuOperacoesAritmeticas():
    print('->   Menu Operações Aritméticas\n    ')
    for key in menuOperacoesAritmeticas.keys():
        print (key, '->', menuOperacoesAritmeticas[key] )

def print_menuOperacoesLogicas():
    print('->   Menu Operações Lógicas\n    ')
    for key in menuOperacoesLogicas.keys():
        print (key, '->', menuOperacoesLogicas[key] )
    
def print_menuFiltragem():
    print('->   Menu Filtragem\n    ')
    for key in menuFiltragem.keys():
        print (key, '->', menuFiltragem[key] )

def print_menuAudioEdicao():
    print('->   Menu Edição de Áudio\n    ')
    for key in menuAudioEdicao.keys():
        print (key, '->', menuAudioEdicao[key] )

def print_menuAudioFiltros():
    print('->   Menu Filtros de Áudio\n    ')
    for key in menuAudioFiltros.keys():
        print (key, '->', menuAudioFiltros[key] )

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
