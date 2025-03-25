-*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: main.py
#
# Descrição: 
# Este script contém a interface gráfica (GUI) utilizando a biblioteca Tkinter para
# realizar o cadastro, busca, atualização e exclusão de alunos. Ele interage com o 
# banco de dados MySQL através das funções e classe definidas no arquivo `app.py`.
# A interface inclui opções de menu como "Sair", "Ajuda" e "Grid de Alunos" para 
# facilitar a navegação e interação do usuário com os dados.
#
# Autor: aluno1
# Data de Criação: 25/03/2025
# Hora de Criação: 15:00
#
# Dependências:
# - tkinter
# - ttk (parte do Tkinter)
# - mysql-connector-python
#
# Uso:
# Este script deve ser executado após a configuração do banco de dados MySQL e o
# preenchimento correto das credenciais de acesso no arquivo `app.py`. O usuário 
# pode interagir com a aplicação para gerenciar os dados de alunos no sistema.
# ==============================================================================

import tkinter as tk
from tkinter import messagebox, ttk
from app import Aluno, conectar_db  # Importando a classe Aluno e função de conexão

class AlunoApp:
    def __init__(self, root):
        # Inicializa a janela principal do aplicativo
        self.root = root
        self.root.title("Cadastro de Alunos")
        
        # Estabelece conexão com o banco de dados
        self.conn = conectar_db()

        # Criação do menu de navegação
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        # Menu "Arquivo"
        self.menu_arquivo = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.menu_arquivo.add_command(label="Sair", command=self.sair)

        # Menu "Ajuda"
        self.menu_ajuda = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ajuda", menu=self.menu_ajuda)
        self.menu_ajuda.add_command(label="Sobre", command=self.mostrar_ajuda)

        # Menu "Visualizar"
        self.menu_visualizar = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Visualizar", menu=self.menu_visualizar)
        self.menu_visualizar.add_command(label="Grid de Alunos", command=self.exibir_grid)

        # Criação dos campos de entrada para matrícula, nome e curso
        self.label_matricula = tk.Label(root, text="Matrícula:")
        self.label_matricula.grid(row=0, column=0)
        self.entry_matricula = tk.Entry(root)
        self.entry_matricula.grid(row=0, column=1)

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=1, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=1, column=1)

        self.label_curso = tk.Label(root, text="Curso:")
        self.label_curso.grid(row=2, column=0)
        self.entry_curso = tk.Entry(root)
        self.entry_curso.grid(row=2, column=1)

        # Criação dos botões para salvar, buscar, atualizar e excluir alunos
        self.botao_salvar = tk.Button(root, text="Salvar", command=self.salvar_aluno)
        self.botao_salvar.grid(row=3, column=0)

        self.botao_buscar = tk.Button(root, text="Buscar", command=self.buscar_aluno)
        self.botao_buscar.grid(row=3, column=1)

        self.botao_atualizar = tk.Button(root, text="Atualizar", command=self.atualizar_aluno)
        self.botao_atualizar.grid(row=3, column=2)

        self.botao_excluir = tk.Button(root, text="Excluir", command=self.excluir_aluno)
        self.botao_excluir.grid(row=3, column=3)

    # Método para salvar um aluno no banco de dados
    def salvar_aluno(self):
        matricula = self.entry_matricula.get()  # Obtém o valor da matrícula
        nome = self.entry_nome.get()            # Obtém o valor do nome
        curso = self.entry_curso.get()          # Obtém o valor do curso

        # Verifica se todos os campos estão preenchidos
        if matricula and nome and curso:
            aluno = Aluno(matricula, nome, curso)  # Cria um objeto Aluno
            aluno.salvar(self.conn)  # Chama o método salvar para inserir o aluno no banco
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

    # Método para buscar um aluno no banco de dados pela matrícula
    def buscar_aluno(self):
        matricula = self.entry_matricula.get()  # Obtém a matrícula inserida

        # Verifica se a matrícula foi informada
        if matricula:
            aluno = Aluno.buscar_por_matricula(self.conn, matricula)  # Busca o aluno
            if aluno:
                # Preenche os campos de nome e curso com os dados do aluno encontrado
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, aluno.nome)
                self.entry_curso.delete(0, tk.END)
                self.entry_curso.insert(0, aluno.curso)
            else:
                messagebox.showerror("Erro", "Aluno não encontrado!")
        else:
            messagebox.showerror("Erro", "Informe a matrícula para buscar!")

    # Método para atualizar os dados de um aluno
    def atualizar_aluno(self):
        matricula = self.entry_matricula.get()  # Obtém a matrícula inserida
        nome = self.entry_nome.get()            # Obtém o nome atualizado
        curso = self.entry_curso.get()          # Obtém o curso atualizado

        if matricula and nome and curso:
            aluno = Aluno.buscar_por_matricula(self.conn, matricula)  # Busca o aluno
            if aluno:
                aluno.nome = nome  # Atualiza os dados do aluno
                aluno.curso = curso
                aluno.atualizar(self.conn)  # Chama o método de atualização no banco
                messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Aluno não encontrado!")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

    # Método para excluir um aluno do banco de dados
    def excluir_aluno(self):
        matricula = self.entry_matricula.get()  # Obtém a matrícula inserida

        # Verifica se a matrícula foi informada
        if matricula:
            aluno = Aluno.buscar_por_matricula(self.conn, matricula)  # Busca o aluno
            if aluno:
                aluno.excluir(self.conn)  # Chama o método para excluir o aluno
                messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
                self.entry_nome.delete(0, tk.END)  # Limpa os campos de nome e curso
                self.entry_curso.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Aluno não encontrado!")
        else:
            messagebox.showerror("Erro", "Informe a matrícula para excluir!")

    # Método para sair do programa
    def sair(self):
        self.root.quit()  # Encerra a aplicação

    # Método para mostrar a ajuda sobre o uso da aplicação
    def mostrar_ajuda(self):
        messagebox.showinfo("Ajuda", "Este é um aplicativo de cadastro de alunos. Você pode:\n"
                                    "- Cadastrar um aluno\n"
                                    "- Buscar um aluno por matrícula\n"
                                    "- Atualizar os dados de um aluno\n"
                                    "- Excluir um aluno\n"
                                    "Para ver a lista de alunos, clique em 'Grid de Alunos'.")

    # Método para exibir a tabela (grid) de todos os alunos
    def exibir_grid(self):
        # Cria uma nova janela para exibir a grid de alunos
        grid_window = tk.Toplevel(self.root)
        grid_window.title("Grid de Alunos")

        # Cria a árvore (treeview) para exibir os dados de forma tabular
        tree = ttk.Treeview(grid_window, columns=("Matrícula", "Nome", "Curso"), show="headings")
        tree.pack(fill=tk.BOTH, expand=True)

        # Define as colunas da tabela
        tree.heading("Matrícula", text="Matrícula")
        tree.heading("Nome", text="Nome")
        tree.heading("Curso", text="Curso")

        # Recupera todos os alunos do banco de dados
        cursor = self.conn.cursor()
        cursor.execute("SELECT matricula, nome, curso FROM alunos")
        alunos = cursor.fetchall()

        # Insere cada aluno na tabela (grid)
        for aluno in alunos:
            tree.insert("", tk.END, values=(aluno[0], aluno[1], aluno[2]))

# Executa a aplicação
root = tk.Tk()
app = AlunoApp(root)
root.mainloop()
