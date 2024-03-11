import numpy as np
import os
import re
import pandas as pd
import requests
from urllib.parse import quote
import webbrowser
from keras.applications import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity

# Carregar o modelo pré-treinado VGG16
modelo_base = VGG16(weights='imagenet', include_top=True)
modelo = Model(inputs=modelo_base.input, outputs=modelo_base.get_layer('fc2').output)

# Função para extrair características de uma imagem
def extrair_caracteristicas(caminho_img, modelo):
    img = image.load_img(caminho_img, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    caracteristicas = modelo.predict(x)
    return caracteristicas.flatten()

# Diretório contendo imagens de diferentes produtos
dir_dados = "Images"
caminhos_imagens = [os.path.join(dir_dados, f) for f in os.listdir(dir_dados) if os.path.isfile(os.path.join(dir_dados, f))]

# Extrair características para todas as imagens
dict_caracteristicas = {}
for caminho_img in caminhos_imagens:
    dict_caracteristicas[caminho_img] = extrair_caracteristicas(caminho_img, modelo)

# Função para recomendar o produto mais similar
def recomendar_produto_mais_similar(caminho_imagem_consulta, dict_caracteristicas):
    caracteristicas_consulta = extrair_caracteristicas(caminho_imagem_consulta, modelo)
    similaridade_maxima = -1
    melhor_caminho_imagem = None
    for caminho_img, caracteristicas in dict_caracteristicas.items():
        similaridade = cosine_similarity([caracteristicas_consulta], [caracteristicas])[0][0]
        if similaridade > similaridade_maxima:
            similaridade_maxima = similaridade
            melhor_caminho_imagem = caminho_img
    return melhor_caminho_imagem, similaridade_maxima

def extrair_numero(nome):
    padrão = r'\\(\d+)\.jpg'
    # Extraindo números entre "\" e ".jpg"
    números = re.findall(padrão, nome)
    return números

def pesquisar_imagens_similares_por_texto(texto_consulta, num_resultados=5):
    consulta = "https://www.google.com/search?q=" + quote(texto_consulta) + "&tbm=isch"
    webbrowser.open(consulta)
    return None

# Exemplo de uso
caminho_imagem_consulta = "ex.jpg"
melhor_caminho_imagem, similaridade = recomendar_produto_mais_similar(caminho_imagem_consulta, dict_caracteristicas)
print("Melhor Produto Similar:")
print(melhor_caminho_imagem, ":", similaridade)

numero = ''.join(extrair_numero(melhor_caminho_imagem))
print(f"Número: {''.join(extrair_numero(melhor_caminho_imagem))}")

df = pd.read_csv("File.csv", delimiter=";", encoding="UTF-8")

# Definir a coluna 'Id' como o índice
df.set_index('Id', inplace=True)

# Acessar o valor na coluna 'Description' para o rótulo no índice 
resultado = df.loc[int(numero), 'Description']

pesquisar_imagens_similares_por_texto(resultado)
