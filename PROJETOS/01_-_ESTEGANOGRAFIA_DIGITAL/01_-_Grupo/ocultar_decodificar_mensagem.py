def ocultar_mensagem(imagem, mensagem):
    # Adicionar o caractere de término à mensagem
    mensagem += '\0'

    # Converter a mensagem em binário
    mensagem_binaria = ''
    for caractere in mensagem:
        binario = format(ord(caractere), '08b')
        mensagem_binaria += binario
    
    imagem_oculta = imagem.copy()
    dados = imagem_oculta.getdata()
    indice_mensagem = 0
    for indice_pixel in range(len(dados)):
        pixel = list(dados[indice_pixel])
        for k in range(2):
            if indice_mensagem < len(mensagem_binaria):
                bit_mensagem = int(mensagem_binaria[indice_mensagem])
                pixel[k] = (pixel[k] & 0xFE) | bit_mensagem
                indice_mensagem += 1
        imagem_oculta.putpixel((indice_pixel % imagem_oculta.width, indice_pixel // imagem_oculta.width), tuple(pixel))

    return imagem_oculta

def decodificar_mensagem(imagem):
    dados = imagem.getdata()
    mensagem_binaria = ""
    for pixel in dados:
        for i in range(2):
            mensagem_binaria += str(pixel[i] & 1)
    mensagem = ""
    for i in range(0, len(mensagem_binaria), 8):
        byte = mensagem_binaria[i:i+8]
        caractere = chr(int(byte, 2))
        if caractere == '\0':  # Se encontrarmos o caractere de término, terminamos a decodificação
            break
        mensagem += caractere
    return mensagem
