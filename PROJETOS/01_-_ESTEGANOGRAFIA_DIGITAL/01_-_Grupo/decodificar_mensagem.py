
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
