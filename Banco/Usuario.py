from abc import ABC, abstractmethod
from datetime import datetime
import random
from Saldo import Saldo

class Usuario(ABC):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._endereco = endereco
        self._senha = senha
        self._numero_conta_corrente = numero_conta_corrente
        self._saldo = Saldo(numero_conta_corrente)

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def endereco(self):
        return self._endereco

    @property
    def numero_conta_corrente(self):
        return self._numero_conta_corrente

    @property
    def saldo(self):
        return self._saldo

    @staticmethod
    def validar_data_nascimento(data):
        try:
            hoje = datetime.now()
            data_nasc = datetime.strptime(data, "%d/%m/%Y")
            return data_nasc <= hoje
        except ValueError:
            return False

    @staticmethod
    def gerar_numero_conta_corrente():
        return str(random.randint(100000, 999999))

    def validar_senha(self, senha):
        return self._senha == senha

    @abstractmethod
    def tipo_usuario(self):
        pass


class Aluno(Usuario):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente, numero_matricula, fumpista, nivel_fump=None):
        super().__init__(nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente)
        self.numero_matricula = numero_matricula
        self.fumpista = fumpista
        self.nivel_fump = nivel_fump if fumpista else None

    def tipo_usuario(self):
        return "Aluno"


class Professor(Usuario):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente, numero_matricula):
        super().__init__(nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente)
        self.numero_matricula = numero_matricula

    def tipo_usuario(self):
        return "Professor"
