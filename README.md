<h2 align="center">
<p>Proyecto 2: Tokenización avanzada y compresión de vocabulario con BPE </p>
</h2>


## 📃 Descripción

Implementación de un sistema de **tokenización** basado en **Byte-Pair Encoding (BPE)** que ajusta dinámicamente su vocabulario para maximizar la cobertura y reducir los términos fuera de vocabulario (**OOV**), evaluando su impacto en **modelos de lenguaje n-grama y neuronales**

## 📊 Dataset

Se utilizará el dataset **[WikiText-103](https://huggingface.co/datasets/wikitext)** disponible en Hugging Face, el cual contiene artículos de Wikipedia en inglés. Este corpus es ampliamente utilizado para entrenar y evaluar modelos de lenguaje debido a su tamaño y riqueza léxica.

La carga del dataset se realiza dinámicamente utilizando el paquete `datasets` de Hugging Face. 
El procedimiento detallado de carga puede consultarse en el notebook [`01_data_loading.ipynb`](notebooks/01_data_loading.ipynb) incluido en este repositorio.

Este dataset será utilizado para observar el comportamiento de la tokenización, la cobertura del vocabulario y el rendimiento de los modelos entrenados.


## 💻 Enfoque
El enfoque del proyecto está centrado en:

1. Implementar un sistema de BPE para tokenizar texto

2. Experimentar con distintos tamaños de vocabulario

3. Aplicar subword regularization mediante muestreo estocástico

4. Entrenar modelos de lenguaje:
  
    - n-grama (orden 3–5), evaluando perplejidad
  
    - RNN simple, evaluando convergencia

5. Visualizar los embeddings de sub-tokens con PCA o t-SNE

6. Analizar los sub-tokens y merges generados para identificar patrones lingüísticos

## 💻 Instrucciones para configurar el entorno con Docker

#### 1. Clonar el repositorio  

```
git clone https://github.com/GabrielaC01/nlp-proyecto02.git
```
#### 2. Construir la imagen Docker

```
docker build -t mi-imagen-nlp .
```
#### 3. Ejecutar el contenedor y acceder a JupyterLab
```
sudo docker run -it --rm \
    -p 8888:8888 \
    -v /tu-ruta/nlp-proyecto02:/home/jovyan/work \
    mi-imagen-nlp
```

## 👩‍💻 Maintainers
* Gabriela Colque, Github: [GabrielaC16](https://github.com/GabrielaC16/) Email: gabriela.colque.u@uni.pe   
