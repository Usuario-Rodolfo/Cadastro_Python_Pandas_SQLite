import tkinter as tk
from tkinter import StringVar

class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Cadastro Clientes")
        self.window.geometry("600x400")

        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Campos de entrada
        tk.Label(self.window, text="Nome").grid(row=0, column=0)
        tk.Entry(self.window, textvariable=self.txtNome).grid(row=0, column=1)

        tk.Label(self.window, text="Sobrenome").grid(row=1, column=0)
        tk.Entry(self.window, textvariable=self.txtSobrenome).grid(row=1, column=1)

        tk.Label(self.window, text="E-mail").grid(row=2, column=0)
        tk.Entry(self.window, textvariable=self.txtEmail).grid(row=2, column=1)

        tk.Label(self.window, text="CPF").grid(row=3, column=0)
        tk.Entry(self.window, textvariable=self.txtCPF).grid(row=3, column=1)

        # Listbox e scrollbar
        self.listClientes = tk.Listbox(self.window, height=10, width=50)
        self.listClientes.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.grid(row=4, column=3, rowspan=6, sticky='ns')

        self.listClientes.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listClientes.yview)

        # Botões
        self.btnViewAll = tk.Button(self.window, text="Ver Todos")
        self.btnViewAll.grid(row=11, column=0)

        self.btnAdd = tk.Button(self.window, text="Inserir")
        self.btnAdd.grid(row=11, column=1)

        self.btnUpdate = tk.Button(self.window, text="Atualizar")
        self.btnUpdate.grid(row=11, column=2)

        self.btnDelete = tk.Button(self.window, text="Deletar")
        self.btnDelete.grid(row=11, column=3)

    def run(self):
        self.window.mainloop()