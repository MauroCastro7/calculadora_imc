import tkinter as tk
from tkinter import ttk

def calculate_imc():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        imc = weight / (height ** 2)
        imc_result.config(text=f"{imc:.2f}")

        if imc < 16:
            imc_category.config(text="Muito abaixo do peso", fg="blue")
        elif imc < 18.5:
            imc_category.config(text="Abaixo do peso", fg="green")
        elif imc < 25:
            imc_category.config(text="Peso normal", fg="lightgreen")
        elif imc < 30:
            imc_category.config(text="Acima do peso", fg="yellow")
        elif imc < 35:
            imc_category.config(text="Obesidade I", fg="orange")
        elif imc < 40:
            imc_category.config(text="Obesidade II", fg="red")
        else:
            imc_category.config(text="Obesidade III", fg="darkred")
    except ValueError:
        imc_result.config(text="")
        imc_category.config(text="Por favor, insira valores válidos.")

root = tk.Tk()
root.title("Calculadora de IMC")

# Criar campos de entrada
weight_label = tk.Label(root, text="Peso (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(root, text="Altura (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Criar botão de cálculo
calculate_button = tk.Button(root, text="Calcular IMC", command=calculate_imc)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Criar campos de exibição do resultado
imc_label = tk.Label(root, text="IMC:")
imc_label.grid(row=3, column=0, padx=10, pady=10)
imc_result = tk.Label(root, text="")
imc_result.grid(row=3, column=1, padx=10, pady=10)

imc_category_label = tk.Label(root, text="Categoria:")
imc_category_label.grid(row=4, column=0, padx=10, pady=10)
imc_category = tk.Label(root, text="")
imc_category.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()

