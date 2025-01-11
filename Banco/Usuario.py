from abc import ABC, abstractmethod
from datetime import datetime
import random


class Usuario(ABC):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._endereco = endereco
        self._senha = senha
        self._numero_conta_corrente = numero_conta_corrente

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

    def validar_senha(self, senha):
        return self._senha == senha

    @staticmethod
    def validar_cpf(cpf):
        return len(cpf) == 11 and cpf.isdigit()

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

    @staticmethod
    def criar_usuario(tipo, **kwargs):
        if not Usuario.validar_cpf(kwargs.get("cpf", "")):
            raise ValueError("CPF inválido. Deve conter 11 dígitos.")

        if not Usuario.validar_data_nascimento(kwargs.get("data_nascimento", "")):
            raise ValueError("Data de nascimento inválida.")

        if tipo == "Aluno":
            return Aluno(**kwargs)
        elif tipo == "Servidor":
            return Servidor(**kwargs)
        else:
            raise ValueError(f"Tipo de usuário desconhecido: {tipo}")

    @abstractmethod
    def tipo_usuario(self):
        pass


class Aluno(Usuario):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente, numero_matricula, fumpista=False, nivel_fump=None):
        super().__init__(nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente)
        self.numero_matricula = numero_matricula
        self.fumpista = fumpista
        self.nivel_fump = nivel_fump

    def tipo_usuario(self):
        return "Aluno"

    def definir_nivel_fump(self, nivel):
        if nivel not in [None, "I", "II", "III", "IV"]:
            raise ValueError("Nível FUMP inválido.")
        self.nivel_fump = nivel
        self.fumpista = nivel is not None


class Servidor(Usuario):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente):
        super().__init__(nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente)

    def tipo_usuario(self):
        return "Servidor"
