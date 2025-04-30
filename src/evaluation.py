import torch
import matplotlib.pyplot as plt
import csv

# Función para calcular la pérdida en los datos de validación
def evaluate_model(model, dataloader, criterion, vocab_size):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for inputs, targets in dataloader:
            outputs = model(inputs)
            outputs = outputs.view(-1, vocab_size)
            targets = targets.view(-1)
            loss = criterion(outputs, targets)
            total_loss += loss.item()
    return total_loss / len(dataloader)

# Función para guardar la pérdida de entrenamiento
def save_training_loss(training_loss, filename='training_loss.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Epoch", "Loss"])  # Encabezado
        for epoch, loss in enumerate(training_loss, 1):
            writer.writerow([epoch, loss])

# Función para cargar la pérdida de entrenamiento desde un archivo
def load_training_loss(filename='training_loss.csv'):
    epochs = []
    loss_values = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Salta los encabezados
        for row in reader:
            epochs.append(int(row[0]))
            loss_values.append(float(row[1]))
    return epochs, loss_values

# Función para graficar la pérdida de entrenamiento
def plot_training_loss(training_loss, filename='training_loss.csv'):
    epochs, training_loss = load_training_loss(filename)

    # Graficar la pérdida de entrenamiento
    plt.plot(epochs, training_loss, label='Training Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training Loss Over Epochs')
    plt.legend()
    plt.grid(True)
    plt.show()