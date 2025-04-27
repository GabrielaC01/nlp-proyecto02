from datasets import load_dataset

def cargar_dataset(split="train"):
    # Carga el dataset WikiText-103 desde Hugging Face
    dataset = load_dataset("wikitext", "wikitext-103-v1")

    # Retorna el split solicitado ('train', 'test' o 'validation')
    return dataset[split]

def tokenize_sentences_by_char(sentences):
    # Tokeniza una lista de oraciones en listas de caracteres 
    return [list(sentence.lower().strip()) for sentence in sentences]

def cargar_oraciones_limpias(split="train", num_oraciones=5):
    # Carga un número de oraciones no vacías del split seleccionado
    dataset = cargar_dataset(split=split)
    sentences = []
    count = 0
    for sentence in dataset:
        if sentence["text"].strip():
            sentences.append(sentence["text"].strip())
            count += 1
        if count == num_oraciones:
            break
    return sentences