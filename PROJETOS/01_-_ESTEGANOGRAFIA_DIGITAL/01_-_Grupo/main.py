from PIL import Image
import matplotlib.pyplot as plt
from ocultar_mensagem import ocultar_mensagem
from decodificar_mensagem import decodificar_mensagem


#Carregar a imagem
imagem = Image.open('img.bmp')

# #Exibir a imagem
# plt.imshow(imagem, cmap='gray')
# plt.show()


# #Converter a imagem em binário
# imagem_binaria = ''
# for pixel in list(imagem.getdata()):
#     imagem_binaria += ''.join([format(i,'08b') for i in pixel])

# #Imprimir a imagem binária
# print(imagem_binaria)


# Solicitar ao usuário que insira a mensagem secreta
mensagem_secreta = input("Por favor, insira a mensagem secreta que você deseja ocultar na imagem: ")

# Ocultar a mensagem na imagem
imagem_oculta = ocultar_mensagem(imagem, mensagem_secreta)

# Salvar a imagem com a mensagem oculta
imagem_oculta.save('img_com_msg.bmp')

#Carregar a imagem
img_oculta = Image.open('img_com_msg.bmp')

#Exibir a imagem
plt.imshow(img_oculta, cmap='gray')
plt.show()

# Carregar a imagem com a mensagem oculta
imagem_oculta = Image.open('img_com_msg.bmp')

# Decodificar a mensagem da imagem
mensagem_decodificada = decodificar_mensagem(imagem_oculta)

# Imprimir a mensagem decodificada
print("A mensagem oculta na imagem é:", mensagem_decodificada)

# Exibir a imagem
imagem_oculta.show()