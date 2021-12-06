import os
from PIL import Image
from PIL import ImageEnhance
from time import sleep

def imagemMultiplicacao(pathImagem1, pathImagem2):
    # Abrir imagens
    imagem1 = Image.open(pathImagem1)
    imagem2 = Image.open(pathImagem2)
    
    # Criar nova imagem onde será guardado o resultado
    imagemMult = Image.new(imagem1.mode, imagem1.size, 'white')
    imagemMult.save("ImagemMultiplicacao.jpg")

    # Precorrer imagem pixel a pixel
    for x in range(0, imagem1.size[0]-1):
        for y in range(0, imagem1.size[1]-1):
            # Para cada imagem, armazenar os dados do pixel
            pixelColorsValsImagem1 = imagem1.getpixel((x,y))
            pixelColorsValsImagem2 = imagem2.getpixel((x,y))

            # Criar novos valores para o RGB -> Multiplicando o valor de cada R,G,B de cada uma das imagens
            redPixel = pixelColorsValsImagem1[0] * pixelColorsValsImagem2[0]
            greenPixel = pixelColorsValsImagem1[1] * pixelColorsValsImagem2[1]
            bluePixel = pixelColorsValsImagem1[2] * pixelColorsValsImagem2[2]

            # Colocar em cada pixel da imagem criada, o pixel com os novos valores de RGB
            imagemMult.putpixel((x,y), (redPixel, greenPixel, bluePixel))
    
    # Guardar nova imagem e mostrar aviso ao utilizador
    imagemMult.save('ImagemMultiplicacao.jpg')

    print('Multiplicação de imagens realizada com sucesso --> Verificar ImagemMultiplicação.jpg')
    sleep(4)

def imagemSubtracao(pathImagem1, pathImagem2):
    # Abrir imagens
    imagem1 = Image.open(pathImagem1)
    imagem2 = Image.open(pathImagem2)

    # Criar nova imagem onde será guardado o resultado
    imagemSoma = Image.new(imagem1.mode, imagem1.size, 'white')
    imagemSoma.save("ImagemSubt.jpg")

    # Precorrer imagem pixel a pixel
    for x in range(0, imagem1.size[0]-1):
        for y in range(0, imagem1.size[1]-1):
            # Para cada imagem, armazenar os dados do pixel
            pixelColorsValsImagem1 = imagem1.getpixel((x,y))
            pixelColorsValsImagem2 = imagem2.getpixel((x,y))

            # Criar novos valores para o RGB -> Subtraindo o valor de cada R,G,B de cada uma das imagens
            redPixel = pixelColorsValsImagem1[0] - pixelColorsValsImagem2[0]
            greenPixel = pixelColorsValsImagem1[1] - pixelColorsValsImagem2[1]
            bluePixel = pixelColorsValsImagem1[2] - pixelColorsValsImagem2[2]

            # Colocar em cada pixel da imagem criada, o pixel com os novos valores de RGB
            imagemSoma.putpixel((x,y), (redPixel, greenPixel, bluePixel))
    
    # Guardar nova imagem e mostrar aviso ao utilizador
    imagemSoma.save('ImagemSubt.jpg')
    print('Subtração de imagens realizada com sucesso --> Verificar ImagemSubt.jpg')
    sleep(4)

def imagemNegativo(pathImagem1):
    # Abrir imagem
    imagem1 = Image.open(pathImagem1)

    # Criar a Imagem Resultado
    imagem_negativo = Image.new(imagem1.mode, imagem1.size, 'white')
    imagem_negativo.save("ImagemNegativo.jpg")
    
    # Negativo - Algoritmo
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
    imagem_negativo.save("ImagemNegativo.jpg")
    print('Negativo de uma imagem realizado com sucesso --> Verificar ImagemNegativo.jpg')
    sleep(4)
  
def imagemAND():
    print('AND de imagens')

def imagemThreshold():
    print('Threshold de uma imagem')

def imagemPretoBranco(pathimagem1):
    # Abrir imagem
    image = Image.open(pathimagem1)

    # recolher dados da imagem
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
    new_img.save("ImagemPretoBranco.jpg")
    print('Preto e branco da imagem realizado com sucesso --> Verificar ImagemPretoBranco.jpg')
    sleep(4)

def audioCortar():
    print('Cortar um áudio')

def audioJuntar():
    print('Juntar um áudio a outro')

def audioAumentarFreq():
    print('Aumentar frequência')

def audioAcelerar():
    print('Acelera um áudio')

def videoPretoBranco():
    print('Vídeo a preeto e branco')

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
    1: 'Aumentar frequência',
    2: 'Mostrar apenas a frequência num determinado intervalo',
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