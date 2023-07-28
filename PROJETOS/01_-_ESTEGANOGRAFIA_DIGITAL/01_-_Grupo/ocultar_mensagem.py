from PIL import Image

def converter_para_escala_de_cinzas(imagem):
    # Converter a imagem para escala de cinzas (modo 'L')
    imagem_cinzas = imagem.convert('L')
    return imagem_cinzas

def ocultar_mensagem(imagem, mensagem):
    # Converter a imagem para escala de cinzas
    imagem_cinzas = converter_para_escala_de_cinzas(imagem)

    # Adicionar o caractere de término à mensagem
    mensagem += '\0'

    # Converter a mensagem em binário
    mensagem_binaria = ''
    for caractere in mensagem:
        binario = format(ord(caractere), '08b')
        mensagem_binaria += binario
    
    imagem_oculta = imagem_cinzas.copy()
    dados = imagem_oculta.getdata()
    indice_mensagem = 0
    for indice_pixel in range(len(dados)):
        pixel = dados[indice_pixel]
        # Aqui estamos modificando o único componente de cor na imagem em escala de cinzas
        if indice_mensagem < len(mensagem_binaria):
            bit_mensagem = int(mensagem_binaria[indice_mensagem])
            # Modificamos o valor do pixel para conter o bit da mensagem
            pixel = pixel & 0xFE | bit_mensagem
            indice_mensagem += 1
        imagem_oculta.putpixel((indice_pixel % imagem_oculta.width, indice_pixel // imagem_oculta.width), pixel)

    return imagem_oculta

def is_grayscale(image_path):
    with Image.open(image_path) as img:
        if img.mode == 'L':
            return True
        else:
            return False
