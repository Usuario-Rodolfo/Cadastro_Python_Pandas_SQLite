import tkinter as tk
from tkinter import messagebox, END
from Backend import TransactionObject
from app_gui import GUI

core = TransactionObject()
selected = None

def view_command():
    records = core.execute("SELECT * FROM clientes", fetch=True)
    app.listClientes.delete(0, END)
    for row in records:
        app.listClientes.insert(END, row)

def insert_command():
    nome = app.txtNome.get()
    sobrenome = app.txtSobrenome.get()
    email = app.txtEmail.get()
    cpf = app.txtCPF.get()
    if nome and sobrenome and email and cpf:
        sql = "INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (?, ?, ?, ?)"
        core.execute(sql, (nome, sobrenome, email, cpf))
        messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
        view_command()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

def getSelectedRow(event):
    global selected
    try:
        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)
        app.txtNome.set(selected[1])
        app.txtSobrenome.set(selected[2])
        app.txtEmail.set(selected[3])
        app.txtCPF.set(selected[4])
    except IndexError:
        pass

def delete_command():
    global selected
    if selected:
        sql = "DELETE FROM clientes WHERE id = ?"
        core.execute(sql, (selected[0],))
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
        view_command()
    else:
        messagebox.showwarning("Atenção", "Selecione um cliente para deletar.")

def update_command():
    global selected
    if selected:
        nome = app.txtNome.get()
        sobrenome = app.txtSobrenome.get()
        email = app.txtEmail.get()
        cpf = app.txtCPF.get()
        sql = "UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, cpf = ? WHERE id = ?"
        core.execute(sql, (nome, sobrenome, email, cpf, selected[0]))
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        view_command()
    else:
        messagebox.showwarning("Atenção", "Selecione um cliente para atualizar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
    app.btnViewAll.configure(command=view_command)
    app.btnAdd.configure(command=insert_command)
    app.btnDelete.configure(command=delete_command)
    app.btnUpdate.configure(command=update_command)
    app.run()