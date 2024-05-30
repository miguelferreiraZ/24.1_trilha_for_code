# Description: Sistema de gerenciamento de alunos e disciplinas da UFRJ
# 


import secrets

class Sistema():
  
  def __init__(self):
    self.alunos = []
    self.disciplinas = []
    self.matriculas = []
    self.professores = []

  def cadastrar_aluno(self, nome, curso, email):
    aluno = Aluno(nome, curso, email)
    self.alunos.append(aluno)

  def cadastrar_disciplina(self, nome, creditos, aulasSemana):
    disciplina = Disciplina(nome, creditos, aulasSemana)
    self.disciplinas.append(disciplina)

  def cadastrar_professor(self, nome, email, senha):
    professor = Professor(nome, email, senha)
    self.professores.append(professor)

class Pessoa():
  
  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha
    
class Aluno(Pessoa):
  def __init__(self, nome, curso, email, senha):
    super().__init__(nome, email, senha)
    self.curso = curso
    self.matricula = secrets.token_hex(8)
    
class Professor(Pessoa):
  def __init__(self, nome, email, senha):
    super().__init__(nome, email, senha)

class Disciplina():
  def __init__(self, nome, creditos, aulasSemana):
    self.nome = nome
    self.creditos = creditos
    self.aulasSemana = aulasSemana
    
