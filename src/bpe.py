from collections import Counter
import random

class BytePairEncoding:
    def __init__(self, num_merges):
        self.num_merges = num_merges  # num_merges: define el número de fusiones de pares de tokens
        self.vocab = {}  # vocab: almacena el vocabulario actual 
        self.merges = []  # merges: lista donde se almacenan las fusiones que se van realizando

    def train(self, corpus):
        # Inicializa el corpus tokenizado y el vocabulario con todos los caracteres únicos en el corpus
        tokenized_corpus = []
        for word in corpus:
            tokens = list(word)  # Convierte cada palabra en una lista de caracteres (tokens iniciales)
            tokenized_corpus.append(tokens)
            # Agrega todos los caracteres únicos al vocabulario
            for char in tokens:
                self.vocab[char] = char
        
        # En cada iteración, el modelo cuenta las frecuencias de todos los pares de tokens
        for merge_step in range(1, self.num_merges + 1):
            pairs = self.get_pair_frequencies(tokenized_corpus)
            if not pairs:
                break

            # Encuentra el par con la frecuencia más alta
            most_frequent_pair = max(pairs, key=pairs.get)

            # Concatenar el par más frecuente para formar un nuevo token
            new_token = ''.join(most_frequent_pair)

            # Actualiza el vocabulario y guarda la fusión
            self.vocab[new_token] = new_token
            self.merges.append(most_frequent_pair)

            # Reemplaza cada aparición del par en las listas de tokens
            tokenized_corpus = self.replace_pairs_in_corpus(tokenized_corpus, most_frequent_pair, new_token)

    # Calcula las frecuencias de todos los pares consecutivos de tokens en el corpus.
    def get_pair_frequencies(self, tokenized_corpus):
        pairs = {}
        for tokens in tokenized_corpus:
            for i in range(len(tokens) - 1):
                pair = (tokens[i], tokens[i + 1])
                if pair in pairs:
                    pairs[pair] += 1
                else:
                    pairs[pair] = 1
        return pairs

    # Toma un par de tokens (pair) y lo reemplaza por un nuevo token
    def replace_pairs_in_corpus(self, tokenized_corpus, pair, new_token):
        new_corpus = []
        for tokens in tokenized_corpus:
            new_word = []
            i = 0
            # Verifica cada posición para detectar el par
            while i < len(tokens):
                if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == pair:
                    new_word.append(new_token)  # Fusiona el par en un nuevo token
                    i += 2  # Salta ambos tokens fusionados
                else:
                    new_word.append(tokens[i])
                    i += 1
            new_corpus.append(new_word)
        return new_corpus

    # Tokeniza una palabra nueva utilizando las fusiones aprendidas durante el entrenamiento
    def tokenize(self, word):
        tokens = list(word)  # Inicialmente cada letra es un token separado
        for merge in self.merges:
            new_token = ''.join(merge)
            merged_word = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == merge:
                    merged_word.append(new_token)
                    i += 2
                else:
                    merged_word.append(tokens[i])
                    i += 1
            tokens = merged_word
        return tokens

    def get_vocabulary(self):  # Devuelve el vocabulario actual de trabajo
        return self.vocab
    
    def tokenize_with_sampling(self, word, prob=0.5):
        tokens = list(word)
        for merge in self.merges:
            new_token = ''.join(merge)
            merged_word = []
            i = 0
            while i < len(tokens):
                if (
                    i < len(tokens) - 1
                    and (tokens[i], tokens[i + 1]) == merge
                    and random.random() < prob  # ← probabilidad de aplicar el merge
                ):
                    merged_word.append(new_token)
                    i += 2
                else:
                    merged_word.append(tokens[i])
                    i += 1
            tokens = merged_word
        return tokens