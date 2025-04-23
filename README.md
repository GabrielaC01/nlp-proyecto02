<h2 align="center">
<p>Proyecto 2: Tokenización avanzada y compresión de vocabulario con BPE </p>
</h2>


## 📃 Descripción

Implementación de un sistema de **tokenización** basado en **Byte-Pair Encoding (BPE)** que ajusta será dinámicamente su vocabulario para maximizar la cobertura y reducir los términos fuera de vocabulario (**OOV**), evaluando su impacto en **modelos de lenguaje n-grama y neuronales**

## 📊 Dataset

Se utilizará el dataset **WikiText-103** de Hugging Face, que consiste en artículos de Wikipedia en inglés, para observar el comportamiento de la tokenización, la cobertura del vocabulario y el rendimiento de los modelos entrenados.

- **Origen**: [WikiText-103 en Hugging Face](https://huggingface.co/datasets/wikitext)

## 💻 Enfoque
El enfoque del proyecto está centrado en:

* Implementar un sistema de BPE para tokenizar texto

* Experimentar con distintos tamaños de vocabulario

* Aplicar subword regularization mediante muestreo estocástico

* Entrenar modelos de lenguaje:

  * n-grama (orden 3–5), evaluando perplejidad

  * RNN simple, evaluando convergencia

* Visualizar los embeddings de sub-tokens con PCA o t-SNE

* Analizar los sub-tokens y merges generados para identificar patrones lingüísticos


## 👩‍💻 Maintainers
* Gabriela Colque, Github: [GabrielaC16](https://github.com/GabrielaC16/) Email: gabriela.colque.u@uni.pe   
