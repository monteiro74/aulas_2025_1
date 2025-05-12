-*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: app.py
#
# Descrição: 
# Este script contém a lógica da aplicação de cadastro de alunos, com a definição
# da classe Aluno que interage com o banco de dados MySQL. Inclui funções para salvar,
# buscar, atualizar e excluir registros de alunos na tabela 'alunos'.
#
# Autor: aluno1
# Data de Criação: 25/03/2025
# Hora de Criação: 15:00
#
# Dependências:
# - mysql-connector-python
#
# Uso:
# Este script é utilizado em conjunto com o script main.py para realizar operações 
# CRUD (Create, Read, Update, Delete) sobre alunos em um banco de dados MySQL.
# ==============================================================================

import mysql.connector

# Definição da classe Aluno, que representa os alunos no sistema
class Aluno:
    # Construtor da classe, inicializa os dados do aluno
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula  # Matrícula do aluno (única)
        self.nome = nome            # Nome do aluno
        self.curso = curso          # Curso do aluno

    # Método para salvar um novo aluno no banco de dados
    def salvar(self, conn):
        # Cria um cursor para executar comandos SQL
        cursor = conn.cursor()
        
        # Comando SQL para inserir um novo aluno
        cursor.execute("INSERT INTO alunos (matricula, nome, curso) VALUES (%s, %s, %s)", 
                       (self.matricula, self.nome, self.curso))
        
        # Commit para salvar as mudanças no banco de dados
        conn.commit()

    # Método para buscar um aluno no banco de dados através da matrícula
    @staticmethod
    def buscar_por_matricula(conn, matricula):
        cursor = conn.cursor()
        
        # Comando SQL para buscar aluno pela matrícula
        cursor.execute("SELECT * FROM alunos WHERE matricula = %s", (matricula,))
        
        # Recupera o primeiro resultado da consulta
        result = cursor.fetchone()
        
        # Se um aluno for encontrado, cria e retorna um objeto Aluno
        if result:
            return Aluno(result[0], result[1], result[2])
        
        # Caso não encontre aluno, retorna None
        return None

    # Método para atualizar as informações de um aluno no banco de dados
    def atualizar(self, conn):
        cursor = conn.cursor()
        
        # Comando SQL para atualizar os dados de um aluno
        cursor.execute("UPDATE alunos SET nome = %s, curso = %s WHERE matricula = %s", 
                       (self.nome, self.curso, self.matricula))
        
        # Commit para salvar as mudanças
        conn.commit()

    # Método para excluir um aluno do banco de dados
    def excluir(self, conn):
        cursor = conn.cursor()
        
        # Comando SQL para deletar o aluno com a matrícula especificada
        cursor.execute("DELETE FROM alunos WHERE matricula = %s", (self.matricula,))
        
        # Commit para salvar as mudanças
        conn.commit()

# Função para conectar ao banco de dados MySQL
def conectar_db():
    # Retorna a conexão com o banco de dados MySQL
    return mysql.connector.connect(
        host="localhost",         # Endereço do servidor MySQL
        user="root",              # Usuário do banco de dados (ajustar conforme sua configuração)
        password="",              # Senha do usuário (ajustar conforme sua configuração)
        database="escola"         # Nome do banco de dados
    )
