import os
from PIL import Image

def imagemAdicao(pathImagem1, pathImagem2):
    imagem1 = Image.open(pathImagem1)
    imagem2 = Image.open(pathImagem2)

    imagemSoma = Image.new(imagem1.mode, imagem1.size, 'white')
    imagemSoma.save("ImagemSoma.jpg")

    for i in range(0, imagem1.size[0]-1):
        for j in range(0, imagem1.size[1]-1):
            pixelColorsValsImagem1 = imagem1.getpixel((i,j))
            pixelColorsValsImagem2 = imagem2.getpixel((i,j))

            redPixel = pixelColorsValsImagem1[0] + pixelColorsValsImagem2[0]
            greenPixel = pixelColorsValsImagem1[1] + pixelColorsValsImagem2[1]
            bluePixel = pixelColorsValsImagem1[2] + pixelColorsValsImagem2[2]

            imagemSoma.putpixel((i,j), (redPixel, greenPixel, bluePixel))
    
    imagemSoma.save('ImagemSoma.jpg')
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