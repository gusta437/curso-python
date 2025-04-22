import tkinter as tk
from tkinter import ttk, messagebox

def carregar_pets():
    for item in tree.get_children():
        tree.delete(item)
    for pet in pets:
        tree.insert('', 'end', values=(
            pet['id'],
            pet['tutor'],     
            pet['nome'],
            pet['especie'],
            pet['raca'],            
            pet['idade']
        ))



def adicionar_pets():
    global next_pet_id
    tutor = entry_tutor.get()
    nome = entry_pet.get()
    especie = entry_especie.get()
    raca = entry_raca.get()
    idade = entry_idade.get()

    if not tutor or not nome:
        messagebox.showerror('Erro',
                             'Tutor e nome do pet sao obrigatorios!')
        return
    
    try:
        idade_int = int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro',
                            'idade deve ser um numero inteiro')
        return

    novo_pet = {
      'id': next_pet_id,
      'tutor': tutor,
      'nome': nome,
      'especie': especie,
      'raca': raca,
      'idade': idade_int,
}

    pets.append(novo_pet)
    next_pet_id += 1
    
    messagebox.showinfo('Sucesso',
                         'Pet cadastrado com sucesso!')                 


    carregar_pets()

def selecionar_pet(event):
    selected_item = tree.selection()
    if not selected_item:
        return

    values = tree.item(selected_item)['values']
    limpar_campos()

    entry_tutor.insert(0, values[1])
    entry_pet.insert(0, values[2])
    entry_especie.insert(0, values[3])
    entry_raca.insert(0, values[4])
    entry_idade.insert(0, values[5])
    
 
def limpar_campos():
    entry_tutor.delete(0,'end')
    entry_pet.delete(0,'end')
    entry_especie.delete(0,'end')
    entry_raca.delete(0,'end')
    entry_idade.delete(0,'end')


def editar_pet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('erro',
                             'selecione um pet para editar')
        return
    

    pet_id = tree.item(selected_item)['values'][0]
    tutor = entry_tutor.get()
    nome = entry_pet.get()
    especie = entry_especie.get()
    raca = entry_raca.get()
    idade = entry_idade.get()
   

    if not tutor or not nome:
        messagebox.showerror('Erro',
                        'tutor e nome do pet sao obrigatorio')
        return


    try:
        idade_int = int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro',
                             'idade deve ser um numero inteiro')
        return


    for pet in pets:
        if pet['id'] == pet_id:
            pet.update({
                'tutor':tutor,
                'nome': nome,
                'especie':especie,
                'raca': raca,
                'idade': idade_int
            })
            break
    
    messagebox.showinfo('Sucesso',
                        'pet atualizado com sucesso')
    carregar_pets()                    
    

def remover_pet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('erro',
                             'selecione um pet para remover')
        
        return
    
    pet_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno('Confirmacao',
                           'tem certeza que deseja remover esse pet?'):
        
        global pets

        pets = [pets for pet in pets if pet['id'] !=pet_id]
        messagebox.showinfo('Sucesso',
                            'pet removido com sucesso')
        
        limpar_campos()
        carregar_pets()




pets = []
next_pet_id = 1

root = tk.Tk()
root.title("sistema de cadastro de pets")
root.geometry('800x500')


frame_form = ttk.LabelFrame(root,
                            text='Formulario de Pet')
frame_form.pack(padx=10, pady=5, fill="x")


ttk.Label(frame_form,
          text='Tutor:').grid(row=0,
                              column=0,
                              padx=5,
                              pady=5,
                              sticky='e')
entry_tutor = ttk.Entry(frame_form,
                        width=40)
entry_tutor.grid(row=0, column=1,
                 padx=5, pady=5)



ttk.Label(frame_form,
          text='Name pet:').grid(row=1,
                              column=0,
                              padx=5,
                              pady=5,
                              sticky='e')
entry_pet = ttk.Entry(frame_form,
                        width=40)
entry_pet.grid(row=1, column=1,
                 padx=5, pady=5)


ttk.Label(frame_form,
          text='Especie:').grid(row=2,
                              column=0,
                              padx=5,
                              pady=5,
                              sticky='e')
entry_especie = ttk.Entry(frame_form,
                        width=40)
entry_especie.grid(row=2, column=1,
                 padx=5, pady=5)

ttk.Label(frame_form,
          text='Raça:').grid(row=3,
                              column=0,
                              padx=5,
                              pady=5,
                              sticky='e')
entry_raca = ttk.Entry(frame_form,
                        width=40)
entry_raca.grid(row=3, column=1,
                 padx=5, pady=5)



ttk.Label(frame_form,
          text='Idade:').grid(row=4,
                              column=0,
                              padx=5,
                              pady=5,
                              sticky='e')
entry_idade = ttk.Entry(frame_form,
                        width=40)
entry_idade.grid(row=4, column=1,
                 padx=5, pady=5)



frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)
btn_adicionar = ttk.Button(frame_botoes,
                           text='adicionar',
                           command=adicionar_pets)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_editar = ttk.Button(frame_botoes,
                           text='editar',
                           command=editar_pet)
btn_editar.grid(row=0, column=1, padx=5)


btn_remover = ttk.Button(frame_botoes,
                           text='Remover',
                           command=remover_pet)
btn_remover.grid(row=0, column=2, padx=5)


btn_limpar = ttk.Button(frame_botoes,
                           text='Limpar',
                           command=limpar_campos
                           )
btn_limpar.grid(row=0, column=3, padx=5)

frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=15, pady=10,
                  fill='both', expand=True)

tree = ttk.Treeview(frame_tabela,
                    columns=('ID', "Tutor", "Nome",
                             'Especie', "Raça",
                             "Idade"), show='headings')
tree.heading('ID', text='ID')
tree.heading('Tutor', text='Tutor')
tree.heading('Nome', text='Nome')
tree.heading('Especie', text='Especie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')

tree.pack(fill=tk.BOTH, expand=True)

tree.column('ID',width=50)
tree.column('Tutor',width=150)
tree.column('Especie',width=100)
tree.column('Raça',width=100)
tree.column('Idade',width=50)

scrollabar = ttk.Scrollbar(frame_tabela,
                           orient='vertical',
                           command=tree.yview)
tree.configure(yscrollcommand=scrollabar.set)

tree.pack(side='left', fill='both',
          expand=True)

scrollabar.pack(side='right', fill='y')


tree.bind('<<TreeviewSelect>>', selecionar_pet)















root.mainloop() 