from datasets import load_dataset

def cargar_dataset(split="train"):
    # Carga el dataset WikiText-103 desde Hugging Face
    dataset = load_dataset("wikitext", "wikitext-103-v1")

    # Retorna el split solicitado ('train', 'test' o 'validation')
    return dataset[split]
